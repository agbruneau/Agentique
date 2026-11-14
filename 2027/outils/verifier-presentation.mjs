// Vérifie la mise en page, les interactions, l'intégrité du contenu et le contraste WCAG 2.1
// de 2027/Presentation.html dans Edge ou Chrome sans interface.
//
// Usage : node outils/verifier-presentation.mjs
// Navigateur : variable d'environnement NAVIGATEUR, sinon Edge puis Chrome aux emplacements usuels.
// Code de sortie : 0 si tout est conforme, 1 sinon.
import { spawn, spawnSync } from 'node:child_process';
import { existsSync, mkdtempSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const PORT = 9250 + Math.floor(Math.random() * 650);
const pageUrl = pathToFileURL(fileURLToPath(new URL('../Presentation.html', import.meta.url))).href;
const pdfPath = fileURLToPath(new URL('../CompendiumMaster.pdf', import.meta.url));

const browser = [
  process.env.NAVIGATEUR,
  'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
  'C:/Program Files/Microsoft/Edge/Application/msedge.exe',
  'C:/Program Files/Google/Chrome/Application/chrome.exe',
  '/usr/bin/microsoft-edge',
  '/usr/bin/google-chrome',
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
].find((p) => p && existsSync(p));

if (!browser) {
  console.error('Aucun navigateur Chromium trouvé : définir NAVIGATEUR.');
  process.exit(2);
}
if (!existsSync(pdfPath)) {
  console.error(`Fichier cible absent : ${pdfPath}`);
  process.exit(2);
}

const proc = spawn(browser, [
  '--headless=new',
  `--remote-debugging-port=${PORT}`,
  `--user-data-dir=${mkdtempSync(join(tmpdir(), 'verif-2027-'))}`,
  'about:blank',
]);

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const quit = async (code) => {
  try {
    const { webSocketDebuggerUrl } = await (await fetch(`http://127.0.0.1:${PORT}/json/version`)).json();
    const b = new WebSocket(webSocketDebuggerUrl);
    await new Promise((r, j) => { b.onopen = r; b.onerror = j; });
    b.send(JSON.stringify({ id: 1, method: 'Browser.close' }));
    await sleep(400);
  } catch {}
  try {
    if (process.platform === 'win32') spawnSync('taskkill', ['/pid', String(proc.pid), '/T', '/F'], { stdio: 'ignore' });
    else proc.kill();
  } catch {}
  process.exit(code);
};

setTimeout(() => { console.error('Délai dépassé'); quit(2); }, 90000);
proc.on('error', (e) => { console.error(`Lancement impossible de ${browser} : ${e.message}`); quit(2); });

let onglet;
for (let i = 0; i < 40 && !onglet; i++) {
  try { onglet = (await (await fetch(`http://127.0.0.1:${PORT}/json`)).json()).find((t) => t.type === 'page'); } catch {}
  if (!onglet) await sleep(250);
}
if (!onglet) { console.error(`Navigateur injoignable sur le port ${PORT}`); await quit(2); }

const ws = new WebSocket(onglet.webSocketDebuggerUrl);
await new Promise((r) => (ws.onopen = r));
let id = 0;
const pending = {};
const runtimeErrors = [];
ws.onmessage = (e) => {
  const m = JSON.parse(e.data);
  if (m.method === 'Runtime.exceptionThrown') {
    runtimeErrors.push(m.params?.exceptionDetails?.text || 'Exception JS');
  }
  if (m.method === 'Runtime.consoleAPICalled' && m.params?.type === 'error') {
    runtimeErrors.push((m.params.args || []).map((a) => a.value ?? a.description).join(' '));
  }
  pending[m.id]?.(m);
};

const send = (method, params = {}) =>
  new Promise((r) => { pending[++id] = r; ws.send(JSON.stringify({ id, method, params })); })
    .then((m) => { if (m.error) throw new Error(`${method} : ${m.error.message}`); return m.result; });

const ev = async (expression) => {
  const res = await send('Runtime.evaluate', { expression, returnByValue: true });
  if (res.exceptionDetails) throw new Error(res.exceptionDetails.text);
  return res.result.value;
};

await send('Runtime.enable');
await send('Page.enable');
await send('Network.enable');

const VIEWPORTS = [
  { w: 375, h: 812, block: false, label: '375x812 (mobile)' },
  { w: 768, h: 1024, block: false, label: '768x1024 (tablette)' },
  { w: 1366, h: 768, block: false, label: '1366x768 (portable)' },
  { w: 1920, h: 1080, block: false, label: '1920x1080 (bureau)' },
  { w: 1366, h: 768, block: true, label: '1366x768 (polices bloquées)' },
];

const CHECK_LAYOUT_AND_WCAG = `(() => {
  const issues = [];
  const doc = document.documentElement;
  if (doc.scrollWidth > doc.clientWidth + 1) {
    const culprits = [...document.querySelectorAll('body *')]
      .filter((el) => {
        const cs = getComputedStyle(el);
        return cs.display !== 'none' && el.getBoundingClientRect().right > doc.clientWidth + 1;
      })
      .map((el) => '<' + el.localName + (el.id ? '#' + el.id : '') + (el.className ? '.' + String(el.className).trim().split(/\\s+/)[0] : '') + '>(' + Math.round(el.getBoundingClientRect().right) + ')')
      .slice(0, 4);
    issues.push('Débordement horizontal global : ' + (doc.scrollWidth - doc.clientWidth) + ' px [' + culprits.join(', ') + ']');
  }
  document.querySelectorAll('.card, .card-elev, .ch-card, .tl-card, .theme-detail, .arch-inspector, .reality-panel')
    .forEach((el) => {
      if (el.offsetParent === null) return;
      if (el.scrollWidth > el.clientWidth + 2) {
        issues.push('Carte déborde en largeur (' + (el.scrollWidth - el.clientWidth) + ' px) : ' + el.textContent.trim().slice(0, 32));
      }
    });

  // Audit contraste WCAG 2.1 sur tous les éléments textuels visibles
  const parseRgba = (str) => {
    const m = str.match(/rgba?\\(([^)]+)\\)/i);
    if (!m) return null;
    const parts = m[1].split(/[\\s,/]+/).filter(Boolean).map(Number);
    return { r: parts[0], g: parts[1], b: parts[2], a: parts[3] === undefined ? 1 : parts[3] };
  };
  const blend = (fg, bg) => {
    const a = fg.a;
    return {
      r: fg.r * a + bg.r * (1 - a),
      g: fg.g * a + bg.g * (1 - a),
      b: fg.b * a + bg.b * (1 - a),
      a: 1
    };
  };
  const lum = (c) => {
    const s = [c.r, c.g, c.b].map((v) => {
      const x = v / 255;
      return x <= 0.03928 ? x / 12.92 : Math.pow((x + 0.055) / 1.055, 2.4);
    });
    return 0.2126 * s[0] + 0.7152 * s[1] + 0.0722 * s[2];
  };
  const ratio = (c1, c2) => {
    const l1 = lum(c1), l2 = lum(c2);
    return (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);
  };
  const effectiveBg = (el) => {
    const stack = [];
    let cur = el;
    while (cur && cur.nodeType === 1) {
      const bg = parseRgba(getComputedStyle(cur).backgroundColor);
      if (bg && bg.a > 0) stack.unshift(bg);
      cur = cur.parentElement;
    }
    let acc = { r: 5, g: 5, b: 6, a: 1 };
    for (const layer of stack) acc = blend(layer, acc);
    return acc;
  };

  let checkedText = 0;
  let minRatio = Infinity;
  const contrastFailures = [];
  document.querySelectorAll('body *').forEach((el) => {
    if (el.classList.contains('sr-only') || el.classList.contains('skip-link')) return;
    const hasText = [...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim().length > 0);
    if (!hasText) return;
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden' || parseFloat(cs.opacity) === 0) return;
    const r = el.getBoundingClientRect();
    if (r.width === 0 || r.height === 0) return;
    const fg = parseRgba(cs.color);
    if (!fg) return;
    const bg = effectiveBg(el);
    const effFg = fg.a < 1 ? blend(fg, bg) : fg;
    const cr = ratio(effFg, bg);
    const fs = parseFloat(cs.fontSize);
    const fw = parseInt(cs.fontWeight, 10) || 400;
    const isLarge = fs >= 24 || (fs >= 18.66 && fw >= 700);
    const threshold = isLarge ? 3.0 : 4.5;
    checkedText++;
    minRatio = Math.min(minRatio, cr);
    if (cr < threshold) {
      contrastFailures.push(
        cr.toFixed(2) + ':1 (< ' + threshold + ') sur <' + el.localName + '> « ' + el.textContent.trim().slice(0, 28) + ' »'
      );
    }
  });
  if (contrastFailures.length) {
    issues.push('Contraste WCAG insuffisant (' + contrastFailures.length + ') : ' + contrastFailures.slice(0, 4).join(' ; '));
  }
  return { issues, checkedText, minRatio: minRatio === Infinity ? 0 : Number(minRatio.toFixed(2)) };
})()`;

let totalFailures = 0;

for (const vp of VIEWPORTS) {
  await send('Emulation.setDeviceMetricsOverride', {
    width: vp.w, height: vp.h, deviceScaleFactor: 1, mobile: vp.w < 780,
  });
  await send('Network.setBlockedURLs', {
    urls: vp.block ? ['*fonts.googleapis.com*', '*fonts.gstatic.com*'] : [],
  });
  await send('Page.navigate', { url: pageUrl });
  await sleep(1600);

  const res = await ev(CHECK_LAYOUT_AND_WCAG);
  const fonts = await ev(`[...new Set([...document.fonts].filter(f => f.status === 'loaded').map(f => f.family))].join(', ') || 'repli système'`);
  if (res.issues.length) totalFailures++;
  console.log(
    `${vp.label.padEnd(28)} · polices : ${fonts.padEnd(32)} · ${res.checkedText} nœuds · min ${res.minRatio}:1 · ${res.issues.join(' | ') || 'OK'}`
  );
}

// Tests d'intégrité des données et des interactions (1366x768)
await send('Emulation.setDeviceMetricsOverride', { width: 1366, height: 768, deviceScaleFactor: 1, mobile: false });
await send('Network.setBlockedURLs', { urls: [] });
await send('Page.navigate', { url: pageUrl });
await sleep(1400);

const functionalIssues = await ev(`(() => {
  const err = [];
  if (document.querySelectorAll('#themesNav .theme-tab').length !== 8) err.push('8 thématiques attendues');
  if (document.querySelectorAll('[data-arch]').length !== 8) err.push('8 briques d architecture attendues');
  if (document.querySelectorAll('#levelsTabs .lvl-btn').length !== 5) err.push('5 niveaux L0-L4 attendus');
  if (document.querySelectorAll('#rolesGrid .role-btn').length !== 6) err.push('6 parcours attendus');
  if (document.querySelectorAll('#chaptersGrid .ch-card').length !== 50) err.push('50 chapitres attendus');
  if (document.querySelectorAll('#annexesGrid .card').length !== 8) err.push('8 annexes attendues');
  const pdfLink = document.querySelector('a[href="CompendiumMaster.pdf"]');
  if (!pdfLink) err.push('Lien CompendiumMaster.pdf manquant');

  // Vérification des 31 codes ADR uniques
  const adrTxt = document.getElementById('chaptersGrid').textContent;
  for (let i = 1; i <= 31; i++) {
    const code = 'ADR-' + String(i).padStart(3, '0');
    if (!adrTxt.includes(code)) err.push('Code manquant : ' + code);
  }

  // Test interaction thématique T5
  document.querySelector('[data-theme="T5"]').click();
  if (!document.getElementById('themeDetail').textContent.includes('Confiance zéro')) {
    err.push('Interaction thématique T5 échouée');
  }

  // Test interaction simulateur L3
  document.querySelector('[data-lv="L3"]').click();
  if (!document.getElementById('levelDetail').textContent.includes('Autonomie bornée')) {
    err.push('Interaction niveau L3 échouée');
  }

  // Test simulateur Lusser (90% sur 5 étapes = 59,0 %)
  const pEl = document.getElementById('lusserP');
  const nEl = document.getElementById('lusserN');
  pEl.value = '90';
  nEl.value = '5';
  pEl.dispatchEvent(new Event('input'));
  if (document.getElementById('lusserOut').textContent.trim() !== '59,0 %') {
    err.push('Calcul Lusser inattendu : ' + document.getElementById('lusserOut').textContent);
  }

  // Test architecture Couche 1
  document.querySelector('[data-arch="c1"]').click();
  if (!document.getElementById('archInspector').textContent.includes('Connectivité Outils')) {
    err.push('Interaction architecture Couche 1 échouée');
  }

  // Test chronologie filtre Canada
  document.querySelector('[data-tl="canada"]').click();
  if (document.querySelectorAll('#timelineGrid .tl-card').length < 3) {
    err.push('Filtre chronologie Canada inattendu');
  }

  // Test filtre rôle CISO (12 chapitres) puis réinitialisation (50 chapitres)
  document.querySelector('[data-role="ciso"]').click();
  document.getElementById('applyRoleFilter').click();
  const cisoCount = document.querySelectorAll('#chaptersGrid .ch-card').length;
  if (cisoCount !== 12) err.push('Filtre CISO attendu 12, reçu ' + cisoCount);
  document.getElementById('resetFilters').click();
  const resetCount = document.querySelectorAll('#chaptersGrid .ch-card').length;
  if (resetCount !== 50) err.push('Réinitialisation attendue 50, reçu ' + resetCount);

  // Test recherche texte "Temporal"
  const sEl = document.getElementById('searchInput');
  sEl.value = 'Temporal';
  sEl.dispatchEvent(new Event('input'));
  const searchCount = document.querySelectorAll('#chaptersGrid .ch-card').length;
  if (searchCount < 1 || searchCount >= 50) err.push('Recherche Temporal inattendue : ' + searchCount);
  document.getElementById('resetFilters').click();

  return err;
})()`);

if (functionalIssues.length) {
  totalFailures++;
  console.error('Contrôles fonctionnels en échec :', functionalIssues);
} else {
  console.log('Contrôles structurels et interactifs : OK (8 thématiques, 8 briques, 5 niveaux, 6 parcours, 50 chapitres, 31 ADR, 8 annexes)');
}

if (runtimeErrors.length) {
  totalFailures++;
  console.error('Erreurs JS / console :', runtimeErrors);
} else {
  console.log('Console et exceptions JS : 0 erreur');
}

console.log(totalFailures ? `ÉCHEC (${totalFailures} catégorie(s) en défaut)` : 'Tout est conforme.');
await quit(totalFailures ? 1 : 0);
