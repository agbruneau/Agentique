# Lot L-11 — L-11

| Champ | Valeur |
|---|---|
| Lot | **L-11** — phase **P2**, jalon J-3 |
| Débloque | **ch. 16, 17, 18** |
| Date d'instruction | **21 juillet 2026** |
| Résultat | **9 affirmations** — 1 en [A], 0 écartée(s) par le vote. **6 échecs de source** consignés |
| Vote | **4 affirmation(s)** portant à elles seules une thèse de chapitre soumises au vote à trois juges, conformément au seuil déclaré (PRD §A.4). Les autres sont en **[B] par extraction citée** |
| Contrôle de bornage | **6 correction(s)** — contrôle systématique introduit en P2 sur constat de la relecture P1.4 |
| Statut | ☑ **CLOS** |

---

## A. Affirmations retenues (9)

| # | Niveau | Degré | Affirmation |
|---|---|---|---|
| `L11-A1` | **[B]** ⚖ | 1 | Au 21 juillet 2026, NIST IR 8547 « Transition to Post-Quantum Cryptography Standards » demeure à l'état d'Initial Public Draft : la fiche CSRC du document ne porte qu'une seule entrée d'historique, « 11/12/24: IR 8547 (Draft) », et sa période de commentaires publics est close depuis le 10 janvier 2025. |
| `L11-A2` | **[B]** ⚖ | 0 | Les jalons de dépréciation et d'interdiction de la cryptographie à clé publique vulnérable au quantique sont portés par un document à l'état de projet et s'y écrivent « Deprecated after 2030 » et « Disallowed after 2035 » : NIST IR 8547 ipd les applique, en §4.1.1 (signatures : ECDSA, EdDSA, RSA) et §4.1.2 (établissement de clés : DH et MQV en corps fini, ECDH, RSA), au niveau 112 bits pour la dépréciation, tous niveaux confon… |
| `L11-A3` | **[B]** | 0 | NIST IR 8547 ipd présente 2035 comme un plafond et non comme un plancher : le projet écrit que les normes d'algorithmes du NIST peuvent continuer de spécifier des techniques vulnérables au quantique jusqu'en 2035, tout en annonçant que les guides propres à une application pourront imposer des transitions plus précoces. |
| `L11-A4` | **[A]** ⚖ | 1 | Le décret présidentiel américain 14412 « Securing the Nation Against Advanced Cryptographic Attacks », signé le 22 juin 2026 et publié au Federal Register du 25 juin 2026 (vol. 91, n° 121, p. 38483), fait porter par l'OMB, sous 90 jours, une directive imposant aux agences fédérales la migration de tous les HVA et systèmes à impact élevé vers la PQC au 31 décembre 2030 pour l'établissement de clés et au 31 décembre 2031 pour le… |
| `L11-A5` | **[B]** ⚖ | 0 | La note OMB M-26-15 du 24 juin 2026, qui met en œuvre le décret 14412, ordonne aux agences fédérales d'aligner leur plan de migration sur NIST IR 8547 « ou un document successeur », et sa note de bas de page renvoie explicitement à l'URL du projet (csrc.nist.gov/pubs/ir/8547/ipd) : une obligation fédérale datée s'ancre ainsi sur un document encore à l'état d'Initial Public Draft. |
| `L11-A6` | **[B]** | 0 | FIPS 203 (ML-KEM) et FIPS 204 (ML-DSA) sont, eux, des normes finales publiées le 13 août 2024 — FIPS 203 portant en tête « Published: August 13, 2024 Effective: August 13, 2024 » — et l'écart de statut avec NIST IR 8547 est donc net : les algorithmes sont normalisés, le calendrier de retrait des algorithmes classiques ne l'est pas. |
| `L11-A7` | **[B]** | 1 | Le document « Quantum Safe Financial Forum — A call to action » d'Europol ne fixe aucune échéance calendaire propre au secteur financier : ses cinq recommandations sont non datées, et la seule échéance datée qu'il énonce est attribuée à l'administration américaine (« The US administration has set 2035 as the deadline for Federal Agencies to achieve quantum resistance »). |
| `L11-A8` | **[B]** | 1 | Le rapport conjoint « Prioritising Post-Quantum Cryptography Migration Activities in Financial Services » (Europol, Office des publications de l'Union européenne, Luxembourg, 2026) substitue à toute échéance calendaire une priorisation par le risque : le texte extrait de ses 26 pages ne contient aucune occurrence de « 2030 », « 2035 » ni « 8547 », et son avertissement précise qu'il n'est pas obligatoire et ne doit pas servir d… |
| `L11-A9` | **[B]** | 0 | La seule étude de coût de migration commanditée par une autorité publique que cette passe a ouverte est le rapport de juillet 2024 de l'Office of Management and Budget au Congrès, exigé par le Quantum Computing Cybersecurity Preparedness Act (Public Law 117-260) : l'Office of the National Cyber Director y projette environ 7,1 milliards de dollars de 2024 pour migrer les systèmes fédéraux civils prioritaires entre 2025 et 2035,… |

⚖ = soumise au vote adversarial à trois juges.

## C. Contrôle de bornage — 6 correction(s)

*Contrôle de forme, non de contenu : il ne juge pas la vérité du fait, il retire l'excès de l'énoncé.*

| # | Faute | Reformulation retenue |
|---|---|---|
| `L11-A1` | **degré injustifié** | Consultee le 21 juillet 2026, la fiche CSRC de NIST IR 8547 « Transition to Post-Quantum Cryptography Standards » affiche le statut Initial Public Draft, une entree d'historique unique — « 11/12/24: IR 8547 (Draft) » — et une periode de commentaires publics close le 10 janvier 2025. Aucune version finale n'y figure a cette date de consultation ; l'etat du document au-dela de ce que cette fiche affiche n'est pas etabl… |
| `L11-A3` | **verbe excessif** | NIST IR 8547 ipd ecrit que les normes d'algorithmes du NIST peuvent continuer de specifier des techniques vulnerables au quantique jusqu'en 2035, et annonce que des guides propres a une application pourront imposer des transitions plus precoces. Lecture de l'auteur : 2035 y fonctionne donc comme un plafond et non comme un plancher. |
| `L11-A4` | **clause d'exclusivité** | Le decret presidentiel americain 14412 « Securing the Nation Against Advanced Cryptographic Attacks », signe le 22 juin 2026 et publie au Federal Register du 25 juin 2026 (vol. 91, n° 121, p. 38483), charge l'OMB de publier sous 90 jours une directive de migration vers la PQC visant les HVA et les systemes a impact eleve, selon le perimetre que le decret definit, avec echeance au 31 decembre 2030 pour l'etablissement… |
| `L11-A6` | **négatif de corpus** | FIPS 203 (ML-KEM) et FIPS 204 (ML-DSA) sont des normes finales publiees le 13 aout 2024 — FIPS 203 portant en tete « Published: August 13, 2024 Effective: August 13, 2024 ». L'ecart de statut est donc net : les algorithmes sont normalises par ces deux FIPS, tandis que le calendrier de retrait porte par NIST IR 8547 demeure, a la fiche CSRC consultee le 21 juillet 2026, a l'etat d'Initial Public Draft. Cette passe n'a… |
| `L11-A7` | **clause d'exclusivité** | Le balayage du document « Quantum Safe Financial Forum — A call to action » (Europol), edition consultee le 21 juillet 2026, ne releve aucune echeance calendaire propre au secteur financier : ses cinq recommandations y sont enoncees sans date, et la seule echeance datee relevee au balayage est attribuee a l'administration americaine (« The US administration has set 2035 as the deadline for Federal Agencies to achieve… |
| `L11-A8` | **verbe excessif** | Le rapport conjoint « Prioritising Post-Quantum Cryptography Migration Activities in Financial Services » (Europol, Office des publications de l'Union europeenne, Luxembourg, 2026) ordonne ses activites de migration par le risque plutot que par un calendrier date : le balayage du texte extrait de ses 26 pages ne releve aucune occurrence de « 2030 », « 2035 » ni « 8547 ». Ce releve porte sur ces trois chaines seulemen… |

## D. Échecs de source consignés (6)

| Ce qui n'a pas pu être ouvert | Motif |
|---|---|
| Page de communiqué d'Europol annonçant le rapport conjoint de janvier 2026 (date de publication, liste des co-auteurs, lien PDF officiel) | Rendu JavaScript : la page ne renvoie que « Loading application. Please wait. ». La date du 21 janvier 2026 et la mention du groupe de travail canadien CFDIR ne reposent donc que sur des sources secondaires et ne sont PAS retenues comme fai… |
| Fiche de publication Europol du rapport 2026 (titre officiel, date, éditeurs, lien PDF) | Rendu JavaScript, même message de chargement. Contourné en ouvrant directement le PDF hébergé sur europol.europa.eu. |
| Fiche de publication Europol du « call to action » du QSFF (date de publication officielle) | Non ouverte ; le domaine sert ses pages de publication en rendu JavaScript (constaté sur deux pages sœurs). La date de février 2025 n'est donc adossée qu'aux métadonnées internes du PDF. |
| Vérification d'une version finale de NIST IR 8547 par URL directe | HTTP 404. Consigné pour mémoire seulement : une URL devinée qui renvoie 404 n'établit AUCUNE absence (règle B). L'absence de version finale est établie par l'énumération « Document History » de la fiche du document, pas par ce 404. |
| Vérification de l'existence d'un document successeur numéroté 8647 | HTTP 404 (de même que /pubs/ir/8647/final). Ne vaut pas preuve d'absence ; la piste est résolue autrement, par la lecture du fil pqc-forum dont le sujet porte « 8647 » alors que le corps du message annonce le document 8547. |
| Texte de FIPS 204 lui-même (clause d'entrée en vigueur, section « Qualifications ») | Non ouvert faute de temps dans cette passe. Le statut final et la date du 13 août 2024 sont établis sur la fiche CSRC ; la date d'entrée en vigueur n'a été constatée que pour FIPS 203. |

## E. Ce que le lot déclare n'avoir pas couvert

Ce lot établit le statut réel d'IR 8547 (a), ses jalons et leur formulation (b), le statut de FIPS 203/204 (c), les jalons du décret 14412 (d), les cibles du QSFF d'Europol (e) et une étude de coût commanditée (f). Ce qu'il ne couvre PAS.  1. Aucune clause d'exclusivité n'est revendiquée. Sur le point (f) en particulier, aucun balayage de la littérature n'a été mené : le rapport OMB de juillet 2024 est la seule étude de coût OUVERTE dans cette passe, ce qui ne dit rien de l'existence d'autres études. Les chiffres circulant dans la presse spécialisée (p. ex. « 15 milliards ») n'ont pas été instruits et ne sont pas rapportés.  2. La question « une version finale d'IR 8547 est-elle parue ? » est tranchée par l'énumération « Document History » de la fiche du document (une seule entrée, projet du 12 novembre 2024). Aucun calendrier de finalisation n'est annoncé par le NIST à la date de consultation : c'est un degré 3 (absence de documentation dans le corpus consulté), pas un fait négatif — ne pas écrire « le NIST n'a pas prévu de finaliser ».  3. Les jalons relevés viennent de QUATRE origines distinctes qui ne se fusionnent pas : (i) NIST IR 8547 ipd — dépréciation VISÉE après 2030, interdiction VISÉE après 2035, dans un projet ; (ii) décret 14412 — 31 décembre 2030 (établissement de clés) et 31 décembre 2031 (signatures) pour les HVA et systèmes fédéraux à impact élevé, plus une règle FAR proposée visant les contractants au 31 décembre 2030 ; (iii) note OMB M-26-15 — cinq phases 2026-2035, dont la seule prescription datée en « must » est la remise du plan sous 120 jours ; (iv) NSM-10, cité par IR 8547, qui fixe 2035 comme cible générale. Un jalon du NIST n'est pas une obligation légale ; l'obligation légale de 2030 ne porte pas sur la dépréciation mais sur la migration d'un périmètre nommé.  4. Rien n'a été instruit hors du couple États-Unis / Union européenne : ni le Canada (CFDIR, Centre canadien pour la cybersécurité), ni le Royaume-Uni (NCSC, calendrier 2028/2031/2035), ni l'ANSSI, ni le BSI. Le volume étant canadien, la lacune canadienne est la plus coûteuse et devrait faire l'objet d'une passe dédiée avant la rédaction du ch. 16.  5. Rien n'a été instruit sur l'application de ces jalons à la pile identitaire agentique elle-même (signatures de cartes d'agent, chaînes de mandat, jetons) : le lot fournit l'horloge, pas son incidence — cette incidence relèvera d'une inférence marquée « Lecture de l'auteur », pas d'un fait.  6. Deux limites de méthode à porter au registre. D'abord, tous les faits négatifs de ce lot reposent sur une extraction texte de PDF (PyMuPDF) : ce qui serait rendu en image échappe au balayage. Ensuite, cinq des sept documents primaires ont été récupérés en PDF et balayés localement, chaîne par chaîne, par mes soins ; les fiches CSRC (IR 8547, FIPS 203, FIPS 204, SP 800-131A Rev. 3) et le fil pqc-forum ont été lus via un outil de récupération web qui rend la page en texte — les citations qui en proviennent sont fidèles mais n'ont pas été recomptées sur fichier local.

## F. Sources et citations

### `L11-A1` — [B]

Au 21 juillet 2026, NIST IR 8547 « Transition to Post-Quantum Cryptography Standards » demeure à l'état d'Initial Public Draft : la fiche CSRC du document ne porte qu'une seule entrée d'historique, « 11/12/24: IR 8547 (Draft) », et sa période de commentaires publics est close depuis le 10 janvier 2025.

**Balayage (degré 1)** — Balayage de l'énumération « Document History » de la page csrc.nist.gov/pubs/ir/8547/ipd (consultée le 21 juillet 2026) : une seule entrée, « 11/12/24: IR 8547 (Draft) ». Balayage complémentaire du PDF du projet (29 pages, extraction texte intégrale) : la page 3 porte « Approved by the NIST Editorial Review Board on YYYY-MM-DD [Will be added to final publication.] », mention propre à un projet non approuvé. Les URL devinées csrc.nist.gov/pubs/ir/8547/final, /pubs/ir/8647/ipd et /pubs/ir/8647/final renvoient HTTP 404 — cela n'établit RIEN (URL devinée, pas balayage) et n'est consigné qu'en échec.

- **primaire** — IR 8547, Transition to Post-Quantum Cryptography Standards — Initial Public Draft, 12 novembre 2024, consultée le 2026-07-21 — <https://csrc.nist.gov/pubs/ir/8547/ipd>
  > 11/12/24: IR 8547 (Draft)
- **primaire** — NIST IR 8547 ipd, Transition to Post-Quantum Cryptography Standards — ipd, novembre 2024, consultée le 2026-07-21 — <https://nvlpubs.nist.gov/nistpubs/ir/2024/NIST.IR.8547.ipd.pdf>
  > Approved by the NIST Editorial Review Board on YYYY-MM-DD [Will be added to final publication.]
- **primaire** — SP 800-131A Rev. 3 (Initial Public Draft), Transitioning the Use of Cryptographic Algorithms and Key Lengths — Initial Public Draft, 21 octobre 2024, consultée le 2026-07-21 — <https://csrc.nist.gov/pubs/sp/800/131/a/r3/ipd>
  > Comments Due: December 4, 2024 (public comment period is CLOSED)
- **primaire** — NISTIR 8647, Transition to Post-Quantum Cryptography Standards (fil pqc-forum) — message du 12 novembre 2024, consultée le 2026-07-21 — <https://groups.google.com/a/list.nist.gov/g/pqc-forum/c/uHMw8RNGkC8>
  > NISTIR 8647, Transition to Post-Quantum Cryptography Standards

**Réserve** — Aucun document successeur portant un autre numéro n'a été constaté. Le fil pqc-forum dont le SUJET porte « NISTIR 8647 » annonce en corps le document 8547 : coquille de sujet, non second document — vérification faite sur le fil, dont le message est daté du 12 novembre 2024 et signé Dustin Moody (NIST). Le véhicule normatif que l'IR 8547 §4.1 désigne pour porter les échéances (SP 800-131A) est lui-même à l'état de projet : SP 800-131A Rev. 3 est un Initial Public Draft du 21 octobre 2024, commentaires clos le 4 décembre 2024. Absence de version finale = degré 1 sur une énumération bornée ; elle ne dit rien d'une finalisation à venir, non annoncée à la date de consultation.

### `L11-A2` — [B]

Les jalons de dépréciation et d'interdiction de la cryptographie à clé publique vulnérable au quantique sont portés par un document à l'état de projet et s'y écrivent « Deprecated after 2030 » et « Disallowed after 2035 » : NIST IR 8547 ipd les applique, en §4.1.1 (signatures : ECDSA, EdDSA, RSA) et §4.1.2 (établissement de clés : DH et MQV en corps fini, ECDH, RSA), au niveau 112 bits pour la dépréciation, tous niveaux confondus pour l'interdiction.

**Balayage (degré 0)** — Extraction texte intégrale des 29 pages du PDF NIST.IR.8547.ipd.pdf puis relevé de toutes les occurrences de « deprecat », « disallow », « 2030 », « 2035 » : 6 lignes « Deprecated after 2030 » et 12 lignes « Disallowed after 2035 » dans les tableaux des §4.1.1 et §4.1.2 ; aucune de ces lignes n'est formulée en obligation ni assortie d'une base légale.

- **primaire** — NIST IR 8547 ipd, Transition to Post-Quantum Cryptography Standards, §4.1.1 — ipd, novembre 2024, consultée le 2026-07-21 — <https://nvlpubs.nist.gov/nistpubs/ir/2024/NIST.IR.8547.ipd.pdf>
  > ECDSA [FIPS186] 112 bits of security strength Deprecated after 2030 Disallowed after 2035 ≥ 128 bits of security strength Disallowed after 2035
- **primaire** — NIST IR 8547 ipd, §4.1 — définitions et intention — ipd, novembre 2024, consultée le 2026-07-21 — <https://nvlpubs.nist.gov/nistpubs/ir/2024/NIST.IR.8547.ipd.pdf>
  > These guidelines had projected that NIST would disallow public-key schemes that provide 112 bits of security on January 1, 2031. However, based on the need to migrate to quantum-resistant algorithms during this timeframe, NIST intends to instead deprecate classical digital signatures at the 112-bit security level.
- **primaire** — NIST IR 8547 ipd, §4.1 — statuts d'approbation — ipd, novembre 2024, consultée le 2026-07-21 — <https://nvlpubs.nist.gov/nistpubs/ir/2024/NIST.IR.8547.ipd.pdf>
  > Deprecated means that the algorithm and key length/strength may be used, but there is some security risk. The data owner must examine this risk potential and decide whether to continue to use a deprecated algorithm or key length.

**Réserve** — Formulation imposée : dépréciation VISÉE pour 2030, interdiction VISÉE pour 2035, par un Initial Public Draft du NIST — jamais « interdit en 2035 ». Le document énonce une intention (« NIST intends to instead deprecate… ») et non une prescription en vigueur. Le vocabulaire est celui de SP 800-131A : « deprecated » n'est pas une interdiction, l'algorithme « may be used, but there is some security risk » et la décision revient au propriétaire des données. Ne jamais fusionner ces jalons avec ceux du décret 14412 ni avec ceux de la note M-26-15 (origines et régimes distincts, voir L11-A4 et L11-A5).

### `L11-A3` — [B]

NIST IR 8547 ipd présente 2035 comme un plafond et non comme un plancher : le projet écrit que les normes d'algorithmes du NIST peuvent continuer de spécifier des techniques vulnérables au quantique jusqu'en 2035, tout en annonçant que les guides propres à une application pourront imposer des transitions plus précoces.

**Balayage (degré 0)** — Lecture du §4.2 « Application-Specific Standards and Guidelines » dans l'extraction texte du PDF (p. 23-24 de l'imprimé) ; la phrase court sur deux pages et se lit en continu dans l'extraction.

- **primaire** — NIST IR 8547 ipd, §4.2 Application-Specific Standards and Guidelines — ipd, novembre 2024, consultée le 2026-07-21 — <https://nvlpubs.nist.gov/nistpubs/ir/2024/NIST.IR.8547.ipd.pdf>
  > While NIST's cryptographic algorithm standards may continue to specify quantum-vulnerable techniques until 2035 and generally allow their use, these application-specific standards and guidelines may specify earlier transitions for certain cryptographic algorithms, techniques, and protocols used within these applications.
- **primaire** — NIST IR 8547 ipd, §3.2 PQC-Classical Hybrid Protocols — ipd, novembre 2024, consultée le 2026-07-21 — <https://nvlpubs.nist.gov/nistpubs/ir/2024/NIST.IR.8547.ipd.pdf>
  > When used, hybrid solutions are typically expected to be temporary measures that lead to a second transition to cryptographic tools that use only PQC algorithms.

**Réserve** — Énoncé d'intention d'un projet, non d'un calendrier opposable. Le projet ne dit pas que les modes hybrides restent admis au-delà de 2035 : il dit que les solutions hybrides sont « typically expected to be temporary measures ». Ne pas prêter au texte une autorisation post-2035 qu'il n'écrit pas.

### `L11-A4` — [A]

Le décret présidentiel américain 14412 « Securing the Nation Against Advanced Cryptographic Attacks », signé le 22 juin 2026 et publié au Federal Register du 25 juin 2026 (vol. 91, n° 121, p. 38483), fait porter par l'OMB, sous 90 jours, une directive imposant aux agences fédérales la migration de tous les HVA et systèmes à impact élevé vers la PQC au 31 décembre 2030 pour l'établissement de clés et au 31 décembre 2031 pour les signatures numériques.

**Balayage (degré 1)** — Extraction texte intégrale (4 pages) du PDF officiel govinfo FR-2026-06-25/2026-12909, puis décompte de chaînes exactes effectué sur le texte extrait : « 8547 » = 0 occurrence, « Internal Report » = 0, « 2035 » = 0, « 2030 » = 2, « 2031 » = 1, « 2027 » = 1, « NIST » = 13, « FIPS » = 8. Le fait négatif est borné à ce texte, dans cette version publiée.

- **primaire** — Executive Order 14412 — Securing the Nation Against Advanced Cryptographic Attacks — signé le 22 juin 2026 ; publié le 25 juin 2026, consultée le 2026-07-21 — <https://www.govinfo.gov/content/pkg/FR-2026-06-25/pdf/2026-12909.pdf>
  > (ii) transition all HVAs and high impact systems to use PQC for key establishment by December 31, 2030; (iii) transition all HVAs and high impact systems to use PQC for digital signatures by December 31, 2031
- **primaire** — Executive Order 14412, Sec. 6 — obligation de filière — 25 juin 2026, consultée le 2026-07-21 — <https://www.govinfo.gov/content/pkg/FR-2026-06-25/pdf/2026-12909.pdf>
  > publish a proposed rule amending the Federal Acquisition Regulation (FAR) to require covered contractors to comply by December 31, 2030, with NIST's FIPS, including all applicable FIPS incorporating PQC compliant algorithms.
- **primaire** — Securing the Nation Against Advanced Cryptographic Attacks — 25 juin 2026, consultée le 2026-07-21 — <https://www.federalregister.gov/d/2026-12909>
  > Executive Order 14412 of June 22, 2026

**Réserve** — Fait négatif de degré 1, borné : le texte du décret tel que publié au Federal Register ne nomme ni NIST IR 8547 ni l'année 2035 ; il ne s'ensuit rien sur les documents d'application. Le décret n'assigne pas les échéances aux agences directement : il ordonne à l'OMB d'émettre une directive qui les imposera (voir L11-A5). Périmètre : « This memorandum does not apply to national security systems » vaut pour la note d'application ; le décret exclut expressément les National Security Systems de l'inventaire visé. Distinct des jalons du NIST : 2030 y désigne une migration exigée, non une dépréciation.

### `L11-A5` — [B]

La note OMB M-26-15 du 24 juin 2026, qui met en œuvre le décret 14412, ordonne aux agences fédérales d'aligner leur plan de migration sur NIST IR 8547 « ou un document successeur », et sa note de bas de page renvoie explicitement à l'URL du projet (csrc.nist.gov/pubs/ir/8547/ipd) : une obligation fédérale datée s'ancre ainsi sur un document encore à l'état d'Initial Public Draft.

**Balayage (degré 0)** — Extraction texte intégrale (11 pages) du PDF M-26-15 publié sur whitehouse.gov, puis décompte de chaînes exactes : « 8547 » = 3 occurrences, « 2035 » = 2, « 2030 » = 4, « 2031 » = 1. Lecture suivie de la section « D. Plan Submission » (phases 1 à 5) et de l'annexe technique portant la note 14.

- **primaire** — M-26-15, Execution of the Migration to Post-Quantum Cryptography — 24 juin 2026, consultée le 2026-07-21 — <https://www.whitehouse.gov/wp-content/uploads/2026/06/M-26-15-Execution-of-the-Migration-to-Post-Quantum-Cryptography.pdf>
  > Agencies must align their plans with NIST Internal Report (IR) 8547, Transition to Post-Quantum Cryptography Standards, or successor document.
- **primaire** — M-26-15, annexe technique, note 14 — 24 juin 2026, consultée le 2026-07-21 — <https://www.whitehouse.gov/wp-content/uploads/2026/06/M-26-15-Execution-of-the-Migration-to-Post-Quantum-Cryptography.pdf>
  > For more information, see NIST IR 8547, available at https://csrc.nist.gov/pubs/ir/8547/ipd.
- **primaire** — M-26-15, section D — Plan Submission, phases 1 à 5 — 24 juin 2026, consultée le 2026-07-21 — <https://www.whitehouse.gov/wp-content/uploads/2026/06/M-26-15-Execution-of-the-Migration-to-Post-Quantum-Cryptography.pdf>
  > Phase 5 (Full Migration – 2035): The final phase should focus on completing the migration of remaining systems with consideration based on risk assessment and the availability of commercial offerings by 2035.

**Réserve** — La note distingue deux registres : la remise du plan est prescrite (« Each agency must develop and submit a PQC Migration Plan to OMB and ONCD no later than 120 days from the date of this memorandum »), tandis que les cinq phases sont formulées au conditionnel de recommandation (« should focus on… »). Ne pas présenter la phase 5 (2035) comme une obligation datée de même force que la remise du plan. Le calendrier de phases — Phase 1 (2026-2027), Phase 2 (2027-2028), Phase 3 (2028-2030), Phase 4 (2031), Phase 5 (2035) — est d'origine OMB, pas NIST ; il ne se fusionne pas avec les jalons de L11-A2.

### `L11-A6` — [B]

FIPS 203 (ML-KEM) et FIPS 204 (ML-DSA) sont, eux, des normes finales publiées le 13 août 2024 — FIPS 203 portant en tête « Published: August 13, 2024 Effective: August 13, 2024 » — et l'écart de statut avec NIST IR 8547 est donc net : les algorithmes sont normalisés, le calendrier de retrait des algorithmes classiques ne l'est pas.

**Balayage (degré 0)** — Extraction texte des six premières pages du PDF officiel NIST.FIPS.203.pdf (section « Announcing… », clauses 11 à 13) ; lecture des fiches CSRC de FIPS 203 et FIPS 204 (historique de document à deux entrées chacune : projet 24 août 2023, version finale 13 août 2024).

- **primaire** — FIPS 203, Module-Lattice-Based Key-Encapsulation Mechanism Standard — version finale, 13 août 2024, consultée le 2026-07-21 — <https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf>
  > Published: August 13, 2024 Effective: August 13, 2024
- **primaire** — FIPS 204, Module-Lattice-Based Digital Signature Standard — version finale, 13 août 2024, consultée le 2026-07-21 — <https://csrc.nist.gov/pubs/fips/204/final>
  > 08/13/24: FIPS 204 (Final)
- **primaire** — FIPS 203 — fiche CSRC, avis d'errata — consultée le 21 juillet 2026, consultée le 2026-07-21 — <https://csrc.nist.gov/pubs/fips/203/final>
  > We've identified an issue that will be corrected in a future update/revision of this publication.

**Réserve** — Statut final ne vaut pas texte figé : les deux fiches CSRC portent un avis d'errata. Celle de FIPS 203 annonce « We've identified an issue that will be corrected in a future update/revision of this publication » ; celle de FIPS 204 porte une note de planification du 23 février 2026 signalant « several minor issues that will be corrected in a future update/revision ». La date d'entrée en vigueur n'a été constatée que dans le texte de FIPS 203 ; pour FIPS 204 seule la fiche CSRC a été ouverte. FIPS 203 porte par ailleurs une clause de qualification propre (« 13. Qualifications ») à lire avant toute formulation sur ce que la norme démontre.

### `L11-A7` — [B]

Le document « Quantum Safe Financial Forum — A call to action » d'Europol ne fixe aucune échéance calendaire propre au secteur financier : ses cinq recommandations sont non datées, et la seule échéance datée qu'il énonce est attribuée à l'administration américaine (« The US administration has set 2035 as the deadline for Federal Agencies to achieve quantum resistance »).

**Balayage (degré 1)** — Extraction texte intégrale des 10 pages du PDF Quantum-safe-financial-forum-2025.pdf hébergé par Europol, puis décompte de chaînes exactes sur le texte extrait : « 2035 » = 1 occurrence (la phrase citée), « 2030 » = 1 occurrence, uniquement à l'intérieur du titre de section « THE TIMELINE: FROM TODAY TO THE MID-2030'S », « 2033 » = 0, « deadline » = 1, « target » = 0, « 8547 » = 0.

- **primaire** — Quantum Safe Financial Forum — A call to action — métadonnées XMP : créé le 5 février 2025, modifié le 7 février 2025, consultée le 2026-07-21 — <https://www.europol.europa.eu/cms/sites/default/files/documents/Quantum-safe-financial-forum-2025.pdf>
  > The US administration has set 2035 as the deadline for Federal Agencies to achieve quantum resistance.
- **primaire** — Quantum Safe Financial Forum — A call to action, recommandation 3 — février 2025, consultée le 2026-07-21 — <https://www.europol.europa.eu/cms/sites/default/files/documents/Quantum-safe-financial-forum-2025.pdf>
  > There is no need for additional legislation to be made; a voluntary framework established between regulators and the private sector would be sufficient to set guidelines for quantum-safe cryptography and promoting standardisation across institutions.

**Réserve** — Fait négatif de degré 1 borné à ce fichier : l'extraction texte ne voit pas ce qui serait rendu en image (infographies). La date de publication n'a pas pu être établie sur une page Europol (rendu JavaScript) ; les éléments dont je dispose sont internes au fichier — métadonnées XMP de création au 5 février 2025 et modification au 7 février 2025, et dates de consultation « 31/01/2025 » portées par ses notes de bas de page. La recommandation n° 3 du forum est explicitement anti-normative : elle écarte le besoin de législation supplémentaire.

### `L11-A8` — [B]

Le rapport conjoint « Prioritising Post-Quantum Cryptography Migration Activities in Financial Services » (Europol, Office des publications de l'Union européenne, Luxembourg, 2026) substitue à toute échéance calendaire une priorisation par le risque : le texte extrait de ses 26 pages ne contient aucune occurrence de « 2030 », « 2035 » ni « 8547 », et son avertissement précise qu'il n'est pas obligatoire et ne doit pas servir de guide de conformité réglementaire.

**Balayage (degré 1)** — Extraction texte intégrale des 26 pages du PDF Post-quantum-cryptography-report.pdf hébergé par Europol, puis décompte de chaînes exactes sur le texte extrait : « 2030 » = 0, « 2035 » = 0, « 8547 » = 0, « 2026 » = 3 (mention d'édition, citation recommandée, et une phrase sur la disponibilité de X25519MLKEM768), « FS-ISAC » = 2.

- **primaire** — Prioritising Post-Quantum Cryptography Migration Activities in Financial Services — 2026 (ISBN 978-92-9414-091-3, DOI 10.2813/9782176 ; métadonnées XMP de…, consultée le 2026-07-21 — <https://www.europol.europa.eu/cms/sites/default/files/documents/Post-quantum-cryptography-report.pdf>
  > Cite this publication: Europol, Prioritising post-quantum cryptography migration activities in financial services, Publications Office of the European Union, Luxembourg, 2026.
- **primaire** — Prioritising Post-Quantum Cryptography Migration Activities in Financial Services — DISCLAIMER — 2026, consultée le 2026-07-21 — <https://www.europol.europa.eu/cms/sites/default/files/documents/Post-quantum-cryptography-report.pdf>
  > This document is not mandatory for implementation or endorsement by any participating organisation, nor does it impose or infer any obligations on its contributors, endorsers, or their institutions
- **primaire** — Prioritising PQC Migration Activities in Financial Services — Executive Summary — 2026, consultée le 2026-07-21 — <https://www.europol.europa.eu/cms/sites/default/files/documents/Post-quantum-cryptography-report.pdf>
  > This document provides actionable guidelines to incorporate quantum safety into existing risk management frameworks by assessing the 'Migration Priority' based on the 'Quantum Risk' and 'Migration Time' of business use cases

**Réserve** — Fait négatif de degré 1 borné à ce fichier ; l'extraction ne voit pas le texte incrusté dans les figures. Le rapport est un document de praticiens, non un acte d'autorité : il est signé de contributeurs nommés d'établissements financiers (dont FS-ISAC, Banco Santander, BMO, TD Bank, Citi, National Bank of Canada, University of Waterloo) et porte onze organisations en endossement. Le lien avec le QSFF et avec le groupe de travail canadien CFDIR est rapporté par les communiqués de presse, non constaté dans le PDF (le sigle « CFDIR » y compte zéro occurrence).

### `L11-A9` — [B]

La seule étude de coût de migration commanditée par une autorité publique que cette passe a ouverte est le rapport de juillet 2024 de l'Office of Management and Budget au Congrès, exigé par le Quantum Computing Cybersecurity Preparedness Act (Public Law 117-260) : l'Office of the National Cyber Director y projette environ 7,1 milliards de dollars de 2024 pour migrer les systèmes fédéraux civils prioritaires entre 2025 et 2035, systèmes de sécurité nationale exclus.

**Balayage (degré 0)** — Extraction texte intégrale des 16 pages du PDF REF_PQC-Report_FINAL_Send.pdf, puis relevé des occurrences de « 7.1 billion » et lecture de la section 2 « Current estimate of the amount of funding needed by agencies to secure information technology ».

- **primaire** — Report on Post-Quantum Cryptography, as required by the Quantum Computing Cybersecurity Preparedness Act — juillet 2024, consultée le 2026-07-21 — <https://bidenwhitehouse.archives.gov/wp-content/uploads/2024/07/REF_PQC-Report_FINAL_Send.pdf>
  > ONCD projects that that the total government-wide cost required to perform a migration of prioritized information systems to PQC between 2025 and 2035 will be approximately $7.1 billion in 2024 dollars.
- **primaire** — Report on Post-Quantum Cryptography — page de titre et réserve d'incertitude — juillet 2024, consultée le 2026-07-21 — <https://bidenwhitehouse.archives.gov/wp-content/uploads/2024/07/REF_PQC-Report_FINAL_Send.pdf>
  > as required by the Quantum Computing Cybersecurity Preparedness Act, Public Law No: 117-260

**Réserve** — Métrique auto-déclarée : chiffre produit par l'ONCD à partir des estimations remises par les agences elles-mêmes — à attribuer à l'ONCD à chaque occurrence, jamais présenté comme un coût constaté. Le rapport porte lui-même la réserve d'incertitude (« This initial projection reflects a high, but expected, level of uncertainty ») et impose une mise à jour annuelle. Périmètre exclu : DoD, ODNI et National Manager for NSS produisent des estimations séparées. Le document n'est plus servi par whitehouse.gov : il a été consulté sur bidenwhitehouse.archives.gov. Ne pas écrire « la seule étude publiée » : aucun balayage exhaustif de la littérature n'a été mené — voir la note de couverture.

