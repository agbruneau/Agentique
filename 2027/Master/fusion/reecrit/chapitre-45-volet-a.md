## Mise en œuvre — Maillages B2B inter-entreprises, espaces de données et négociation multi-parties {.volet}

:::: {.encadre .executive}
::: {.encadre-titre}
**Synthèse exécutive**
:::

- **Enjeu stratégique.** Les gains internes de la fabrique agentique butent sur la frontière juridique de l'organisation : relances de fournisseurs par courriel, messages EDI X12 rigides, litiges de facturation de soixante jours, appels d'offres manuels. Exposer un agent d'achat ou de souscription à des agents externes, sans architecture de confiance mutuelle, expose l'entreprise à l'extraction de ses marges, à l'usurpation d'un mandataire social et à des engagements contractuels non autorisés.
- **Décisions architecturales structurantes.**
  1. *Irréversible à moyen terme* : fédérer les relations B2B en couplant la découverte et la délégation AGNTCY / A2A v1.0 à un connecteur EDC / DSP, à des politiques d'usage W3C ODRL 2.2, qui expriment l'usage sans l'appliquer (section 45.2), et à des identifiants d'entités juridiques vLEI (GLEIF).
  2. *Non négociable en sécurité économique* : isoler physiquement le graphe privé de valorisation interne (coûts de revient, prix de réserve, pénalités de rupture) de l'agent diplomate exposé au tiers, et déporter les enchères multi-attributs sensibles dans des salles blanches confidentielles sur TEE attesté.
  3. *Structurante pour la finance opérationnelle* : remplacer le contrôle a posteriori des factures par un rapprochement à trois voies autonome, qui subordonne la libération d'un séquestre AP2 à la concordance déterministe (Cedar) entre le mandat contractuel, la preuve physique IoT de réception et la facture; le micropaiement x402 passe par un portefeuille dédié et plafonné, avec rapprochement a posteriori (section 45.7).
- **Indicateurs de gouvernance.** Partenaires B2B actifs authentifiés par vLEI et sous contrat ODRL signé (100 %), taux de fuite de paramètres de réserve lors des campagnes Red Team B2B (0 %), délai médian de rapprochement commande-réception-règlement ($< 8\text{ min}$ hors litige physique) et taux d'écarts interceptés sans perte financière.
::::

---

## 45.8 Traverser les frontières de confiance zéro : couplage A2A / AGNTCY, connecteurs Dataspace (EDC) et identité légale vLEI

À l'intérieur d'une entreprise (chapitres 6 et 30), les agents partagent une racine de confiance : l'autorité de certification SPIFFE/SPIRE du groupe, son annuaire Entra ID et l'arbitrage hiérarchique d'une direction générale unique. Au-delà de la frontière légale, face à un donneur d'ordre industriel, un aciériste tiers, un transporteur transfrontalier ou un assureur maritime, cette racine disparaît. Chaque participant opère en confiance nulle mutuelle. Le partenaire est à la fois le fournisseur d'un concurrent direct, une cible possible de compromission de la chaîne d'approvisionnement (OWASP ASI04) et une contrepartie juridiquement autonome, dont les intérêts divergent sur le partage de la marge.

### Les limites de l'EDI patrimonial

L'EDI (ANSI X12 en Amérique du Nord, UN/EDIFACT en Europe) transporte de façon fiable des transactions canoniques : bon de commande (X12 850), avis préalable d'expédition (856), facture (810). Il reste muet devant une exception. Quand une tempête verglaçante ferme un corridor ferroviaire, ou qu'une coulée d'acier présente un écart métallurgique mineur, acceptable sous décote, sa grammaire ne permet ni de négocier un compromis multi-contraintes (délai contre remise, fractionnement de lot, itinéraire alternatif), ni de vérifier une empreinte carbone unitaire. Les portails fournisseurs font ressaisir les mêmes statuts par des opérateurs humains dans douze extranets clients incompatibles.

Remplacer un flux EDI par un canal A2A v1.0 libre serait une régression en sécurité juridique et en souveraineté des données. A2A normalise le cycle de vie d'une tâche déléguée et AGNTCY (OASF, SLIM) fournit l'annuaire et la messagerie chiffrée. Ni l'un ni l'autre ne définit le droit de réutiliser une donnée industrielle partagée, ni la capacité juridique du signataire. Les sections 45.2 et 45.3 décrivent les mécanismes qui comblent ces deux manques.

### Les quatre strates du maillage

Le maillage B2B de référence, pensé dans le sillage de Catena-X, de Manufacturing-X et de la fondation Eclipse, superpose quatre strates à chaque frontière d’entreprise. C’est une cible pour 2027, non un état de l’art vérifié : la négociation entre agents et la prévention de la collusion relèvent encore de la recherche (section 45.1).

1. **Identité vérifiable.** Un identifiant SPIFFE interne (`spiffe://boreal.ca/...`) n'a aucune valeur probante pour une banque ou un fournisseur externe. Chaque passerelle B2B présente donc un justificatif vLEI, émis par un émetteur qualifié accrédité par la GLEIF, sur infrastructure KERI / ACDC ou W3C Verifiable Credentials. Le justificatif d'entité établit qui est la contrepartie et le justificatif OOR, quel dirigeant peut l'engager; l'agent `boreal-bel-procurement` agit au nom de Groupe Boréal Inc. (division Boréal Équipements & Logistique, BEL) sous une délégation opposable du vice-président aux approvisionnements, distincte, bornée et révocable, qui renvoie à ces deux justificatifs. Le justificatif OOR désigne une personne qui occupe une fonction officielle : rien ne prévoit son émission à un agent logiciel, et l'acceptation du vLEI par un espace de données n'a pas été vérifiée (section 45.3).
2. **Souveraineté d'usage des données.** Avant qu'un agent fournisseur transmette une nomenclature technique, un passeport numérique de produit (DPP) ou une courbe de capacité d'usine, les deux connecteurs EDC négocient automatiquement en DSP une offre, puis un accord immuable `ContractAgreement` exprimé en ODRL 2.2. Après la signature bilatérale, le plan de contrôle émet un jeton éphémère `EndpointDataReference` (EDR) qui ouvre le transfert sur le plan de données. La politique ODRL exprime l'interdiction de l'ingestion des données du partenaire dans l'entraînement de modèles (`aiTrainingProhibited`), de la rétention au-delà de la clôture de l'appel d'offres et de toute retransmission à des sous-agents tiers non listés. ODRL n'applique rien : retirer un accord n'efface pas une copie, et le respect de l'accord dépend du consommateur et du contrat (section 45.2).
3. **Négociation structurée sur A2A v1.0 / SLIM.** Une fois le tunnel EDC établi et chiffré par SLIM (au moyen de MLS, *Messaging Layer Security*), les agents échangent des artefacts A2A typés par schémas JSON (`RFQProposal`, `CounterOffer`, `CapacityAttestation`) plutôt que de la prose, qui peut transporter une injection entre entreprises (OWASP ASI01 / ASI07).
4. **Coexistence avec l'EDI.** Pour les partenaires de rang 2 ou 3 qui n'ont pas encore d'agents A2A natifs fin 2026–2027, un adaptateur B2B bidirectionnel traduit les accords conclus en transactions X12 850/855/856 normalisées et préserve l'investissement ERP existant.

![Architecture de maillage B2B inter-entreprises : séparation acheteur-fournisseur, connecteurs EDC sous politique ODRL, Clean Room confidentielle et rapprochement tripartite autonome.](figures/fig-45-a-1.svg)

| Dimension B2B | EDI X12 / EDIFACT patrimonial | API / A2A direct point-à-point | Maillage fédéré A2A + EDC (ODRL) + vLEI |
|:------------------|:--------------------------|:-------------------------|:-----------------------------|
| Preuve d'entité légale | Pré-câblage VAN bilatéral lent (4–12 sem.) | Certificat mTLS technique sans mandat social | vLEI et rôle OOR vérifiables instantanément |
| Gouvernance des données | Implicite dans le contrat-cadre papier | Aucune garantie technique après la transmission | Contrat ODRL 2.2 négocié et surveillé par le connecteur EDC; le respect dépend du consommateur et du contrat |
| Gestion des exceptions | Nulle (rejet syntaxique, puis courriel humain) | Souple, mais vulnérable à la manipulation | Négociation bornée sur schémas typés et salle blanche |
| Risque d'injection ASI01 | Très faible (grammaire positionnelle stricte) | Élevé si des champs de texte libre sont ingérés par un modèle de langage | Maîtrisé (désérialisation stricte et isolation du Diplomate) |
| Règlement financier | Facture 810 et rapprochement manuel de 30–60 j | Webhook de paiement sans preuve physique | Rapprochement à trois voies déterministe : IoT, Cedar, AP2/x402 |

---

## 45.9 Négociation asymétrique, isolation des consignes et salles blanches confidentielles

La négociation entre un agent acheteur et un agent vendeur repose sur une asymétrie d'information privée. Pour arbitrer entre trois aciéristes sur un lot critique de tôles magnétiques, la fonction d'utilité de l'entreprise acheteuse dépend de paramètres confidentiels : son prix maximal tolérable (prix de réserve $P_{\max}$), le coût horaire réel d'arrêt de sa ligne d'assemblage si la livraison glisse de quarante-huit heures et le niveau exact de son stock de sécurité. Le risque est décrit à la section 45.4.

### Le contre-exemple de l'agent négociateur monolithique

Injecter `prix_max_autorise = 142 000 CAD` et `urgence_rupture_stock = CRITIQUE_J+3` dans la consigne système de l'agent qui dialogue en A2A avec l'agent commercial externe expose le surplus économique de l'entreprise. Même sans attaque directe, un agent vendeur entraîné par apprentissage par renforcement sur des milliers de négociations sonde l'élasticité de son interlocuteur en délai et en prix. Il peut aussi glisser dans les métadonnées d'un certificat produit une directive adverse qui pousse l'agent acheteur à concéder le haut de sa fourchette.

### Le Diplomate et l'Évaluateur interne

La scission de la section 45.4 prend la forme de deux composants séparés par une frontière déterministe.

1. **L'agent Diplomate externe (zone DMZ B2B).** Seul autorisé à communiquer sur le canal A2A / EDC, il ne connaît ni le prix de réserve, ni les marges internes, ni l'état des stocks. Il reçoit pour chaque tour une enveloppe de mandat tactique étroite, générée pour ce tour (par exemple : *« Demander une cotation ferme pour 40 tonnes grade M270 livrées à Drummondville avant le 18 mai, objectif cible 126 500 \$ CAD, variante autorisée sur incoterm DAP »*). Un analyseur syntaxique strict convertit chaque réponse entrante du fournisseur en structure numérique avant qu'elle franchisse la DMZ : aucun champ de commentaire libre externe n'atteint le système interne.
2. **L'Évaluateur interne (zone interne à haute sécurité).** Isolé du réseau externe, ce service hybride (optimiseur mathématique déterministe secondé par un SLM interne d'analyse contractuelle) évalue les offres structurées reçues selon une fonction de score multi-attributs pondérée :

$$U(\mathbf{x}) = w_p \cdot \frac{P_{\max} - p}{P_{\max} - P_{\text{cible}}} + w_d \cdot \exp\bigl(-\lambda \max(0, d - d_{\text{req}})\bigr) + w_q \cdot S_{\text{qual}}(q) - w_c \cdot \frac{E_{\text{CO}_2}}{E_{\text{plafond}}}$$

Tant que $p \le P_{\max}$ et que les contraintes dures de conformité sont satisfaites, le moteur calcule la contre-proposition optimale du tour $t+1$, avec un plafond dur de $T_{\max} = 4$ tours qui interdit le sondage statistique prolongé par un tiers, ou émet un jeton d'acceptation vers le sas de signature AP2.

### Vérifications sans divulgation en salle blanche

Quand la coopération exige de croiser des données mutuellement secrètes, les parties recourent à une salle blanche exécutée dans un TEE (Intel TDX, AMD SEV-SNP ou NVIDIA H100/B200 Confidential Computing). Deux cas : vérifier qu'un sous-traitant dispose de la capacité machine libre promise sur les six prochaines semaines, sans qu'il révèle son carnet de commandes clients; calculer une tarification d'assurance flotte sur la sinistralité fine, sans transférer les données brutes.

Chaque entreprise vérifie à distance l'empreinte cryptographique (PCR) du binaire d'évaluation neutre avant de lui libérer ses entrées chiffrées. L'attestation et la répartition des rôles sont décrites à la section 45.5. Le TEE exécute le calcul conjoint (optimisation linéaire, score de compatibilité ou audit d'empreinte carbone Scope 3), détruit la mémoire vive éphémère et ne renvoie aux agents A2A des deux rives qu'un résultat booléen ou agrégé signé (*« Capacité disponible confirmée à 99,4 %; prix d'équilibre mutuellement gagnant : 131 400 \$ CAD »*).

### Accords de niveau de service B2B, pénalités programmables et réputation vérifiable

Dans un écosystème ouvert, des dizaines d'agents fournisseurs publient des Agent Cards qui promettent des délais ambitieux. L'architecture fédérée complète l'évaluation ponctuelle du prix par un registre vérifiable de performance d'exécution. Chaque clôture de rapprochement à trois voies génère un reçu cryptographique cosigné, qui atteste le respect du créneau horaire, la conformité qualité et l'absence de litige. Lors des consultations A2A suivantes, le moteur d'utilité pondère l'offre nominale d'un fournisseur par sa fiabilité observée sur les douze derniers mois. Il pénalise ainsi les promesses non tenues, sans publier d'information nominative chez les concurrents.

Toute passerelle B2B applique aussi un pare-feu protocolaire asymétrique sur les délais et les volumes d'appels : un partenaire externe ne peut soumettre plus de trois requêtes d'appel d'offres par minute, ni maintenir une tâche A2A ouverte sans mise à jour au-delà du TTL négocié dans le contrat ODRL. Cette limite prévient les attaques par déni de service économique (chapitre 40), où un tiers malveillant épuiserait les budgets d'inférence internes sous un flot de fausses demandes de cotation complexes.

#### Extrait 45.1 — Politique Cedar interdisant l’accès du Diplomate B2B aux secrets internes (b2b-dmz-isolation.cedar)

Appliquée sur agentgateway, cette règle interdit à tout agent exposé au réseau EDC / A2A externe d'interroger un outil MCP interne qui expose des marges ou des prix de réserve :

``` cedar
// Tout agent en zone DMZ B2B est bloqué sur les données de marge
forbid (
  principal is Boreal::Agent,
  action == Boreal::Mcp::"InvokeTool",
  resource is Boreal::McpServer
)
when {
  principal.networkZone == "DMZ_EXTERNAL_B2B" &&
  [
    "RESERVE_PRICING",
    "INTERNAL_BILL_OF_MATERIALS_COST",
    "PLANT_OUTAGE_PENALTY_CURVE"
  ].contains(resource.dataSensitivity)
};
```

#### Extrait 45.2 — Contrat d’usage W3C ODRL 2.2 et enveloppe de négociation B2B scindée (b2b-dataspace-offer.json)

Le champ `roleCredential` y montre un justificatif OOR attribué à un délégué; l'exposé indique plutôt qu'un justificatif OOR désigne un représentant officiel et que l'agent porte une délégation distincte, bornée et révocable (section 45.3). Ce descripteur lie l'identité légale vLEI, l'interdiction d'exploitation secondaire des données sous EDC et l'offre structurée, sans aucun contexte privé interne :

``` json
{
  "@context": [
    "http://www.w3.org/ns/odrl.jsonld",
    "https://w3id.org/tractusx/v2.0/context.jsonld"
  ],
  "@type": "odrl:Offer",
  "uid": "urn:uuid:8f41c2d0-91b3-4e6a-8a11-7c3092b41e09",
  "assigner": {
    "vlei": "549300BOREALBELQC882",
    "roleCredential": "OOR:VP_SUPPLY_CHAIN_DELEGATE",
    "edcConnector": "https://edc.bel.boreal.ca/api/v2/dsp"
  },
  "target": "urn:artifact:rfq-steel-m270-2027-05",
  "permission": [{
    "action": "odrl:use",
    "constraint": [
      {
        "leftOperand": "cx-policy:UsagePurpose",
        "operator": "odrl:eq",
        "rightOperand": "b2b.spot.quotation.evaluation"
      },
      {
        "leftOperand": "odrl:elapsedTime",
        "operator": "odrl:lteq",
        "rightOperand": "PT12H"
      }
    ]
  }],
  "prohibition": [{
    "action": [
      "cx-policy:ModelTraining",
      "odrl:distribute",
      "cx-policy:CompetitorBenchmarking"
    ]
  }],
  "rfqPayload": {
    "materialSpec": "ASTM-A677-M270-35A",
    "quantityMetricTons": 40.0,
    "deliveryIncoterms": "DAP_DRUMMONDVILLE_QC",
    "latestArrivalUtc": "2027-05-18T16:00:00Z",
    "targetPriceCad": 126500,
    "maxNegotiationRounds": 4
  }
}
```

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Droit de la concurrence et chaînes d'approvisionnement : prévenir la collusion tacite algorithmique dans les espaces de données**
:::

Connecter plusieurs fournisseurs d'un même secteur à un espace de données agentique appelle l'attention des autorités de la concurrence (Bureau de la concurrence du Canada, DG COMP européenne, DOJ américain). Deux règles s'ajoutent aux précautions de la section 45.6.

1. **Étanchéité en étoile.** Lors d'un appel d'offres multi-fournisseurs, les sessions A2A / EDC sont bilatérales et isolées. Aucun signal de prix ou de capacité soumis par le fournisseur A ne transite vers le fournisseur B, même sous forme de moyenne agrégée en temps réel.
2. **Aucune clause d'alignement automatique en temps réel.** Les moteurs d'utilité proscrivent les règles du type *« égaler automatiquement le prix concurrent détecté plus 0,5 % »*, assimilables à un cartel algorithmique tacite.
::::

---

## 45.10 Du flux EDI statique au rapprochement à trois voies autonome et au séquestre AP2 / x402

Une négociation conclue en quelques secondes perd son intérêt si le cycle aval de réception, de vérification de facture et de décaissement retombe dans trente jours de rapprochements manuels. Elle expose aussi l'entreprise si un agent financier décaisse des fonds irréversibles sur la foi d'une facture envoyée par un agent tiers compromis. Le contrôle est décrit à la section 45.7. L’orchestration durable (Temporal), les capteurs IoT d’entrepôt, le moteur de politique Cedar et les protocoles AP2 / x402 doivent permettre de l’exécuter de façon instantanée, déterministe et opposable cryptographiquement.

### Les quatre temps de la saga de règlement

1. **Verrouillage contractuel initial.** À l'issue de la négociation A2A, l'évaluateur interne émet un mandat contractuel vérifiable `CartMandate`, cosigné par le connecteur du fournisseur. Il fige l'identifiant d'article Apache Ossie, la quantité exacte, le prix unitaire convenu, la fourchette de tolérance industrielle (par exemple $\pm 0{,}5\,\%$ sur pesée vrac) et les pénalités de retard. Ce séquestre logique crée le bon de commande dans SAP S/4HANA et réserve l'enveloppe budgétaire, sans émettre de mandat de paiement AP2 ni déclencher de transfert bancaire : le mandat de paiement ne s'émet qu'après un rapprochement à trois voies réussi (section 45.7).
2. **Attestation physique de réception (IoT, OASF).** À l'arrivée du camion au quai, le pont-bascule étalonné, le portique RFID et le lecteur optique du certificat d'analyse métallurgique génèrent un justificatif signé de réception. L'opérateur de quai n'intervient en HOTL que si l'inspection visuelle signale un dommage d'emballage.
3. **Arbitrage comptable hors modèle de langage, par politique Cedar.** Lorsque la demande de règlement du fournisseur arrive (`InvoiceArtifact` A2A), aucun modèle de langage ne décide de la conformité comptable. Une activité déterministe évalue la règle Cedar de rapprochement à trois voies, au centime et au kilogramme près. Le micropaiement x402 (en-tête) pour les services logistiques ou numériques à l'acte, où le service est rendu dans la réponse qui suit le paiement, échappe à ce rapprochement préalable : on le traite par un portefeuille dédié et plafonné (le jeton de règlement x402 sur compte pré-provisionné) et un rapprochement a posteriori (section 45.7).
4. **Libération du paiement ou quarantaine du litige.** Si l'écart sur les trois pièces est inférieur aux seuils contractuels, le mandat de paiement AP2 est alors émis (section 45.7), puis le connecteur de trésorerie libère l'ordre de paiement ISO 20022 et scelle le dossier fiscal en stockage WORM septennal. Pour les commandes fractionnées en plusieurs camions, le moteur Temporal décrémente de façon atomique le solde ouvert du `CartMandate` à chaque bordereau de réception unique (`lot_receipt_id`), ce qui empêche de rejouer une même pesée IoT sur deux factures partielles. Au moindre dépassement de tolérance, la somme litigieuse est gelée, la portion conforme peut faire l'objet d'un règlement partiel prévu au contrat, et un dossier contradictoire pré-instruit est transmis à l'arbitrage humain.

#### Extrait 45.3 — Arbitre déterministe de rapprochement tripartite B2B avant libération AP2 (three_way_match.py)

Exécuté comme activité durable dans Temporal, ce garde-fou bloque toute hallucination ou tentative de surfacturation externe avant l'appel à l'API de trésorerie :

``` python
from dataclasses import dataclass
from decimal import Decimal

@dataclass(frozen=True)
class MandateTerms:
    po_id: str
    supplier_vlei: str
    sku_code: str
    ordered_qty: Decimal
    unit_price_cad: Decimal
    qty_tolerance_ratio: Decimal  # ex. Decimal("0.005") = 0.5 %

@dataclass(frozen=True)
class PhysicalReceipt:
    po_id: str
    sku_code: str
    measured_qty: Decimal
    quality_passed: bool
    iot_gate_signature_valid: bool

@dataclass(frozen=True)
class SupplierInvoice:
    invoice_id: str
    po_id: str
    supplier_vlei: str
    billed_qty: Decimal
    billed_total_cad: Decimal

def evaluate_three_way_match(
    mandate: MandateTerms,
    receipt: PhysicalReceipt,
    invoice: SupplierInvoice,
) -> tuple[str, Decimal, str]:
    zero = Decimal("0.00")
    if invoice.supplier_vlei != mandate.supplier_vlei:
        return ("QUARANTINE_SECURITY", zero, "VLEI_MISMATCH")
    iot_ok = (
        receipt.iot_gate_signature_valid
        and receipt.quality_passed
    )
    if not iot_ok:
        return ("HOLD_QUALITY_HOTL", zero, "RECEIPT_UNVERIFIED")
    po_match = (
        receipt.po_id == mandate.po_id
        and invoice.po_id == mandate.po_id
        and receipt.sku_code == mandate.sku_code
    )
    if not po_match:
        return ("REJECT_CORRELATION", zero, "PO_OR_SKU_MISMATCH")

    qty_gap = abs(receipt.measured_qty - mandate.ordered_qty)
    max_gap = mandate.ordered_qty * mandate.qty_tolerance_ratio
    over_billed = invoice.billed_qty > receipt.measured_qty
    if qty_gap > max_gap or over_billed:
        return ("ESCALATE_AP_DISPUTE", zero, "QTY_OUT_OF_BOUNDS")

    raw_total = invoice.billed_qty * mandate.unit_price_cad
    expected_total = raw_total.quantize(Decimal("0.01"))
    diff = abs(invoice.billed_total_cad - expected_total)
    if diff > Decimal("0.02"):
        return ("ESCALATE_PRICE_DIFF", zero, "PRICE_DEVIATION")

    return (
        "RELEASE_AP2_SETTLEMENT",
        expected_total,
        "MATCH_VERIFIED",
    )
```

---

## 45.11 Application au fil rouge : le réseau fournisseurs et transporteurs fédéré du Groupe Boréal

Au second semestre 2027, Groupe Boréal Inc. projette sa fabrique interne (parties I à VIII) vers son écosystème d'approvisionnement et de co-assurance en Amérique du Nord et en Europe.

:::: {.encadre .filrouge}
::: {.encadre-titre}
**Fil rouge — Groupe Boréal : maillage B2B de 320 fournisseurs et transporteurs chez BEL et BCA**
:::

**Problème opérationnel initial.** Bien que la division Boréal Équipements & Logistique (BEL) ait automatisé ses sagas internes (chapitre 19), 38 % des retards d'assemblage de ses usines de Drummondville et de Mannheim provenaient d'aléas externes sur les aciers spéciaux, les roulements de précision et le transport routier transfrontalier. Les achats spot urgents mobilisaient onze acheteurs seniors par courriel et téléphone pendant 72 heures, et le service des comptes fournisseurs traitait manuellement 4 900 écarts de facturation EDI 810 par trimestre. De son côté, Boréal Capital & Assurances (BCA) mettait neuf jours ouvrables à placer en co-assurance externe les risques industriels qui dépassent sa rétention nette de 10 M\$ CAD.

**Architecture déployée.**

1. **Passerelle fédérée EDC + AGNTCY et identité vLEI.** Boréal a équipé sa DMZ de Montréal et de Francfort de connecteurs EDC adossés à agentgateway et authentifiés par les vLEI de BEL et de BCA. Les 85 fournisseurs stratégiques de rang 1 ont raccordé leurs agents commerciaux en A2A v1.0 sous contrat ODRL 2.2. Les 235 transporteurs et fournisseurs de rang 2 ont été intégrés par le traducteur bidirectionnel A2A ↔︎ EDI X12.
2. **Séparation du Diplomate et de l'Évaluateur interne, et salle blanche de co-assurance.** Chez BEL, les courbes de coûts de rupture d'atelier restent confinées sur le cluster interne. L'agent diplomate négocie en quatre tours maximum les réallocations de lots en cas de perturbation logistique. Chez BCA, le placement de tranches de co-assurance avec trois réassureurs canadiens et européens se fait dans une salle blanche confidentielle Azure/OVHcloud SEV-SNP, qui calcule la prime technique sans exposer le portefeuille nominatif des assurés (Loi 25 et BSIF E-23 tiers).
3. **Rapprochement à trois voies : IoT, SAP et AP2.** Aux quais des neuf centres logistiques BEL, la pesée connectée et le contrôle RFID déclenchent l'arbitre déterministe (Extrait 45.3).

**Résultats mesurés après six mois.**

- Le délai d'approvisionnement spot sur incident passe de 72 heures à 34 minutes, ce qui réduit de 61 % les arrêts de ligne liés aux ruptures fournisseurs.
- Le taux de règlement sans intervention humaine passe de 54 % à 93,8 %, avec zéro décaissement erroné et une économie d'escompte pour paiement rapide validé de 2,1 M\$ CAD/an.
- **Audit Red Team B2B.** Les 400 tentatives adversariales d'extraction du prix de réserve menées contre l'agent diplomate ont toutes échoué (0 % de fuite : la valeur secrète est physiquement absente de son contexte mémoire).
::::

---

## 45.12 Décision d’architecture normative et points de contrôle

La décision ADR-026 codifie les règles d'ouverture du maillage agentique aux partenaires commerciaux externes. La décision (a) va au-delà de ce que retient l'exposé, qui recommande un justificatif d'entité vérifiable (le vLEI si le réseau l'accepte, ce qui n'a pas été vérifié) et une délégation distincte, bornée et révocable (section 45.3). La décision (c) et l'option retenue valent hors micropaiement x402, que l'exposé traite par un portefeuille dédié et plafonné et un rapprochement a posteriori (section 45.7).

:::: {.encadre .adr}
::: {.encadre-titre}
**ADR-026 — Maillage B2B fédéré sous connecteurs Dataspace (EDC/ODRL), isolation du diplomate et règlement tripartite déterministe**
:::

- **Statut** : Acceptée \| Périmètre : Relations B2B, Achats, Logistique & Co-assurance \| Révision : Semestrielle
- **Contexte** : L'automatisation inter-entreprises par A2A v1.0 apporte des gains d'agilité sur l'EDI classique, mais expose l'entreprise au vol de secrets économiques, au réemploi non consenti de ses données industrielles, à l'injection adverse entre organisations et à la fraude au paiement si le modèle contrôle directement la trésorerie.
- **Options évaluées** :
  1. *Maintien exclusif de l'EDI X12/EDIFACT et de portails web manuels* : Rejetée — incapacité à gérer dynamiquement les pénuries, retards et négociations multi-attributs.
  2. *Exposition directe d'agents internes complets sur Internet via A2A et mTLS* : Rejetée — fuite des prix de réserve sous sondage adverse et absence de gouvernance d'usage des données partagées.
  3. *Architecture B2B à connecteur EDC (ODRL + vLEI), séparation du Diplomate et de l'Évaluateur interne, salles blanches matérielles pour les calculs conjoints et libération AP2/x402 conditionnée à un rapprochement à trois voies déterministe* : Retenue.
- **Décision** : (a) exiger une identité légale vLEI et un contrat W3C ODRL 2.2 sur tout canal B2B mutatif; (b) interdire la présence des marges internes, des stocks critiques et des prix de réserve dans le contexte de tout agent qui dialogue avec l'extérieur; (c) imposer la validation déterministe, hors modèle de langage, du triptyque commande, réception physique et facture avant tout décaissement.
- **Conséquences** : Protection du secret d'affaires contre la divulgation directe (les concessions révèlent encore le prix de réserve, section 45.4), opposabilité juridique entre entreprises et réduction du risque de paiement indu, que le rapprochement ne supprime pas : un paiement indu se traite par compensation (section 45.7), au prix de l'exploitation d'une passerelle EDC en DMZ et de la normalisation stricte des schémas d'offres.
::::

### Liste de contrôle de mise en production

1. **Identité vLEI.** Chaque partenaire B2B connecté au maillage présente-t-il un justificatif d'entité vLEI, le justificatif OOR de son représentant officiel et la délégation distincte, bornée et révocable de son agent, vérifiés cryptographiquement à l'ouverture de session ?
2. **Contrat d'usage ODRL 2.2.** Tout échange de données techniques, tarifaires ou de capacité est-il gouverné par une politique ODRL qui interdit l'entraînement de modèles tiers et la redistribution ?
3. **Scission Diplomate / Évaluateur.** La revue d'architecture prouve-t-elle que l'agent exposé au réseau externe n'a aucun accès en lecture aux prix de réserve, aux coûts marginaux et aux niveaux de stocks critiques ?
4. **Désérialisation stricte en DMZ.** Les offres et contre-propositions entrantes sont-elles converties en structures numériques typées, avec rejet ou isolement de tout texte libre qui pourrait porter une injection ASI01 ?
5. **Plafond de tours et anti-collusion.** Le protocole de négociation borne-t-il le nombre de tours ($\le 4$) et garantit-il l'étanchéité totale de l'information entre soumissionnaires concurrents ?
6. **Salles blanches.** Les calculs conjoints sur des données confidentielles mutuelles s'exécutent-ils dans un TEE dont chaque partie vérifie l'attestation matérielle avant le déchiffrement ?
7. **Rapprochement à trois voies hors modèle de langage.** La libération d'un règlement AP2 est-elle subordonnée à un contrôle déterministe exact entre le mandat signé, la preuve IoT et qualité de réception, et la facture, et le micropaiement x402 passe-t-il par un portefeuille dédié et plafonné, avec rapprochement a posteriori ?
8. **Passerelle de repli EDI.** Un adaptateur A2A ↔︎ EDI X12/EDIFACT permet-il d'intégrer sans rupture les fournisseurs et transporteurs patrimoniaux non agentiques ?
