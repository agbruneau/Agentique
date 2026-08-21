// Côté WASM du banc DT1, et comparateur.
//
// Node exécute le même moteur WebAssembly que le navigateur visé par O5 : la
// mesure porte donc sur la cible réelle du produit, pas sur un substitut WASI.
//
// Usage : node banc.mjs <fichier.wasm> <sortie-native.tsv> [n]
//
// Sortie : une ligne par groupe, puis le verdict. Le code de sortie ne vaut 1
// que si un groupe à parité **exigée** diverge : la divergence des
// transcendantes `std` est le constat qui fonde DT1, pas une régression. Un
// banc qui échouerait sur son propre résultat ne pourrait pas servir de test
// permanent pour NF-02.

import { readFile } from 'node:fs/promises';

const [, , cheminWasm, cheminNatif, nBrut] = process.argv;
if (!cheminWasm || !cheminNatif) {
  console.error('usage: node banc.mjs <fichier.wasm> <sortie-native.tsv> [n]');
  process.exit(2);
}
const n = Number(nBrut ?? 1_000_000);

const { instance } = await WebAssembly.instantiate(await readFile(cheminWasm), {});
const { banc_dt1, banc_dt1_nb_groupes } = instance.exports;

// La sortie native porte le nom de chaque groupe ; on le réutilise plutôt que
// de dupliquer la liste ici. Une divergence de nomenclature serait un défaut
// silencieux du banc lui-même.
const natif = new Map();
for (const ligne of (await readFile(cheminNatif, 'utf8')).split(/\r?\n/)) {
  if (!ligne || ligne.startsWith('#')) continue;
  const [g, hachage, parite, nom] = ligne.split('\t');
  natif.set(Number(g), { hachage, nom, exigee: parite === 'exigée' });
}

const nbGroupes = banc_dt1_nb_groupes();
if (natif.size !== nbGroupes) {
  console.error(`sortie native incomplète : ${natif.size} groupes sur ${nbGroupes}`);
  process.exit(2);
}

console.log(`# banc DT1 — wasm32-unknown-unknown sous Node ${process.version} — ${n} itérations par groupe\n`);
console.log('groupe                                        parité   natif             wasm              verdict');

const ecartsExiges = [];
const ecartsConstates = [];
// Compté sur la colonne « parité exigée », et non par soustraction des groupes
// qui n'ont pas divergé : `mul_add` est un groupe *constat* et coïncidait au
// dernier passage, ce qui gonflait le verdict de 8 à 9 sans qu'aucune parité
// exigée de plus n'ait été vérifiée.
let nbExiges = 0;
for (let g = 0; g < nbGroupes; g++) {
  const attendu = natif.get(g);
  const obtenu = BigInt.asUintN(64, banc_dt1(g, n)).toString(16).padStart(16, '0');
  const identique = obtenu === attendu.hachage;
  if (attendu.exigee) nbExiges += 1;
  if (!identique) (attendu.exigee ? ecartsExiges : ecartsConstates).push(attendu.nom);
  console.log(
    `${attendu.nom.padEnd(44)}  ${(attendu.exigee ? 'exigée' : 'constat').padEnd(7)}  ` +
      `${attendu.hachage}  ${obtenu}  ${identique ? 'identique' : 'DIVERGE'}`,
  );
}

console.log('');
console.log(
  `constat : ${ecartsConstates.length} opération(s) de la bibliothèque de plateforme divergent` +
    `${ecartsConstates.length ? ' — ' + ecartsConstates.join(', ') : ''}.`,
);

if (ecartsExiges.length === 0) {
  console.log(`NF-02 : tenue sur ${nbExiges} groupes à parité exigée, ${n} itérations chacun.`);
} else {
  console.log(`NF-02 : VIOLÉE — ${ecartsExiges.join(', ')}.`);
  process.exit(1);
}
