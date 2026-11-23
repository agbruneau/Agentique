// SPDX-License-Identifier: MIT
// Adaptateur mince vers le gabarit Typst partage de la collection (/gabarit-pdf/gabarit-collection.typ).
// Conserve pour compatibilite documentaire ; compile_pdf() dans assemble_livre.py utilise directement gabarit-pdf/.

#import "/gabarit-pdf/gabarit-collection.typ": collection-pdf, divider, horizontalRule

#show: collection-pdf.with(
  title: [/* {{TITLE}} */],
  subtitle: [/* {{SUBTITLE}} */],
  author: [/* {{AUTHOR}} */],
  pub-date: [/* {{PUB_DATE}} */],
  freeze-date: [/* {{FREEZE_DATE}} */],
  license-badge: [/* {{LICENSE_TEXT}} */],
  diffusion-note: [*Régime de diffusion* : /* {{LICENSE_TEXT}} */ (manuel et figures); trousse exécutable `Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/` et outillage sous licence MIT.],
  integrity-note: [*Note d'intégrité (`AO-05` & `DC-P12`)* : ouvrage conçu sur cahier des charges humain, rédigé et vérifié intégralement en six barrières `G0–G5` sur corpus ouvert haché `SHA-256` et doublures synthétiques hors modèle. Référence figée et vérifiée à la date de gel; ne constitue ni un avis juridique, ni une certification, ni une homologation sur système réel.],
)

/* {{BODY_TYPST}} */
