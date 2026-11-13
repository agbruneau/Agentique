"""Correctifs de l'audit du 11 novembre 2026, lot cadre-d (annexes A à H, glossaire, références, chapitre 15).

Appliqué après les modules 05 à 07 : chaque passage d'origine est cherché dans le corps déjà corrigé.
"""

CORRECTIONS = [('Le cadre gradue donc les contrôles selon le niveau d’autonomie et le palier d’outil (section 8.4).',
  'Le cadre gradue donc les contrôles selon la classe de risque, le niveau d’autonomie et le palier d’outil (sections 8.4 et '
  '12.1).',
  'C4-18'),
 ('Contrôles gradués par niveau et par palier (section 8.4)',
  'Contrôles gradués par classe, par niveau et par palier (section 8.4)',
  'C4-18'),
 ('Classer chaque agent inventorié (faible, modéré, élevé) et fixer',
  'Classer chaque agent inventorié (classe faible, modérée ou élevée) et fixer',
  'COQ-Cad-061/231'),
 ('avec les délais de détection et de confinement</td>', 'avec les délais de détection et de contention</td>', 'COQ-Cad-232'),
 ('Elle concrétise la sous-catégorie MANAGE\xa02.4',
  'La cible de révocation concrétise la sous-catégorie MANAGE\xa02.4',
  'COQ-Cad-233'),
 ('jetons contraints à l’émetteur et de courte durée', 'jetons liés à l’expéditeur et de courte durée', 'R06-21'),
 ('la liaison à l’émetteur et la durée courte', 'la liaison à l’expéditeur et la durée courte', 'R06-21'),
 ('<tr><td><strong>Jeton contraint à l’émetteur</strong></td><td><em>sender-constrained token</em></td><td>Jeton d’accès lié à '
  'une clé ou à un certificat que seul son détenteur légitime peut présenter\xa0: mTLS (RFC 8705, revendication <code>cnf</code> '
  '«\xa0<code>x5t#S256</code>\xa0») dans le maillage de services, ou DPoP (RFC 9449, preuve JWT à chaque requête) hors du '
  'maillage. La RFC 9700 recommande cette contrainte<strong><sup>[175]</sup></strong>; le cadre l’exige pour tout jeton qui '
  'donne accès à un outil P2 ou P3 ou que détient un agent de classe élevée. Voir la section 9.3.</td></tr>',
  '',
  'R06-21'),
 ('<tr><td><strong>Journal d’audit</strong>',
  '<tr><td><strong>Jeton lié à l’expéditeur</strong></td><td><em>sender-constrained token</em></td><td>Jeton d’accès lié à une '
  'clé ou à un certificat que seul son détenteur légitime peut présenter\xa0: mTLS (RFC 8705, revendication <code>cnf</code> '
  '«\xa0<code>x5t#S256</code>\xa0») dans le maillage de services, ou DPoP (RFC 9449, preuve JWT à chaque requête) hors du '
  'maillage. La RFC 9700 recommande cette contrainte<strong><sup>[175]</sup></strong>; le cadre l’exige pour tout jeton qui '
  'donne accès à un outil P2 ou P3 ou que détient un agent de classe élevée. Voir la section '
  '9.3.</td></tr><tr><td><strong>Journal d’audit</strong>',
  'R06-21'),
 ('il en compte dix au 22\xa0octobre 2026<strong><sup>[4, 130, 193]</sup></strong>',
  'il en compte dix au 22\xa0octobre 2026<strong><sup>[4, 38, 130, 193]</sup></strong>',
  'C5-14'),
 ('projets diplômés de la CNCF. Un SPIFFE ID prend',
  'projets de la CNCF au stade «\xa0Graduated\xa0». Un SPIFFE ID prend',
  'COQ-Cad-236'),
 ('demande de tirage nº 3696, fusionnée', 'demande de tirage no\xa03696, fusionnée', 'COQ-Cad-242/243'),
 ('<tr><td>1.0</td><td>27\xa0oct.\xa02026</td>', '<tr><td>1.0</td><td>28\xa0oct.\xa02026</td>', 'R06-28'),
 ('      "definition": "1.4.0",\n'
  '      "definition_sha256": "sha256:e8c1ccd755dd196d40fb358447998a964dd643fa03614e9e8fbbfa66abf643b6",\n',
  '      "definition_sha256": "sha256:e8c1ccd755dd196d40fb358447998a964dd643fa03614e9e8fbbfa66abf643b6",\n'
  '      "definition_version": "1.4.0",\n',
  'R06-34'),
 ('"outil": "erp_enregistrer_decision", "definition": "1.4.1",',
  '"outil": "erp_enregistrer_decision", "definition_version": "1.4.1",',
  'R06-34'),
 ('; 49 sources ont été ajoutées au registre pendant les corrections. L’annexe G compte 473 entrées, dont 25 doublons signalés '
  '(448 sources distinctes); l’écart de 45 entrées entre l’audit final et l’annexe G n’est pas ventilé dans la présente version '
  '(annexe F.1).',
  '. À l’issue de l’audit, l’annexe G comptait 473 entrées, dont 25 doublons signalés (448 sources distinctes)\xa0: les 428 '
  'références auditées et les références [429] à [473], ajoutées lors de la consolidation et vérifiées le 27 octobre 2026; la '
  'version 1.1 y ajoute la référence [496] (annexe F.1).',
  'R01-02'),
 ('; 49 sources ont été ajoutées pendant les corrections, et l’annexe G compte 473 entrées, dont 25 doublons signalés (448 '
  'sources distinctes; annexe F.1).</li>',
  '; l’annexe G comptait alors 473 entrées, soit ces 428 références et les 45 références [429] à [473] ajoutées lors de la '
  'consolidation, dont 25 doublons signalés (448 sources distinctes; annexe F.1); la version 1.1 y ajoute la référence '
  '[496].</li>',
  'R01-02'),
 ('Les corrections retenues ont été intégrées au texte; 49 sources ont été ajoutées au registre, et le texte des exigences, les '
  'échelles et les renvois ont été harmonisés. Après l’intégration de ces corrections, l’annexe G compte 473 entrées, toutes '
  'citées dans le corps du cadre,',
  'Les corrections retenues ont été intégrées au texte, et le texte des exigences, les échelles et les renvois ont été '
  'harmonisés. Après l’intégration de ces corrections, l’annexe G comptait 473 entrées, toutes citées dans le corps du cadre,',
  'R01-02'),
 ('l’écart de 45 entrées entre l’audit final et l’annexe G n’est pas ventilé, et le relevé lien par lien des affirmations et des '
  'sources n’est pas publié.',
  'l’écart de 45 entrées entre l’audit final et l’annexe G correspond aux références [429] à [473], ajoutées lors de la '
  'consolidation et vérifiées le 27 octobre 2026 (historique des versions), et le relevé lien par lien des affirmations et des '
  'sources n’est pas publié. La version 1.1 ajoute la référence [496] (RFC 7515, section 6.6), ce qui porte l’annexe G à 474 '
  'entrées et à 449 sources distinctes.',
  'R01-02'),
 ('<p>Les décomptes ci-dessous portent sur les 121 références et sur les 427 liens affirmation-source de la recherche '
  'documentaire.</p>',
  '<p>Les quatre premiers décomptes portent sur les 121 références et sur les 427 liens affirmation-source de la recherche '
  'documentaire; les deux derniers (705 et 448) portent sur la version finale.</p>',
  'R06-30'),
 ('; 49 ont été ajoutées lors de l’audit final. Ce recensement est plus large que l’annexe G</p>',
  '; 49 ont été ajoutées à ce recensement lors de l’audit final. Ce recensement n’est pas le registre de l’annexe G\xa0: il '
  'dépasse de 232 sources les 473 entrées de l’annexe G à l’issue de l’audit (de 231 les 474 entrées de la version 1.1), et le '
  'présent document ne ventile pas cet écart</p>',
  'C5-02'),
 ('<p>sources distinctes à l’annexe G (473 entrées, dont 25 doublons), dont 410 de catégorie A,',
  '<p>sources distinctes à l’annexe G à l’issue de l’audit (473 entrées, dont 25 doublons; la version 1.1 y ajoute [496], de '
  'catégorie A, soit 449 sources distinctes et 474 entrées), dont 410 de catégorie A,',
  'C5-02'),
 ('La carte peut être signée en JWS (RFC 7515) après canonisation JCS',
  'La carte peut être signée en JWS (RFC 7515)<strong><sup>[496]</sup></strong> après canonisation JCS',
  'C5-12'),
 ('<a href="https://arxiv.org/abs/2404.14219"><code>https://arxiv.org/abs/2404.14219</code></a></li>\n</ul>',
  '<a href="https://arxiv.org/abs/2404.14219"><code>https://arxiv.org/abs/2404.14219</code></a></li>\n'
  '<li><strong><code>[496]</code></strong> Jones, M., Bradley, J. et Sakimura, N. (2015, mai). <em>RFC 7515 — JSON Web Signature '
  '(JWS)</em>. RFC Editor. <a '
  'href="https://www.rfc-editor.org/rfc/rfc7515.html"><code>https://www.rfc-editor.org/rfc/rfc7515.html</code></a></li>\n'
  '</ul>',
  'C5-12'),
 ('<p>Liste des sources citées, numérotées dans l’ordre de leur première citation. Elles relèvent',
  '<p>Liste des sources citées, numérotées approximativement dans l’ordre de leur première citation (les références ajoutées à '
  'la consolidation, [429] à [473], et à la version 1.1, [496], suivent les autres). Elles relèvent',
  'R07-17'),
 ('La liste compte 473 entrées, dont 25 doublons signalés («\xa0Même source que [n]\xa0»), soit 448 sources distinctes; les '
  'numéros ne sont jamais réattribués.',
  'La liste compte 474 entrées ([1] à [473] et [496]), dont 25 doublons signalés («\xa0Même source que [n]\xa0»), soit 449 '
  'sources distinctes; les numéros ne sont jamais réattribués.',
  'R07-17'),
 ('Gabarit des entrées\xa0: Auteur (AAAA, j mois, ou l’année seule quand la source ne donne pas le jour).',
  'Gabarit des entrées\xa0: Auteur (AAAA, j mois; AAAA, mois quand la source ne donne pas le jour; l’année seule quand elle ne '
  'donne pas le mois; AAAA-AAAA pour un dépôt de versions successives; «\xa0mis à jour le…\xa0» pour une page révisée). Les '
  'auteurs d’un RFC ou d’un brouillon de l’IETF sont nommés; «\xa0IETF\xa0» seul désigne une page ou un groupe de travail.',
  'R07-18'),
 ('<h2>D Registre des exigences</h2>',
  '<div data-typst="pagebreak(weak: true)"></div>\n<h2>D Registre des exigences</h2>',
  'V3-36'),
 ('<h2>E Glossaire</h2>', '<div data-typst="pagebreak(weak: true)"></div>\n<h2>E Glossaire</h2>', 'V3-36'),
 ('<h2>F Validation des sources et des ébauches</h2>',
  '<div data-typst="pagebreak(weak: true)"></div>\n<h2>F Validation des sources et des ébauches</h2>',
  'V3-36'),
 ('<h2>G Références</h2>', '<div data-typst="pagebreak(weak: true)"></div>\n<h2>G Références</h2>', 'V3-36'),
 ('(2025). Introducing the MCP Registry.', '(2025, 8 septembre). Introducing the MCP Registry.', 'R07-18'),
 ('(2022). SPIFFE and SPIRE Projects Graduate', '(2022, 20 septembre). SPIFFE and SPIRE Projects Graduate', 'R07-18'),
 ('(2025). Agentic AI Threat Modeling Framework: MAESTRO.',
  '(2025, 6 février). Agentic AI Threat Modeling Framework: MAESTRO.',
  'R07-18'),
 ('(2025). The lethal trifecta for AI agents', '(2025, 16 juin). The lethal trifecta for AI agents', 'R07-18'),
 ('(2023). The Dual LLM pattern', '(2023, 25 avril). The Dual LLM pattern', 'R07-18'),
 ('<code>[69]</code></strong> IETF (2020, janvier).',
  '<code>[69]</code></strong> Jones, M., Nadalin, A., Campbell, B., Bradley, J. et Mortimore, C. (2020, janvier).',
  'R07-20'),
 ('<code>[70]</code></strong> IETF (2020, janvier).',
  '<code>[70]</code></strong> Jones, M., Nadalin, A., Campbell, B., Bradley, J. et Mortimore, C. (2020, janvier).',
  'R07-20'),
 ('<code>[118]</code></strong> IETF (2020, janvier).',
  '<code>[118]</code></strong> Jones, M., Nadalin, A., Campbell, B., Bradley, J. et Mortimore, C. (2020, janvier).',
  'R07-20'),
 ('<code>[71]</code></strong> IETF (2020).',
  '<code>[71]</code></strong> Campbell, B., Bradley, J. et Tschofenig, H. (2020, février).',
  'R07-20'),
 ('<code>[72]</code></strong> IETF (2021, octobre).', '<code>[72]</code></strong> Bertocci, V. (2021, octobre).', 'R07-20'),
 ('<code>[175]</code></strong> IETF (2025, janvier).',
  '<code>[175]</code></strong> Lodderstedt, T., Bradley, J., Labunets, A. et Fett, D. (2025, janvier).',
  'R07-20'),
 ('<code>[179]</code></strong> IETF (2026, 30 juillet).',
  '<code>[179]</code></strong> Tulshibagwale, A., Fletcher, G. et Kasselman, P. (2026, 30 juillet).',
  'R07-20'),
 ('<code>[216]</code></strong> IETF (2026, 6 juillet).',
  '<code>[216]</code></strong> Parecki, A. et Smith, E. (2026, 6 juillet).',
  'R07-20'),
 ('(texte annoté des modifications). Future of Life Institute. <a href="https://artificialintelligenceact.eu/article/113">',
  '(texte annoté des modifications). Future of Life Institute. Site non officiel (agrégateur, catégorie C au sens du tableau '
  '66), source secondaire sans valeur d’appui; le texte de référence est le règlement [61]. <a '
  'href="https://artificialintelligenceact.eu/article/113">',
  'R07-11'),
 ('ISO/IEC (2023). ISO/IEC 42001:2023 — Technologies',
  'ISO/IEC (2023, 18 décembre). ISO/IEC 42001:2023 — Technologies',
  'R07-21'),
 ('ISO/IEC 42006:2025 — Exigences pour les organismes',
  'ISO/IEC 42006:2025 — Technologies de l’information — Intelligence artificielle — Exigences pour les organismes',
  'R07-21'),
 ('Gowling WLG. <a '
  'href="https://gowlingwlg.com/fr/insights-resources/articles/2025/specter-aviation-v-laprade-qc-first-judicial-sanction-ai">',
  'Gowling WLG. Décision commentée\xa0: <em>Specter Aviation Limited c. Laprade</em>, 2025 QCCS 3521 (Cour supérieure du Québec, '
  '1<sup>er</sup> octobre 2025), référence neutre relevée à la note 1 de l’article; la décision n’a pas été rouverte. <a '
  'href="https://gowlingwlg.com/fr/insights-resources/articles/2025/specter-aviation-v-laprade-qc-first-judicial-sanction-ai">',
  'R07-14'),
 ('<td>Appui de toute exigence et de tout fait.</td>',
  '<td>Appui de tout fait. Une exigence ne s’appuie que sur une source apte à la fonder (norme, loi, spécification, '
  'documentation officielle)\xa0: un communiqué de firme d’analystes ou un article non révisé par les pairs établit ce que ses '
  'auteurs affirment, non une exigence à lui seul.</td>',
  'R06-31'),
 ('<td>Source secondaire reconnue\xa0: grande presse spécialisée, cabinets juridiques, experts reconnus.</td>',
  '<td>Source secondaire reconnue\xa0: grande presse spécialisée, cabinets juridiques, experts reconnus, études d’éditeurs, '
  'd’investisseurs ou de cabinets.</td>',
  'R07-06'),
 ('</tbody></table>\n<h3>F.2 Bilan chiffré</h3>',
  '</tbody></table>\n'
  '<p>La catégorie d’une entrée tient à la nature de la source, non à la firme qui la publie\xa0: un communiqué, un billet ou '
  'une étude d’éditeur vaut comme source primaire de ce que son éditeur affirme de lui-même ou de ses produits (catégorie A), et '
  'comme source secondaire pour toute affirmation sur le marché ou sur d’autres produits (catégorie B); un blogue de '
  'positionnement ou un agrégateur reste en catégorie C. Cette précision est postérieure au classement des entrées de l’annexe '
  'G, qui n’a pas été repris entrée par entrée.</p>\n'
  '<h3>F.2 Bilan chiffré</h3>',
  'R07-06'),
 ('et le cadre ajoute des extensions de gouvernance (contexte de trace, mandant, classification, compteur de sauts).',
  'et le cadre exige des extensions documentées (contexte de trace, contexte d’authentification, classification, clé de '
  'partition) et ajoute les siennes (origine, compteur et plafond de sauts, centre de coûts).',
  'R06-25'),
 ('<tr><td><strong>Bus d’événements</strong></td>',
  '<tr><td><strong>Bureau du surintendant des institutions financières</strong> (BSIF)</td><td><em>Office of the Superintendent '
  'of Financial Institutions (OSFI)</em></td><td>Organisme fédéral dont la ligne directrice E-23 vise les institutions '
  'financières fédérales\xa0: elle inclut les méthodes d’IA dans sa définition de modèle et exige un inventaire d’entreprise, '
  'que le cadre étend à chaque agent et à chaque modèle utilisé (EXIG-CON-12). Voir la section '
  '12.3.</td></tr><tr><td><strong>Bus d’événements</strong></td>',
  'R06-24'),
 ('<tr><td><strong>Coupe-circuit</strong></td>',
  '<tr><td><strong>Contrôle calculé</strong></td><td><em>computed control (terme du cadre)</em></td><td>Contrôle que la '
  'passerelle d’agents détermine à chaque appel d’outil\xa0: l’union des contrôles de la cellule classe × palier, du niveau '
  'd’autonomie et de la classe les plus contraignants de la chaîne de délégation, des déclencheurs d’approbation et des points '
  'non dérogeables (EXIG-AUT-10). Voir la section 8.4.</td></tr><tr><td><strong>Coupe-circuit</strong></td>',
  'R06-24'),
 ('<tr><td><strong>FinOps</strong></td>',
  '<tr><td><strong>Existant inventorié</strong></td><td><em>inventoried legacy agent (terme du cadre)</em></td><td>Statut d’un '
  'agent en exploitation à l’adoption du cadre, ou découvert ensuite hors registre\xa0: il reçoit une fiche minimale (champs de '
  'l’étape Proposition) et un parrain nommé dans les cinq jours ouvrables qui suivent sa découverte, faute de quoi il est '
  'désactivé (section 11.6, EXIG-GOV-16).</td></tr><tr><td><strong>Fiche d’agent</strong></td><td><em>agent record (terme du '
  'cadre)</em></td><td>Entrée du registre d’entreprise qui décrit un agent\xa0: elle s’ouvre à l’étape Proposition, se complète '
  'au fil du cycle de vie et doit être complète avant tout jeton d’exécution en production (EXIG-GOV-07). Voir la section 11.4 '
  'et l’annexe B.</td></tr><tr><td><strong>FinOps</strong></td>',
  'R06-24'),
 ('<tr><td><strong>Maillage</strong>',
  '<tr><td><strong>Loi sur la protection des renseignements personnels et les documents électroniques</strong> '
  '(LPRPDE)</td><td><em>Personal Information Protection and Electronic Documents Act (PIPEDA)</em></td><td>Loi fédérale en '
  'vigueur. En cas d’atteinte présentant un risque réel de préjudice grave, elle impose la déclaration au Commissariat et l’avis '
  'aux personnes «\xa0le plus tôt possible\xa0» (par. 10.1(2) et (6)), et la consignation de toutes les atteintes pendant 24 '
  'mois. Voir la section 12.3 (tableau 48).</td></tr><tr><td><strong>Maillage</strong>',
  'R06-24'),
 ('<tr><td><strong>MCP</strong> (Model Context Protocol)</td>',
  '<tr><td><strong>Matrice RACI</strong></td><td><em>RACI matrix</em></td><td>Tableau qui attribue chaque activité du cycle de '
  'vie d’un agent à un rôle qui réalise (R), à un seul rôle qui approuve et répond (A), aux rôles consultés (C) et aux rôles '
  'informés (I). Voir la section 11.2 (tableau 44).</td></tr><tr><td><strong>MCP</strong> (Model Context Protocol)</td>',
  'R06-24'),
 ('<tr><td><strong>Modèle</strong></td><td><em>model; large language model (LLM)</em>',
  '<tr><td><strong>Mesure transitoire de cohorte</strong></td><td><em>cohort transitional measure (terme du '
  'cadre)</em></td><td>Décision unique du comité qui place une liste d’agents existants sous un régime transitoire dont '
  'l’échéance est liée à un jalon de la feuille de route\xa0: elle n’admet aucun point de l’EXIG-GOV-17 ni aucune obligation '
  'légale et ne couvre jamais un dépassement du plafond de la classe (section 11.6, '
  'EXIG-GOV-16).</td></tr><tr><td><strong>Modèle</strong></td><td><em>model; large language model (LLM)</em>',
  'R06-24'),
 ('<tr><td><strong>Règlement européen sur l’IA</strong> (RIA)</td>',
  '<tr><td><strong>Règle d’or</strong></td><td><em>golden rule (terme du cadre)</em></td><td>Règle propre au cadre\xa0: un agent '
  'dont le rayon d’impact, la réversibilité et le délai de détection atteignent les seuils d’étalonnage approuvés par le comité '
  '(rayon élevé, réversibilité faible, détection lente) ne peut être autorisé au-delà de N2, quels que soient ses résultats aux '
  'bancs d’essai (EXIG-AUT-07; point non dérogeable, EXIG-GOV-17). Voir la section 8.2.</td></tr><tr><td><strong>Règlement '
  'européen sur l’IA</strong> (RIA)</td>',
  'R06-24'),
 ('à une entrée du journal d’audit</td><td>100\xa0%</td>',
  'à une entrée du journal d’audit</td><td>100\xa0% dès l’ouverture des outils P2 et P3 à la passerelle d’agents (phase '
  'Plateforme)\xa0: aucun effet sans journal d’audit (EXIG-OBS-11, non dérogeable)</td>',
  'R05-57'),
 ('atteint ses seuils (section 10.4)</td><td>100\xa0%</td>',
  'atteint ses seuils (section 10.4)</td><td>100\xa0% des nouveaux agents dès la mise en service de la chaîne CI/CD (phase '
  'Industrialisation; d’ici là, forme minimale déclarée à la fiche, annexe A); 100\xa0% des agents existants au jalon 3 (mesure '
  'transitoire de cohorte d’ici là)</td>',
  'R05-57'),
 ('dont l’EFVP couvre la version en production</td><td>100\xa0%</td>',
  'dont l’EFVP couvre la version en production</td><td>100\xa0% des nouveaux agents dès leur homologation (EXIG-CON-04); 100\xa0'
  '% des agents existants au jalon 1, les flux visés restant suspendus d’ici là (tableau 58)</td>',
  'R05-57'),
 ('<li>chaque indicateur a un responsable de mesure nommé parmi les rôles de la section 11.1.</li>',
  '<li>chaque indicateur a un responsable de mesure, nommé par le comité parmi les rôles de la section 11.1; le tableau 61 '
  'propose le rôle qui opère la source de la donnée.</li>',
  'R05-57'),
 ('où chaque indicateur d’entreprise tient sa cible chiffrée',
  'où chaque indicateur du tableau 61, mesuré pour l’entreprise, tient sa cible chiffrée',
  'R05-57'),
 ('au plus tard le 28\xa0juillet 2027 (EXIG-MCP-22).</td><td>Traces de bout en bout, du canal au modèle; catalogue initial '
  'publié; plan de migration MCP</td>',
  'au plus tard le 28\xa0juillet 2027 (EXIG-MCP-22); ouvrir, sur un banc d’essai de l’entreprise, les essais reproductibles des '
  'candidats aux blocs de la phase Plateforme (EXIG-APP-03, EXIG-APP-04, EXIG-APP-06).</td><td>Traces de bout en bout, du canal '
  'au modèle; catalogue initial publié; plan de migration MCP; banc d’essai des candidats ouvert</td>',
  'R05-58'),
 ('Choisir les blocs de solution de la phase Plateforme (passerelle d’agents, moteur d’exécution durable, registre) avec la '
  'grille de la section 13.4;',
  'Choisir les blocs de solution de la phase Plateforme (passerelle d’agents, moteur d’exécution durable, registre d’entreprise, '
  'qui prolonge le registre initial des semaines 3 et 4) avec la grille de la section 13.4, appliquée aux essais du banc d’essai '
  'ouvert aux semaines 7 et 8; les preuves qui supposent un agent pilote (export FOCUS d’un mois, essai de restitution) sont '
  'cotées provisoirement sur la démonstration du fournisseur et confirmées au premier pilote de la phase Plateforme;',
  'R05-58'),
 ('Décision de plateforme; rapport d’exercice du coupe-circuit',
  'Décision de plateforme, avec ses notes provisoires; rapport d’exercice du coupe-circuit',
  'R05-58'),
 ('la note d’un critère que l’entreprise n’a pas vérifié est plafonnée à 1.',
  'la note d’un critère que l’entreprise n’a pas vérifié est plafonnée à 1. La preuve d’un autre critère qui suppose un agent '
  'pilote (coûts, réversibilité) peut être cotée provisoirement à 2, sur la démonstration du fournisseur, et se confirme au '
  'premier pilote.',
  'R05-58'),
 ('Elle reprend, sous forme vérifiable, les exigences qui conditionnent la mise en production; chaque point renvoie aux '
  'exigences qui le fondent.',
  'Elle reprend, sous forme vérifiable, l’ensemble des 287 exigences du registre (annexe D), regroupées en points; chaque point '
  'renvoie aux exigences qui le fondent, et celles qui conditionnent la mise en production y figurent toutes.',
  'R06-07'),
 ('<code>EXIG-AUT-08, EXIG-AUT-10, EXIG-AUT-11, EXIG-AUT-24</code>',
  '<code>EXIG-AUT-08, EXIG-AUT-10, EXIG-AUT-11</code>',
  'R06-07'),
 ('Légende de l’applicabilité\xa0: Tous s’applique à tout agent; Si … s’applique seulement dans le cas indiqué.',
  'Légende de l’applicabilité\xa0: chaque point des sections A.2 à A.8 occupe une ligne de tableau. La première colonne donne '
  'l’applicabilité (Tous s’applique à tout agent; Si … s’applique seulement dans le cas indiqué) et, sur une seconde ligne, la '
  'marque «\xa0non dérogeable\xa0» lorsqu’elle s’applique; la dernière colonne reçoit la réponse et le lien vers la preuve (voir '
  '«\xa0Réponses admises\xa0»).',
  'V3-32')]

JOURNAL = [('§ 15.4, facteur « Une gouvernance proportionnée »; tableau 62 (ligne « Gouvernance uniforme »)',
  'La gradation des contrôles nomme la classe de risque avec le niveau d’autonomie et le palier d’outil (sections 8.4 et 12.1).',
  ['C4-18']),
 ('Annexe A.6 (Profil OAuth); annexe E (entrée « Jeton lié à l’expéditeur », reclassée à sa place alphabétique); tableau 68 '
  '(ligne 5)',
  '« Contraint à l’émetteur » remplacé par « lié à l’expéditeur » (sender-constrained), comme dans l’EXIG-IAM-14; « émetteur » '
  'reste réservé à l’issuer du jeton.',
  ['R06-21']),
 ('Annexe E (AAIF)',
  'Appel de la référence [38], communiqué du 22 octobre 2026 qui fonde le décompte de dix projets.',
  ['C5-14']),
 ('Historique des versions (version 1.0)',
  'La version 1.0 est datée du 28 octobre 2026, jour de l’audit final dont elle intègre les corrections; l’état des sources '
  'reste celui du 27 octobre.',
  ['R06-28']),
 ('§ 10.3 (extrait d’enregistrement); annexe C.8',
  'Champ « definition » renommé « definition_version » (il porte une version, l’empreinte étant dans « definition_sha256 »); '
  'clés de C.8 remises dans l’ordre RFC 8785 et empreinte de l’enregistrement recalculée.',
  ['R06-34']),
 ('Méthode et avertissements; § 1.7; annexe F.1 et F.2',
  'Arithmétique des décomptes rétablie : 428 références auditées + 45 références ([429] à [473], ajoutées à la consolidation) = '
  '473 entrées à l’annexe G; le « 49 » ne subsiste que dans le recensement de F.2, désigné comme tel; l’écart de 705 sources est '
  'chiffré (232) et déclaré non ventilé; en-tête de F.2 précisant la population de chaque décompte.',
  ['R01-02', 'C5-02', 'R06-30']),
 ('§ 6.6 (signature de la carte d’agent); annexe G, [496]',
  'Entrée [496] ajoutée pour la RFC 7515 (JWS), que citaient le tableau 64 et la section 6.6 sans référence; appel de [496] à la '
  'section 6.6.',
  ['C5-12']),
 ('Annexes D à G (mise en page)',
  'Saut de page avant les annexes D, E, F et G, pour que chacune s’ouvre en haut de page sous son propre en-tête courant.',
  ['V3-36']),
 ('Annexe G, introduction',
  '« Numérotées approximativement dans l’ordre de leur première citation » (la numérotation n’est pas réattribuée); gabarit des '
  'dates complété des formes en usage (AAAA, mois; AAAA-AAAA; mis à jour le); auteurs d’un RFC ou d’un brouillon nommés.',
  ['R07-17', 'R07-18', 'R07-20']),
 ('Annexe G, [25], [321], [351], [354], [358]',
  'Jour de publication ajouté (relevé dans l’adresse de la source, qui le porte).',
  ['R07-18']),
 ('Annexe G, [69], [70], [71], [72], [118], [175], [179], [216]',
  'Auteurs nommés (« IETF » en auteur remplacé), d’après les fiches de rfc-editor.org et de datatracker.ietf.org; mois de '
  'publication de la RFC 8707 (février 2020) ajouté à [71].',
  ['R07-20', 'R07-18']),
 ('Annexe G, [315]',
  'Signalement de la catégorie C (site non officiel, sans valeur d’appui) ajouté, comme aux autres entrées de l’agrégateur.',
  ['R07-11']),
 ('Annexe G, [395], [451]',
  'Même date pour la norme ISO/IEC 42001 en [395] et en [450]; préfixe du titre de l’ISO/IEC 42006 ajouté en [451] (titre de la '
  'fiche de Standards Norway).',
  ['R07-21']),
 ('Annexe G, [458]',
  'Référence neutre de la décision commentée (2025 QCCS 3521, 1er octobre 2025) ajoutée, relevée à la note 1 de l’article; la '
  'décision n’a pas été rouverte à la source.',
  ['R07-14']),
 ('Annexe F.1, tableau 66',
  'Catégorie A : une exigence ne s’appuie que sur une source apte à la fonder (norme, loi, spécification, documentation '
  'officielle), non sur un communiqué d’analyste ou un article non révisé; catégorie B : études d’éditeurs, d’investisseurs ou '
  'de cabinets, que le registre appliquait déjà; critère unique énoncé sous le tableau (nature de la source, non firme). Le '
  'classement entrée par entrée n’est pas repris.',
  ['R06-31', 'R07-06']),
 ('Annexe E (CloudEvents)',
  'Les extensions documentées (Distributed Tracing, Auth Context, Data Classification, Partitioning) sont distinguées de celles '
  'qui sont propres au cadre (xagentorigin, xagenthopcount, xagentmaxhops, xcostcenter), comme en C.4.',
  ['R06-25']),
 ('Annexe E (glossaire)',
  'Huit entrées ajoutées à leur place alphabétique : Bureau du surintendant des institutions financières (BSIF), Contrôle '
  'calculé, Existant inventorié, Fiche d’agent, Loi sur la protection des renseignements personnels et les documents '
  'électroniques (LPRPDE), Matrice RACI, Mesure transitoire de cohorte et Règle d’or, d’après le corps du cadre.',
  ['R06-24']),
 ('§ 15.3, tableau 61 et règles de mesure; tableau 58 (jalon 4)',
  'Cibles de 100 % échelonnées (traçabilité dès l’ouverture des outils P2 et P3; évaluation continue : nouveaux agents dès la '
  'mise en service de la chaîne CI/CD, existants au jalon 3; EFVP : nouveaux agents dès l’homologation, existants au jalon 1); '
  'colonne « Responsable de mesure (proposé) » ajoutée; « indicateur d’entreprise » défini comme un indicateur du tableau 61 '
  'mesuré pour l’entreprise.',
  ['R05-57']),
 ('§ 15.2, tableau 60 (semaines 7 et 8, semaine 11); § 13.4',
  'Les essais reproductibles de l’entreprise sur banc d’essai s’ouvrent aux semaines 7 et 8, avant le choix des blocs de la '
  'semaine 11; les preuves qui supposent un agent pilote sont cotées provisoirement (note 2, démonstration du fournisseur) et '
  'confirmées au premier pilote; le registre à choisir prolonge le registre initial des semaines 3 et 4.',
  ['R05-58']),
 ('Annexe A (en-tête); A.5 (point « Paliers des outils »)',
  'L’en-tête dit que la grille reprend l’ensemble des 287 exigences du registre (couverture vérifiée à la composition, module '
  '04) et non plus seulement celles qui conditionnent la mise en production; renvoi à l’EXIG-AUT-24, absente du registre (seuil '
  'et grandeur : EXIG-AUT-08), retiré.',
  ['R06-07']),
 ('Annexe A.2 à A.8; A.1 (légende de l’applicabilité)',
  'Chaque point de la grille devient une ligne de tableau (applicabilité, marque « non dérogeable » sur une seconde ligne, point '
  'à vérifier, exigences, colonne de réponse et de preuve), au lieu d’une puce où la condition et la marque se lisaient d’un '
  'trait avec le texte.',
  ['V3-32', 'R06-32']),
 ('Annexe H.5 (« Hors du cadre »)',
  'Le Real-Time Rail, qui n’avait ni date, ni fait, ni référence, quitte les « sources datées » (trois restent : NIST IR 8547, '
  'EN 18286, déclaration du BSIF); il est signalé, avec l’avis 11-348 des ACVM, le cadre des services bancaires axés sur les '
  'consommateurs et ISO 20022, parmi les absences non datées que traite le Compendium (chapitres 28, 32 et 33).',
  ['R08-30', 'X1-24'])]

import hashlib, json, re


def _empreinte_c8(s):
    """Empreinte de l'enregistrement C.8 recalculée après le renommage du champ definition_version (R06-34)."""
    i = s.index('<h3>C.8 Enregistrement d’audit</h3>')
    j = s.index('<h2>D Registre des exigences</h2>', i)
    sec = s[i:j]
    m = re.search(r'<pre><code>(\{.*?\})</code></pre>', sec, flags=re.S)
    obj = json.loads(m.group(1))
    jcs = json.dumps(obj['enregistrement'], ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')
    emp = 'sha256:' + hashlib.sha256(jcs).hexdigest()
    sec = re.sub(r'"empreinte": "sha256:[0-9a-f]{64}"', f'"empreinte": "{emp}"', sec)
    return s[:i] + sec + s[j:]


RESP_61 = {'Couverture du registre': 'Équipe plateforme', 'Découverte d’agents hors registre': 'Équipe plateforme', 'Agents sans secret partagé': 'Sécurité de l’information', 'Couverture des passerelles': 'Équipe plateforme', 'Conformité au catalogue': 'Architecture d’entreprise', 'Traçabilité': 'Équipe plateforme', 'Couverture de l’évaluation': 'Équipe d’évaluation', 'Réussite des tâches': 'Responsable technique de chaque agent', 'Escalade humaine': 'Responsable technique de chaque agent', 'Approbation sans modification': 'Équipe plateforme (EXIG-AUT-21)', 'Incidents agentiques': 'Risques et conformité', 'Délai de révocation en exercice': 'Sécurité de l’information', 'Délai d’intégration': 'Équipe plateforme', 'Réutilisation': 'Équipe plateforme', 'Coût par tâche réussie': 'Équipe FinOps', 'EFVP à jour': 'Responsable de la protection des RP'}


def _tableau_61(s):
    """Colonne « Responsable de mesure (proposé) » du tableau 61 (R05-57); rôles de la section 11.1."""
    i = s.index('<caption>Tableau 61 —')
    j = s.index('</table>', i)
    t = s[i:j]
    t = t.replace('<th><strong>Fréquence</strong></th></tr>', '<th><strong>Fréquence</strong></th><th><strong>Responsable de mesure (proposé)</strong></th></tr>', 1)
    vus = set()

    def ligne(m):
        nom = m.group(1)
        assert nom in RESP_61, nom
        vus.add(nom)
        return m.group(0)[:-len('</tr>')] + '<td>' + RESP_61[nom] + '</td></tr>'
    t = re.sub(r'<tr><td>([^<]+)</td>(?:(?!</tr>).)*</tr>', ligne, t, flags=re.S)
    assert vus == set(RESP_61), set(RESP_61) - vus
    return s[:i] + t + s[j:]



_LI_GRILLE = re.compile(r'<li>(Tous|Si [^<]*?)( non dérogeable(?: \([^)]*\))?)? <strong>(.*?)</strong>(.*?) — <code>(.*?)</code></li>', re.S)


def _tableau_grille(m):
    lignes = []
    for li in re.findall(r'<li>.*?</li>', m.group(0), flags=re.S):
        x = _LI_GRILLE.fullmatch(li)
        assert x, li[:120]
        cond, marque, titre, suite, codes = x.groups()
        applic = cond + (f'<br><strong>{marque.strip()}</strong>' if marque else '')
        lignes.append(f'<tr><td>{applic}</td><td><strong>{titre}</strong>{suite}</td><td><code>{codes}</code></td><td></td></tr>')
    return ('<table><thead><tr><th><strong>Applicabilité</strong></th><th><strong>Point à vérifier</strong></th>'
            '<th><strong>Exigences</strong></th><th><strong>Réponse et preuve</strong></th></tr></thead><tbody>'
            + ''.join(lignes) + '</tbody></table>')


def _grille_en_tableaux(s):
    """A.2 à A.8 : une ligne de tableau par point de la grille (V3-32, R06-32)."""
    a = s.index('<h3>A.2 ')
    b = s.index('<h2>B Gabarit de fiche d’agent</h2>', a)
    sec, n = re.subn(r'<ul>\n?<li>.*?</li>\n?</ul>', _tableau_grille, s[a:b], flags=re.S)
    assert n == 7, n
    return s[:a] + sec + s[b:]


def transformer(s):
    s = _empreinte_c8(s)
    s = _tableau_61(s)
    s = _grille_en_tableaux(s)
    return s, []
