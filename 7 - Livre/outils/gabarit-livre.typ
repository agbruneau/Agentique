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
  diffusion-note: [*Régime de diffusion* : /* {{LICENSE_TEXT}} */ (textes et figures); scripts d'assurance qualité sous licence MIT.],
  integrity-note: [*Note d'intégrité (`AO-05`)* : ouvrage conçu sur cahier des charges humain, rédigé et vérifié intégralement par chaîne d'agents indépendants sur corpus ouvert haché `SHA-256`. Document de référence architecturale à portée consultative; ne constitue ni un avis juridique, ni une certification actuarielle ou d'audit.],
)

/* {{BODY_TYPST}} */
