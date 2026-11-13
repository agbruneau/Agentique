// Vérifie la mise en page de Presentation.html dans Edge ou Chrome sans interface.
//
// Pour chaque diapositive : débordement horizontal, cartes qui débordent, blocs qui se
// chevauchent (en-tête, blocs du corps, pied de page), pied de page masqué par les
// contrôles, défilement interne (interdit au-delà de 1024 px de large, signalé en deçà)
// et plus petite taille de texte.
//
// Usage : node outils/verifier-presentation.mjs [largeur] [hauteur] [options]
//   options : print          mise en page d'impression (média print émulé)
//             block          bloque Google Fonts (cas hors ligne, police de repli)
//             pdf=sortie.pdf écrit aussi le PDF A4 paysage
//   Navigateur : variable d'environnement NAVIGATEUR, sinon Edge puis Chrome aux emplacements usuels.
//
// Code de sortie : 0 si tout est conforme, 1 sinon.
import { spawn, spawnSync } from 'node:child_process';
import { existsSync, mkdtempSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const args = process.argv.slice(2);
const [W = 1366, H = 768] = args.filter((a) => /^\d+$/.test(a)).map(Number);
const PRINT = args.includes('print');
const BLOCK = args.includes('block');
const PDF = (args.find((a) => a.startsWith('pdf=')) || '').slice(4);
const PORT = 9200 + Math.floor(Math.random() * 700);

const page = pathToFileURL(fileURLToPath(new URL('../Presentation.html', import.meta.url))).href;
const browser = [
  process.env.NAVIGATEUR,
  'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
  'C:/Program Files/Microsoft/Edge/Application/msedge.exe',
  'C:/Program Files/Google/Chrome/Application/chrome.exe',
  '/usr/bin/microsoft-edge',
  '/usr/bin/google-chrome',
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
].find((p) => p && existsSync(p));
if (!browser) { console.error('Aucun navigateur Chromium trouvé : définir NAVIGATEUR.'); process.exit(2); }

const proc = spawn(browser, [
  '--headless=new', `--remote-debugging-port=${PORT}`,
  `--user-data-dir=${mkdtempSync(join(tmpdir(), 'verif-pres-'))}`, 'about:blank',
]);
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
// Fermeture du navigateur par le protocole (Browser.close) : sous Windows, le lanceur d'Edge
// passe la main à un processus détaché que kill() n'atteint pas. taskkill /T reste en repli.
const quit = async (code) => {
  try {
    const { webSocketDebuggerUrl } = await (await fetch(`http://127.0.0.1:${PORT}/json/version`)).json();
    const b = new WebSocket(webSocketDebuggerUrl);
    await new Promise((r, j) => { b.onopen = r; b.onerror = j; });
    b.send(JSON.stringify({ id: 1, method: 'Browser.close' }));
    await sleep(500);
  } catch {}
  try {
    if (process.platform === 'win32') spawnSync('taskkill', ['/pid', String(proc.pid), '/T', '/F'], { stdio: 'ignore' });
    else proc.kill();
  } catch {}
  process.exit(code);
};
setTimeout(() => { console.error('Délai dépassé'); quit(2); }, 100000);

proc.on('error', (e) => { console.error(`Lancement impossible de ${browser} : ${e.message}`); quit(2); });

// onglet de la page, attendu 10 s au plus (liste vide tant que le navigateur démarre)
let onglet;
for (let i = 0; i < 40 && !onglet; i++) {
  try { onglet = (await (await fetch(`http://127.0.0.1:${PORT}/json`)).json()).find((t) => t.type === 'page'); } catch {}
  if (!onglet) await sleep(250);
}
if (!onglet) { console.error(`Navigateur injoignable sur le port ${PORT} : ${browser}`); await quit(2); }
const ws = new WebSocket(onglet.webSocketDebuggerUrl);
await new Promise((r) => (ws.onopen = r));
let id = 0;
const pending = {};
ws.onmessage = (e) => { const m = JSON.parse(e.data); pending[m.id]?.(m); };
const send = (method, params = {}) =>
  new Promise((r) => { pending[++id] = r; ws.send(JSON.stringify({ id, method, params })); })
    .then((m) => { if (m.error) throw new Error(`${method} : ${m.error.message}`); return m.result; });
const ev = async (expression) => (await send('Runtime.evaluate', { expression, returnByValue: true })).result.value;

await send('Emulation.setDeviceMetricsOverride', { width: W, height: H, deviceScaleFactor: 1, mobile: W < 780 });
if (BLOCK) {
  await send('Network.enable');
  await send('Network.setBlockedURLs', { urls: ['*fonts.googleapis.com*', '*fonts.gstatic.com*'] });
}
await send('Page.navigate', { url: page });
await sleep(2500);
if (PRINT) { await send('Emulation.setEmulatedMedia', { media: 'print' }); await sleep(400); }

const fonts = await ev(`[...new Set([...document.fonts].filter(f => f.status === 'loaded').map(f => f.family + ' ' + f.weight))].join(', ') || 'aucune (repli système)'`);
console.log(`${W}×${H} · ${PRINT ? 'impression' : 'écran'} · polices web : ${fonts}`);

const probe = (i) => `(() => {
  const s = document.querySelectorAll('.slide')[${i}];
  const deep = (e) => Math.max(e.getBoundingClientRect().bottom, ...[...e.querySelectorAll('*')].map((c) => c.getBoundingClientRect().bottom));
  const nom = (e) => e.className.split(' ')[0] || e.localName;
  const issues = [];
  if (s.scrollWidth > s.clientWidth + 1) issues.push('débordement horizontal ' + (s.scrollWidth - s.clientWidth) + ' px');
  const blocks = [s.querySelector('header'), ...s.querySelector('.body').children, s.querySelector('.foot')];
  for (let k = 0; k < blocks.length - 1; k++) {
    const ov = deep(blocks[k]) - blocks[k + 1].getBoundingClientRect().top;
    if (ov > 1) issues.push(nom(blocks[k]) + ' chevauche ' + nom(blocks[k + 1]) + ' de ' + Math.round(ov) + ' px');
  }
  // défilement interne : interdit sur grand écran, permis (et signalé) à 1024 px et moins
  const notes = [];
  const surplus = s.scrollHeight - s.clientHeight;
  if (surplus > 1) {
    if (${W} > 1024 || ${PRINT}) issues.push('défilement interne de ' + surplus + ' px');
    else notes.push('défile de ' + surplus + ' px (permis)');
  }
  const fond = s.getBoundingClientRect().top + Math.max(s.clientHeight, s.scrollHeight);
  const out = deep(blocks[blocks.length - 1]) - fond;
  if (out > 1) issues.push('pied de page hors diapositive de ' + Math.round(out) + ' px');
  // contrôles flottants : ils ne doivent masquer aucun texte du pied de page, mesuré là où
  // il se lit (en bas du défilement quand la diapositive défile)
  const hud = document.querySelector('.hud');
  if (hud && getComputedStyle(hud).display !== 'none') {
    s.scrollTop = s.scrollHeight;
    const h = hud.getBoundingClientRect();
    [...s.querySelector('.foot').children].forEach((c) => {
      const r = c.getBoundingClientRect();
      if (r.right > h.left + 1 && r.left < h.right - 1 && r.bottom > h.top + 1 && r.top < h.bottom - 1)
        issues.push('pied de page sous les contrôles (' + c.textContent.trim().slice(0, 24) + '…)');
    });
    s.scrollTop = 0;
  }
  s.querySelectorAll('.col,.tile,.fig,.row,.note')
    .forEach((b) => {
      if (b.scrollHeight > b.clientHeight + 1) issues.push(nom(b) + ' déborde de ' + (b.scrollHeight - b.clientHeight) + ' px');
      // texte insécable plus large que sa carte (masqué par overflow: hidden)
      if (b.scrollWidth > b.clientWidth + 1) issues.push(nom(b) + ' déborde en largeur de ' + (b.scrollWidth - b.clientWidth) + ' px (' + b.textContent.trim().slice(0, 16) + '…)');
    });
  let min = Infinity;
  s.querySelectorAll('*').forEach((el) => {
    if ([...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim())) min = Math.min(min, parseFloat(getComputedStyle(el).fontSize));
  });
  return { min: min.toFixed(1), issues, notes };
})()`;

let failures = 0;
const total = await ev(`document.querySelectorAll('.slide').length`);
for (let i = 0; i < total; i++) {
  // navigation par les boutons du sommaire (goTo de la présentation)
  if (!PRINT) { await ev(`document.querySelectorAll('#tocList button')[${i}].click()`); await sleep(450); }
  const { min, issues, notes } = await ev(probe(i));
  if (issues.length) failures++;
  console.log(`${String(i + 1).padStart(2, '0')}  texte min ${min} px  ${issues.join(' · ') || 'OK'}${notes.length ? ' · ' + notes.join(' · ') : ''}`);
}

if (PDF) {
  await send('Emulation.setEmulatedMedia', { media: '' });
  const { data } = await send('Page.printToPDF', { preferCSSPageSize: true, printBackground: true });
  writeFileSync(PDF, Buffer.from(data, 'base64'));
  console.log(`PDF écrit : ${PDF}`);
}
console.log(failures ? `${failures} diapositive(s) en défaut` : 'Tout est conforme');
quit(failures ? 1 : 0);
