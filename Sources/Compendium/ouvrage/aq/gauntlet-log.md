# Journal d'homologation `G4` (`gauntlet-loop` à l'aveugle)

- **Barre nommée, récupérable et comparable :** [Compendium/prd.md](file:///c:/Github/Agentique/Compendium/prd.md) (§ 1–5 *Sommaire exécutif global*, référentiels `01.2` / `36.2` et descriptifs ciblés par chapitre)
- **Protocole d'étanchéité (`AO-07`, `CA-15`) :** exécution intégrale hors tableau `swarm` via `invoke_subagent` ; critiques `research` neufs à chaque tour sans accès aux chemins sources, à `manifest.json` ni aux journaux des bâtisseurs ; comparaison binaire forcée (`A` ou `B`) en ordre alterné puis inversé au Tour 2.
- **Plafond budgétaire et arrêt :** convergence atteinte en `2` tours (`37/37` au Tour 1 ; `20/20` en ordre inversé au Tour 2).

---

## 1. Tour 1 — Évaluation à l'aveugle des `37` unités narratives (`r1/`)

Résultat global : **`37 / 37` victoires des unités rédigées (`candidat`)** face à l'étalon structurel `prd.md`, avec extraction systématique d'écarts actionnables concrets sur `20` unités (plus recalibrage des `5` unités `sur_calibre` sous `parser_plan` : `ch01`, `ch02`, `ch05`, `ch20`, `ch21`).

| Unité | Position `candidat` | Verdict binaire | Écart retenu / action vers Tour 2 |
|---|---:|---:|---|
| `00-liminaire` | `B` | `B` (Candidat) | Convergence nette ; aucune retouche requise |
| `ch01` | `A` | `A` (Candidat) | Préciser contrat `EXIG-D01-01.3` + garde-fou `BDI` et resserrer calibre (`5066 > 4989`) |
| `ch02` | `B` | `B` (Candidat) | Arbitrer `n ≥ 300` (Wilson) vs banc CI `50–100 × k=5` (`EXIG-D01-02.3`) et resserrer (`4310 > 4168`) |
| `ch03` | `A` | `A` (Candidat) | Préciser critère de bascule `SLM` (`pass^k` / incertitude) et arbitrage sur site vs géré (`EXIG-D01-03.5`) |
| `ch04` | `B` | `B` (Candidat) | Convergence nette |
| `ch05` | `A` | `A` (Candidat) | Resserrer calibre sous `parser_plan` (`4232 > 4168`) sans perte de faits sourcés |
| `ch06` | `B` | `B` (Candidat) | Convergence nette |
| `ch07` | `A` | `A` (Candidat) | Convergence nette |
| `ch08` | `B` | `B` (Candidat) | Convergence nette |
| `ch09` | `A` | `A` (Candidat) | Convergence nette |
| `ch10` | `B` | `B` (Candidat) | Convergence nette |
| `ch11` | `A` | `A` (Candidat) | Convergence nette |
| `ch12` | `B` | `B` (Candidat) | Convergence nette |
| `ch13` | `A` | `A` (Candidat) | Convergence nette |
| `ch14` | `B` | `B` (Candidat) | Convergence nette |
| `ch15` | `A` | `A` (Candidat) | Convergence nette |
| `ch16` | `B` | `B` (Candidat) | Préciser TTL de fraîcheur et politique `fail-closed` `AgentCard` / `a2a_card.py` |
| `ch17` | `A` | `A` (Candidat) | Dissocier `G0` (`obo_dpop.py`/`revocation_fsm.py`) et `EXIG-IAM-15` (`TTL ≤ 15 min`, `RAR`, `SSF/CAEP`) |
| `ch18` | `B` | `B` (Candidat) | Expliciter cumul `Authorization`/`Txn-Token` + `DPoP` face à `8 192` o et rôle de `slh_dsa_fips205.py` |
| `ch19` | `A` | `A` (Candidat) | Préciser enveloppe/gestion HMAC cible sous `Cedar` vs socle `OPA/Rego` scellé en `G0` |
| `ch20` | `B` | `B` (Candidat) | Qualifier statut hors-`G0` de `< 1,5 ms` (`Cedar`) et runbooks `R1–R3`, et resserrer (`5349 > 5194`) |
| `ch21` | `A` | `A` (Candidat) | Arbitrer `Firecracker`/`gVisor`/`WASI 0.2`, `virtio-vsock`/`SSF-CAEP`, et resserrer (`4327 > 4168`) |
| `ch22` | `B` | `B` (Candidat) | Convergence nette |
| `ch23` | `A` | `A` (Candidat) | Convergence nette |
| `ch24` | `B` | `B` (Candidat) | Convergence nette |
| `ch25` | `A` | `A` (Candidat) | Convergence nette |
| `ch26` | `B` | `B` (Candidat) | Critères FinOps/latence `C2 (HYOK)` vs `C3 (TEE)` (`RTT ≤ 35 ms`, `PCR` distant) |
| `ch27` | `A` | `A` (Candidat) | Articuler tests substitutifs `a2a_card.py` (`CARD-SIGN`) et borne `EXIG-IAM-20` (`SSF/CAEP`) |
| `ch28` | `B` | `B` (Candidat) | Articuler `EXIG-INT-22` (`P3`) et `EXIG-CON-29` (`CIBA`, rétention `≥ 30 s`, rail `RTR pacs.008`) |
| `ch29` | `A` | `A` (Candidat) | Découpage temporel `Cognitive DR` (`T + 30 s` quiescence, `≤ 180 s` NVMe, Canary `T + 12 min`) |
| `ch30` | `B` | `B` (Candidat) | Borner protocole de dérogation `ARB` (`EXIG-ORC-29` : 6 mois, `EXIG-GOV-17`, révocation GitOps/`OPA`) |
| `ch31` | `A` | `A` (Candidat) | Convergence nette |
| `ch32` | `B` | `B` (Candidat) | Expliciter grille proportionnée `R1–R4` (§ 32.3) |
| `ch33` | `A` | `A` (Candidat) | Préciser bornes sourcées et auditables de `EXIG-HUM-01..04` |
| `ch34` | `B` | `B` (Candidat) | Expliciter filtrage `L0–L4 → PRR-75 / 305 EXIG-*` et ajouter `EXIG-HOM-02` au Tableau 34.3 |
| `ch35` | `A` | `A` (Candidat) | Clarifier `[Schéma conceptuel]` `C.5/C.6` vs CI `G0` et complexité `O(sauts)` vs `O(1)` (`pqc_http431.py`) |
| `ch36` | `B` | `B` (Candidat) | Nommer `CAP-025/028/033/046/052` et compléter l'arrimage `C1–C6` (`C3` et `C5` incluses) |

---

## 2. Interventions bâtisseurs (`self` hors essaim, lots strictement disjoints)

Quatre bâtisseurs parallèles (`G4-A`, `G4-B`, `G4-C`, `G4-D`) ont appliqué les rectifications sourcées sur les `20` chapitres cibles en préservant intégralement les `14` blocs `CA-G0-SYNC`, la charte `fr-CA` et les plages `[min_words, max_words]` sous les **deux** compteurs (`verifie_manuscrit` et `parser_plan` : `42 / 42` unités `conforme`).

---

## 3. Tour 2 — Contrôle à l'aveugle en ordre `A`/`B` inversé (`r2/`, 4 critiques neufs)

Résultat global : **`20 / 20` victoires des unités révisées (`100,0 %`)** malgré l'inversion stricte des positions `A`/`B` par rapport au Tour 1.

| Unité | Position Tour 1 | Position Tour 2 | Verdict Tour 2 | Observations transversales transmises au lissage `G5` (Task 8) |
|---|---:|---:|---:|---|
| `ch01` | `A` | `B` | `B` (Candidat) | Validé net (contrat `EXIG-D01-01.3` et bornes `EXIG-ORC-26/27` jugés nets) |
| `ch02` | `B` | `A` | `A` (Candidat) | Validé net (arbitrage Wilson `n ≥ 300` vs CI `50–100 × k=5` jugé net) |
| `ch03` | `A` | `B` | `B` (Candidat) | Validé net (seuils `SLM`/`LLM` et arbitrage `C04` jugés nets) |
| `ch05` | `A` | `B` | `B` (Candidat) | Validé net (définition `D1–D8`, `Stades 0–4`, matrice et `CIBA`) |
| `ch16` | `B` | `A` | `A` (Candidat) | Validé net ; vérifier cohérence lexicale `0/15` vs `3×5` et versions `WIMSE` en `G5` |
| `ch17` | `A` | `B` | `B` (Candidat) | Validé net (frontière `G0` / `STS-PDP` et `fail-closed SSF/CAEP`) |
| `ch18` | `B` | `A` | `A` (Candidat) | Validé net (mesures `pqc_http431.py`, `DPoP` + `Txn-Token`, rôle `slh_dsa_fips205.py`) |
| `ch19` | `A` | `B` | `B` (Candidat) | Validé net (socle `G0` vs cible `HMAC`/`Cedar` Tome 3) |
| `ch20` | `B` | `A` | `A` (Candidat) | Validé net (`OPA 45/45` vs cible `< 1,5 ms` hors `G0`, calibre `5006 pp` conforme) |
| `ch21` | `A` | `B` | `B` (Candidat) | Validé net (`Firecracker`/`gVisor`/`WASI 0.2`, `virtio-vsock`, calibre `3948 pp` conforme) |
| `ch26` | `B` | `A` | `A` (Candidat) | Validé ; expliciter repli `fail-closed` en `C2 > 35 ms` lors du lissage `G5` |
| `ch27` | `A` | `B` | `B` (Candidat) | Validé ; harmoniser libellé note `2` provisoire vs `< 2` au Tableau 27.1 en `G5` |
| `ch28` | `B` | `A` | `A` (Candidat) | Validé ; clarifier lien `EXIG-INT-22` (`P3`) vs seuil `EXIG-CON-29` (`30 s`) en `G5` |
| `ch29` | `A` | `B` | `B` (Candidat) | Validé ; expliciter la zone `[0,90 ; 0,94 · pass^5_nominal[` en `G5` |
| `ch30` | `B` | `A` | `A` (Candidat) | Validé ; lier explicitement les 10 anti-patrons aux 12 codes `AP-01..12` en `G5` |
| `ch32` | `B` | `A` | `A` (Candidat) | Validé ; nettoyer toute étiquette `Classe 1` résiduelle sous `DISC-02` en `G5` |
| `ch33` | `A` | `B` | `B` (Candidat) | Validé ; harmoniser bascule `L0` vs `N2 < 60 s` dans `EXIG-HUM-04` en `G5` |
| `ch34` | `B` | `A` | `A` (Candidat) | Validé ; harmoniser `L2–L4` vs `L3–L4` (24 portes) en `G5` |
| `ch35` | `A` | `B` | `B` (Candidat) | Validé ; rappeler la limite `NOT_AUTOMATABLE` au Tableau 35.1 en `G5` |
| `ch36` | `B` | `A` | `A` (Candidat) | Validé ; supprimer toute mention résiduelle `Stade 3` sous `DISC-02` et renvoi `Annexe C` en `G5` |

---

## 4. Clôture de barrière `G4`

- **Verdict `G4` :** **VALIDÉE** (convergence `37/37` au Tour 1 et `20/20` au Tour 2 en ordre inversé ; l'intégralité des micro-raccords inter-chapitres détectés au Tour 2 est versée au mandat du `lisseur-editorial` en Task 8 `G5`).
