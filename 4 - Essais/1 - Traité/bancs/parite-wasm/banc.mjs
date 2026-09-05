// Côté WASM du banc EX-V12, et comparateur.
//
// Usage : node banc.mjs <fichier.wasm> <sortie-native.tsv> [graine] [budget]
//
// Toute divergence est un **défaut bloquant** : contrairement au banc DT1, il
// n'y a ici aucune ligne « constat ». Un chiffre qui diffère entre les deux
// cibles signifie que le destinataire d'un lien partagé ne voit pas la même
// figure, ce qui vide EX-V09 de son sens en même temps qu'EX-V12.

import { readFile } from 'node:fs/promises';

const [, , cheminWasm, cheminNatif, graineBrute, budgetBrut] = process.argv;
if (!cheminWasm || !cheminNatif) {
  console.error('usage: node banc.mjs <fichier.wasm> <sortie-native.tsv> [graine] [budget]');
  process.exit(2);
}
const graine = BigInt(graineBrute ?? 1);
const budget = BigInt(budgetBrut ?? 20000);

const { instance } = await WebAssembly.instantiate(await readFile(cheminWasm), {});
const { banc_parite, banc_parite_nb_cas } = instance.exports;

const natif = new Map();
for (const ligne of (await readFile(cheminNatif, 'utf8')).split(/\r?\n/)) {
  if (!ligne || ligne.startsWith('#')) continue;
  const [cas, empreinte, nom] = ligne.split('\t');
  natif.set(Number(cas), { empreinte, nom });
}

const nbCas = banc_parite_nb_cas();
if (natif.size !== nbCas) {
  console.error(`sortie native incomplète : ${natif.size} cas sur ${nbCas}`);
  process.exit(2);
}

console.log(`# banc EX-V12 — wasm32-unknown-unknown sous Node ${process.version}`);
console.log(`# graine ${graine}, budget ${budget}\n`);
console.log('cas                            natif             wasm              verdict');

const divergents = [];
for (let cas = 0; cas < nbCas; cas++) {
  const attendu = natif.get(cas);
  const obtenu = BigInt.asUintN(64, banc_parite(cas, graine, budget))
    .toString(16)
    .padStart(16, '0');
  const identique = obtenu === attendu.empreinte;
  if (!identique) divergents.push(attendu.nom);
  console.log(
    `${attendu.nom.padEnd(30)} ${attendu.empreinte}  ${obtenu}  ${identique ? 'identique' : 'DIVERGE'}`,
  );
}

console.log('');
if (divergents.length === 0) {
  console.log(`EX-V12 : tenue sur ${nbCas} cas — le destinataire voit exactement la même figure.`);
} else {
  console.log(`EX-V12 : VIOLÉE — ${divergents.join(', ')}. Défaut bloquant.`);
  process.exit(1);
}
