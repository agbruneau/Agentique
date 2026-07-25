# Bibliographie — L'interopérabilité des systèmes d'information

*Bibliographie du chapitre sur l'interopérabilité (angle dominant : intégration des systèmes d'entreprise), arrêtée à juin 2026.*

**Convention de citation.** Auteurs/Organisme (Année). *Titre*. Support/éditeur. Identifiant stable (DOI / RFC / ISO/IEC / recommandation W3C / URL).
Six catégories ; ordre alphabétique par auteur/organisme. Dans la catégorie 2, les RFC sont classées à leur rang alphabétique (par premier auteur ou éditeur), et le bloc des normes ISO/IEC est rangé par numéro de norme croissant.

**Méthode de constitution.** Recherche en éventail sur 12 sous-domaines, puis vérification adverse de chaque citation sur le web (existence, auteurs, année, numéro de norme/RFC/recommandation), enfin dédoublonnage. Bilan : **236 références vérifiées → 222 entrées après fusion des doublons ; 217 confirmées, 19 corrigées, 0 non vérifiable.** *Révision v2 (2026-06-24) : +1 référence IBM vérifiée (acquisition webMethods/StreamSets), soit 237 → 223 entrées.* *Révision v3 (2026-07-02) : +5 références vérifiées (Hardy 1988 « Confused Deputy » ; AsyncAPI 3.1.0 ; RFC 8693 Token Exchange ; drafts IETF Transaction Tokens et WIMSE), soit 242 → 228 entrées.*

**Marqueur ⚠.** Signale une *ressource vivante* (documentation produit, spécification versionnée par date, travail en cours) dont le numéro de version exact ou l'ancre doit être fixé au moment de citer.

**Deux réserves de forme.** (1) Les renvois de section par référence n'ont pas été reportés ici : chaque agent de recherche a numéroté selon sa propre vue de la TOC, ce qui rend ces renvois non fiables — un index « section → références » peut être régénéré sur demande à partir de la TOC finale. (2) Les accents des noms de mois français ne sont pas normalisés dans les chaînes de citation (préservées verbatim pour ne pas altérer les métadonnées) ; un simple chercher-remplacer suffit (« fevrier » → « février », etc.).

---

## 1. Ouvrages et articles fondateurs

- Akkoyunlu, E. A.; Ekanadham, K.; Huber, R. V. (1975). *Some Constraints and Tradeoffs in the Design of Network Communications*. Proceedings of the 5th ACM Symposium on Operating Systems Principles (SOSP'75), ACM, p. 67-74. DOI 10.1145/800213.806523.
- Armbrust, M.; Das, T.; Paranjpye, S.; Xin, R.; Zhu, S.; Ghodsi, A.; Yavuz, B.; Murthy, M.; Torres, J.; Sun, L.; Boncz, P. A.; Mokhtar, M.; Van Hovell, H.; Ionescu, A.; Luszczak, A.; Switakowski, M.; Ueshin, T.; Li, X.; Szafranski, M.; Senster, P.; Zaharia, M. (2020). *Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores*. Proceedings of the VLDB Endowment (PVLDB), vol. 13, no 12, p. 3411-3424. DOI 10.14778/3415478.3415560.
- Booth, D.; Haas, H.; McCabe, F.; Newcomer, E.; Champion, M.; Ferris, C.; Orchard, D. (2004). *Web Services Architecture*. W3C Working Group Note, 11 fevrier 2004. https://www.w3.org/TR/2004/NOTE-ws-arch-20040211/.
- Brewer, E. A. (2000). *Towards Robust Distributed Systems* (Keynote). Proceedings of the 19th Annual ACM Symposium on Principles of Distributed Computing (PODC), ACM. DOI 10.1145/343477.343502.
- Brewer, E. (2012). *CAP Twelve Years Later: How the "Rules" Have Changed*. Computer (IEEE), vol. 45, no 2, p. 23-29. DOI 10.1109/MC.2012.37. *(contexte non cité)*
- Chappell, D. A. (2004). *Enterprise Service Bus*. O'Reilly Media (série Theory in Practice). ISBN 978-0-596-00675-4.
- Chen, D.; Daclin, N. (2006). *Framework for Enterprise Interoperability*. Proceedings of the IFAC Workshop EI2N, Bordeaux, p. 77-88 ; aussi chapitre 6 dans *Interoperability for Enterprise Software and Applications* (dir. H. Panetto, N. Boudjlida), ISTE/Wiley. DOI 10.1002/9780470612200.ch6.
- Chen, D.; Doumeingts, G.; Vernadat, F. (2008). *Architectures for enterprise integration and interoperability: Past, present and future*. Computers in Industry, vol. 59, no 7, p. 647-659. Elsevier. DOI 10.1016/j.compind.2007.12.016.
- de Alfaro, L.; Henzinger, T. A. (2001). *Interface Automata*. Proceedings of ESEC/FSE-9, ACM, p. 109-120. DOI 10.1145/503209.503226.
- Dragoni, N.; Giallorenzo, S.; Lafuente, A. L.; Mazzara, M.; Montesi, F.; Mustafin, R.; Safina, L. (2017). *Microservices: Yesterday, Today, and Tomorrow*. Dans *Present and Ulterior Software Engineering* (dir. M. Mazzara, B. Meyer), Springer, Cham, p. 195-216. DOI 10.1007/978-3-319-67425-4_12.
- Erl, T. (2005). *Service-Oriented Architecture: Concepts, Technology, and Design*. Prentice Hall PTR (Pearson Education). ISBN 978-0-13-185858-9.
- Euzenat, J.; Shvaiko, P. (2013). *Ontology Matching* (2nd Edition). Springer-Verlag, Heidelberg. ISBN 978-3-642-38720-3. DOI 10.1007/978-3-642-38721-0.
- Evans, E. (2003). *Domain-Driven Design: Tackling Complexity in the Heart of Software*. Addison-Wesley Professional. ISBN 978-0-321-12521-7.
- Fielding, R. T. (2000). *Architectural Styles and the Design of Network-based Software Architectures*. Dissertation, University of California, Irvine. https://ics.uci.edu/~fielding/pubs/dissertation/top.htm.
- Fischer, M. J.; Lynch, N. A.; Paterson, M. S. (1985). *Impossibility of Distributed Consensus with One Faulty Process*. Journal of the ACM, vol. 32, no 2, p. 374-382. DOI 10.1145/3149.214121.
- Fowler, M. (2005). *Event Sourcing*. martinfowler.com (eaaDev). https://martinfowler.com/eaaDev/EventSourcing.html.
- Fowler, M. (2010). *Richardson Maturity Model*. martinfowler.com (bliki), 18 mars 2010. https://martinfowler.com/articles/richardsonMaturityModel.html.
- Fowler, M. (2011). *CQRS*. martinfowler.com (bliki). https://martinfowler.com/bliki/CQRS.html.
- Garcia-Molina, H.; Salem, K. (1987). *Sagas*. Proceedings of the 1987 ACM SIGMOD International Conference on Management of Data, p. 249-259. DOI 10.1145/38713.38742.
- Gilbert, S.; Lynch, N. (2002). *Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services*. ACM SIGACT News, vol. 33, no 2, p. 51-59. DOI 10.1145/564585.564601.
- Gilbert, S.; Lynch, N. (2012). *Perspectives on the CAP Theorem*. Computer (IEEE), vol. 45, no 2, p. 30-36. DOI 10.1109/MC.2011.389. *(contexte non cité)*
- Gray, J. (1978). *Notes on Data Base Operating Systems*. Dans *Operating Systems — An Advanced Course*, LNCS vol. 60, Springer, p. 393-481. DOI 10.1007/3-540-08755-9_9. *(contexte non cité)*
- Gruber, T. R. (1993). *A Translation Approach to Portable Ontology Specifications*. Knowledge Acquisition, vol. 5, no 2, p. 199-220. DOI 10.1006/knac.1993.1008.
- Hardy, N. (1988). *The Confused Deputy: (or why capabilities might have been invented)*. ACM SIGOPS Operating Systems Review, vol. 22, no 4, p. 36-38. DOI 10.1145/54289.871709.
- Hohpe, G.; Woolf, B. (2003). *Enterprise Integration Patterns: Designing, Building, and Deploying Messaging Solutions*. Addison-Wesley (Signature Series, M. Fowler). ISBN 978-0-321-20068-6.
- Honda, K.; Vasconcelos, V. T.; Kubo, M. (1998). *Language Primitives and Type Discipline for Structured Communication-Based Programming*. Dans *Programming Languages and Systems* (ESOP'98), LNCS vol. 1381, Springer, p. 122-138. DOI 10.1007/BFb0053567.
- Honda, K.; Yoshida, N.; Carbone, M. (2008). *Multiparty Asynchronous Session Types*. Proceedings of POPL'08, ACM, p. 273-284. DOI 10.1145/1328438.1328472.
- Kleppmann, M. (2017). *Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems*. O'Reilly Media. ISBN 978-1-4493-7332-0. *(contexte non cité)*
- Kreps, J.; Narkhede, N.; Rao, J. (2011). *Kafka: a Distributed Messaging System for Log Processing*. Proceedings of the 6th International Workshop on Networking Meets Databases (NetDB'11), Athènes (co-localisé avec SIGMOD 2011). https://www.microsoft.com/en-us/research/publication/kafka-a-distributed-messaging-system-for-log-processing/.
- Lamport, L. (1978). *Time, Clocks, and the Ordering of Events in a Distributed System*. Communications of the ACM, vol. 21, no 7, p. 558-565. DOI 10.1145/359545.359563.
- Lewis, J.; Fowler, M. (2014). *Microservices: a definition of this new architectural term*. martinfowler.com, 25 mars 2014. https://martinfowler.com/articles/microservices.html.
- Parnas, D. L. (1972). *On the Criteria To Be Used in Decomposing Systems into Modules*. Communications of the ACM, vol. 15, no 12, p. 1053-1058. DOI 10.1145/361598.361623.
- Poggi, A.; Lembo, D.; Calvanese, D.; De Giacomo, G.; Lenzerini, M.; Rosati, R. (2008). *Linking Data to Ontologies*. Dans *Journal on Data Semantics X*, LNCS vol. 4900, Springer, p. 133-173. DOI 10.1007/978-3-540-77688-8_5.
- Pritchett, D. (2008). *BASE: An Acid Alternative*. ACM Queue, vol. 6, no 3, p. 48-55. DOI 10.1145/1394127.1394128.
- Sheth, A. P.; Larson, J. A. (1990). *Federated Database Systems for Managing Distributed, Heterogeneous, and Autonomous Databases*. ACM Computing Surveys, vol. 22, no 3, p. 183-236. DOI 10.1145/96602.96604.
- Sheth, A. P. (1999). *Changing Focus on Interoperability in Information Systems: From System, Syntax, Structure to Semantics*. Dans *Interoperating Geographic Information Systems* (dir. M. Goodchild et al.), Springer (Kluwer), p. 5-29. DOI 10.1007/978-1-4615-5189-8_2.
- Sigelman, B. H.; Barroso, L. A.; Burrows, M.; Stephenson, P.; Plakal, M.; Beaver, D.; Jaspan, S.; Shanbhag, C. (2010). *Dapper, a Large-Scale Distributed Systems Tracing Infrastructure*. Google Technical Report dapper-2010-1. https://research.google/pubs/dapper-a-large-scale-distributed-systems-tracing-infrastructure/.
- Smith, R. G. (1980). *The Contract Net Protocol: High-Level Communication and Control in a Distributed Problem Solver*. IEEE Transactions on Computers, vol. C-29, no 12, p. 1104-1113. DOI 10.1109/TC.1980.1675516.
- van der Aalst, W. M. P.; ter Hofstede, A. H. M.; Kiepuszewski, B.; Barros, A. P. (2003). *Workflow Patterns*. Distributed and Parallel Databases, vol. 14, no 1, p. 5-51. Springer. DOI 10.1023/A:1022883727209. *(contexte non cité)*
- Wegner, P. (1996). *Interoperability*. ACM Computing Surveys, vol. 28, no 1, p. 285-287. DOI 10.1145/234313.234424.
- Wooldridge, M. (2009). *An Introduction to MultiAgent Systems* (2e édition). John Wiley & Sons. ISBN 978-0-470-51946-2. *(contexte non cité)*
- Young, G. (2010). *CQRS Documents*. Recueil auto-publié. https://cqrs.wordpress.com/wp-content/uploads/2010/11/cqrs_documents.pdf.

## 2. Normes et spécifications techniques

- Apache Software Foundation (2024). *Apache Avro Specification (1.12.0)*. https://avro.apache.org/docs/1.12.0/specification/. ⚠
- ASC X12 (Accredited Standards Committee X12, accrédité ANSI depuis 1979) (s. d.). *ASC X12 — Electronic Data Interchange (EDI) Standards* (publiés par release : 004010, 005010, etc.). ANSI. https://x12.org/.
- Apache Software Foundation (2024). *Apache ORC Specification (v1)*. https://orc.apache.org/specification/ORCv1/.
- Apache Software Foundation (2024). *Apache Parquet File Format Specification*. https://parquet.apache.org/docs/file-format/.
- Apache Software Foundation, Apache Arrow (2024). *Apache Arrow — Columnar Format Specification*. https://arrow.apache.org/docs/format/Columnar.html.
- Apache Software Foundation, Apache Arrow (2024). *Arrow Flight SQL Protocol Specification*. https://arrow.apache.org/docs/format/FlightSql.html.
- Apache Software Foundation, Apache Arrow (2024). *ADBC: Arrow Database Connectivity (spécification 1.1.0)*. https://arrow.apache.org/docs/format/ADBC.html.
- AsyncAPI Initiative (Linux Foundation) (2023). *AsyncAPI Specification 3.0.0*, 5 décembre 2023. https://www.asyncapi.com/docs/reference/specification/v3.0.0.
- AsyncAPI Initiative (Linux Foundation) (2026). *AsyncAPI Specification 3.1.0*, 31 janvier 2026. https://www.asyncapi.com/docs/reference/specification/v3.1.0.
- Bray, T. (Ed.) (2017). *The JavaScript Object Notation (JSON) Data Interchange Format*. IETF, Internet Standard STD 90, RFC 8259. https://www.rfc-editor.org/rfc/rfc8259.
- Bray, T.; Paoli, J.; Sperberg-McQueen, C. M.; Maler, E.; Yergeau, F. (Eds.) (2008). *Extensible Markup Language (XML) 1.0 (Fifth Edition)*. W3C Recommendation, 26 novembre 2008. https://www.w3.org/TR/2008/REC-xml-20081126/.
- Brickley, D.; Guha, R. V. (Eds.) (2014). *RDF Schema 1.1*. W3C Recommendation, 25 février 2014. https://www.w3.org/TR/2014/REC-rdf-schema-20140225/.
- Campbell, B.; Bradley, J.; Sakimura, N.; Lodderstedt, T. (2020). *OAuth 2.0 Mutual-TLS Client Authentication and Certificate-Bound Access Tokens*. IETF, RFC 8705. DOI 10.17487/RFC8705.
- Campbell, B.; Bradley, J.; Tschofenig, H. (2020). *Resource Indicators for OAuth 2.0*. IETF, RFC 8707. DOI 10.17487/RFC8707.
- Cantor, S.; Kemp, J.; Philpott, R.; Maler, E. (Eds.) (2005). *Assertions and Protocols for the OASIS Security Assertion Markup Language (SAML) V2.0*. OASIS Standard (saml-core-2.0-os), 15 mars 2005. https://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf.
- CNCF Serverless Working Group / CloudEvents (2022). *CloudEvents — Version 1.0.2*. Cloud Native Computing Foundation. https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md.
- Cyganiak, R.; Wood, D.; Lanthaler, M. (Eds.) (2014). *RDF 1.1 Concepts and Abstract Syntax*. W3C Recommendation, 25 février 2014. https://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/.
- Dalal, S.; Wilde, E. (2025). *The Deprecation HTTP Response Header Field*. IETF, RFC 9745. DOI 10.17487/RFC9745.
- Das, S.; Sundara, S.; Cyganiak, R. (Eds.) (2012). *R2RML: RDB to RDF Mapping Language*. W3C Recommendation, 27 septembre 2012. https://www.w3.org/TR/2012/REC-r2rml-20120927/.
- Eclipse Foundation (Jakarta EE) (2022). *Jakarta Messaging 3.1*. https://jakarta.ee/specifications/messaging/3.1/.
- Ecma International (2017). *Standard ECMA-404: The JSON Data Interchange Syntax (2nd edition)* (également ISO/IEC 21778:2017). https://ecma-international.org/publications-and-standards/standards/ecma-404/.
- Fett, D.; Campbell, B.; Bradley, J.; Lodderstedt, T.; Jones, M.; Waite, D. (2023). *OAuth 2.0 Demonstrating Proof of Possession (DPoP)*. IETF, RFC 9449. DOI 10.17487/RFC9449.
- Fett, D.; Yasuda, K.; Campbell, B. (2025). *Selective Disclosure for JSON Web Tokens (SD-JWT)*. IETF, RFC 9901. DOI 10.17487/RFC9901.
- Fielding, R.; Nottingham, M.; Reschke, J. (Eds.) (2022). *HTTP Semantics*. IETF, Internet Standard STD 97, RFC 9110. https://www.rfc-editor.org/rfc/rfc9110.
- FIPA (Foundation for Intelligent Physical Agents) / IEEE Computer Society (2002). *FIPA ACL Message Structure Specification (SC00061G)*, *FIPA Communicative Act Library Specification (SC00037J)*, *FIPA SL Content Language Specification (SC00008I)*, 6 décembre 2002. http://www.fipa.org/repository/standardspecs.html.
- Genestoux, J.; Parecki, A. (Eds.); W3C Social Web Working Group (2018). *WebSub*. W3C Recommendation, 23 janvier 2018. https://www.w3.org/TR/2018/REC-websub-20180123/.
- GraphQL Foundation (Linux Foundation) (2021). *GraphQL Specification (October 2021)*. https://spec.graphql.org/October2021/.
- Hardt, D. (Ed.) (2012). *The OAuth 2.0 Authorization Framework*. IETF, RFC 6749. DOI 10.17487/RFC6749.
- Harris, S.; Seaborne, A. (Eds.) (2013). *SPARQL 1.1 Query Language*. W3C Recommendation, 21 mars 2013. https://www.w3.org/TR/2013/REC-sparql11-query-20130321/.
- Hunt, P. (Ed.); Grizzle, K.; Wahlstroem, E.; Mortimore, C. (2015). *System for Cross-domain Identity Management: Core Schema*. IETF, RFC 7643. DOI 10.17487/RFC7643.
- Hunt, P. (Ed.); Grizzle, K.; Ansari, M.; Wahlstroem, E.; Mortimore, C. (2015). *System for Cross-domain Identity Management: Protocol*. IETF, RFC 7644. DOI 10.17487/RFC7644.
- ISO (2002). *Electronic data interchange for administration, commerce and transport (EDIFACT) — Application level syntax rules — Part 1*. ISO 9735-1:2002. https://www.iso.org/standard/35032.html.
- ISO (2011). *Advanced automation technologies and their applications — Requirements for establishing manufacturing enterprise process interoperability — Part 1: Framework for enterprise interoperability*. ISO 11354-1:2011. https://www.iso.org/standard/50417.html.
- ISO (2015). *... — Part 2: Maturity model for assessing enterprise interoperability*. ISO 11354-2:2015. https://www.iso.org/standard/57019.html. *(contexte non cité)*
- ISO/IEC JTC 1 (2014). *Information technology — Advanced Message Queuing Protocol (AMQP) v1.0 specification*. ISO/IEC 19464:2014. https://www.iso.org/standard/64955.html.
- ISO/IEC (2013). *Information technology — Object Management Group Business Process Model and Notation*. ISO/IEC 19510:2013. https://www.iso.org/standard/62652.html.
- ISO/IEC JTC 1 (2016). *Information technology — Message Queuing Telemetry Transport (MQTT) v3.1.1*. ISO/IEC 20922:2016. https://www.iso.org/standard/69466.html.
- ISO/IEC (2023). *Systems and software engineering — SQuaRE — Product quality model*. ISO/IEC 25010:2023. https://www.iso.org/standard/78176.html. ⚠
- ISO/IEC/IEEE (2013). *Software and systems engineering — Software testing — Part 1: Concepts and definitions*. ISO/IEC/IEEE 29119-1:2013. https://www.iso.org/standard/45142.html. *(contexte non cité)*
- ISO/IEC (2024). *Information technology — Governance of IT for the organization*. ISO/IEC 38500:2024. https://www.iso.org/standard/81684.html.
- ISO/IEC JTC 1/SC 32 (2024). *Information technology — Database languages — GQL*. ISO/IEC 39075:2024. https://www.iso.org/standard/76120.html.
- Jones, M.; Hardt, D. (2012). *The OAuth 2.0 Authorization Framework: Bearer Token Usage*. IETF, RFC 6750. DOI 10.17487/RFC6750.
- Jones, M.; Bradley, J.; Sakimura, N. (2015). *JSON Web Token (JWT)*. IETF, RFC 7519. DOI 10.17487/RFC7519.
- Jones, M.; Hunt, P.; Parecki, A. (2025). *OAuth 2.0 Protected Resource Metadata*. IETF, RFC 9728. DOI 10.17487/RFC9728. *(contexte non cité)*
- Jones, M.; Nadalin, A.; Campbell, B. (Ed.); Bradley, J.; Mortimore, C. (2020). *OAuth 2.0 Token Exchange*. IETF, RFC 8693. DOI 10.17487/RFC8693.
- Knublauch, H.; Kontokostas, D. (Eds.) (2017). *Shapes Constraint Language (SHACL)*. W3C Recommendation, 20 juillet 2017. https://www.w3.org/TR/2017/REC-shacl-20170720/.
- Lodderstedt, T.; Bradley, J.; Labunets, A.; Fett, D. (2025). *Best Current Practice for OAuth 2.0 Security*. IETF, RFC 9700, BCP 240. DOI 10.17487/RFC9700.
- Moberg, D.; Drummond, R. (2005). *MIME-Based Secure Peer-to-Peer Business Data Interchange Using HTTP, Applicability Statement 2 (AS2)*. IETF, RFC 4130. https://www.rfc-editor.org/rfc/rfc4130.html.
- OASIS (2004). *UDDI Version 3.0.2* (ratifié OASIS Standard le 3 février 2005). https://www.oasis-open.org/committees/uddi-spec/doc/spec/v3/uddi-v3.0.2-20041019.htm.
- OASIS (2007). *Web Services Business Process Execution Language (WS-BPEL) Version 2.0*. OASIS Standard, 11 avril 2007. https://docs.oasis-open.org/wsbpel/2.0/OS/wsbpel-v2.0-OS.html.
- OASIS (2007). *ebXML Messaging Services Version 3.0: Part 1, Core Features (ebMS 3.0)*. OASIS Standard, 1 octobre 2007. https://docs.oasis-open.org/ebxml-msg/ebms/v3.0/core/ebms_core-3.0-spec.html.
- OASIS (2009). *Web Services Reliable Messaging (WS-ReliableMessaging) Version 1.2*. OASIS Standard, 2 février 2009. https://docs.oasis-open.org/ws-rx/wsrm/200702/wsrm-1.2-spec-os.html.
- OASIS (2012). *Web Services Security: SOAP Message Security Version 1.1.1*. OASIS Standard, 18 mai 2012. https://docs.oasis-open.org/wss-m/wss/v1.1.1/os/wss-SOAPMessageSecurity-v1.1.1-os.html.
- OASIS AMQP TC (2012). *OASIS Advanced Message Queuing Protocol (AMQP) Version 1.0*. OASIS Standard, 29 octobre 2012. https://docs.oasis-open.org/amqp/core/v1.0/os/amqp-core-overview-v1.0-os.html.
- OASIS (2013). *AS4 Profile of ebMS 3.0 Version 1.0*. OASIS Standard, 23 janvier 2013. https://docs.oasis-open.org/ebxml-msg/ebms/v3.0/profiles/AS4-profile/v1.0/os/AS4-profile-v1.0-os.html.
- OASIS MQTT TC (2019). *MQTT Version 5.0*. OASIS Standard, 7 mars 2019. https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html.
- Object Management Group (OMG) (2013). *Business Process Model and Notation (BPMN), Version 2.0.2*. Document formal/2013-12-09. https://www.omg.org/spec/BPMN/2.0.2/. (BPMN 2.0.1 = version soumise à l'ISO et reprise en ISO/IEC 19510:2013 ; 2.0.2 = révision de maintenance ultérieure.)
- Object Management Group (OMG) (2016). *Case Management Model and Notation (CMMN), Version 1.1*. https://www.omg.org/spec/CMMN/1.1/.
- Object Management Group (OMG) (2024). *Decision Model and Notation (DMN), Version 1.5*. https://www.omg.org/spec/DMN/1.5/.
- OpenAPI Initiative (Linux Foundation) (2021). *OpenAPI Specification v3.1.0*, 18 février 2021. https://spec.openapis.org/oas/v3.1.0.html.
- OpenAPI Initiative (Linux Foundation) (2024). *Arazzo Specification v1.0.0*, mai 2024. https://spec.openapis.org/arazzo/v1.0.0.html.
- OpenAPI Initiative (Linux Foundation) (2024). *Overlay Specification v1.0.0*, 22 octobre 2024. https://spec.openapis.org/overlay/v1.0.0.html.
- OpenID Foundation FAPI Working Group (2025). *FAPI 2.0 Security Profile* (Final Specification), 22 février 2025. https://openid.net/specs/fapi-security-profile-2_0-final.html.
- OWASP API Security Project (2023). *OWASP API Security Top 10 — 2023*. OWASP Foundation, 3 juillet 2023. https://owasp.org/API-Security/editions/2023/en/0x11-t10/.
- Rose, S.; Borchert, O.; Mitchell, S.; Connelly, S. (2020). *Zero Trust Architecture*. NIST Special Publication 800-207. DOI 10.6028/NIST.SP.800-207.
- Sakimura, N.; Bradley, J.; Jones, M.; de Medeiros, B.; Mortimore, C. (2014). *OpenID Connect Core 1.0*. OpenID Foundation. https://openid.net/specs/openid-connect-core-1_0.html.
- Sakimura, N. (Ed.); Bradley, J.; Agarwal, N. (2015). *Proof Key for Code Exchange by OAuth Public Clients (PKCE)*. IETF, RFC 7636. DOI 10.17487/RFC7636.
- Sporny, M.; Longley, D.; Kellogg, G.; Lanthaler, M.; Champin, P.-A.; Lindstrom, N. (Eds.) (2020). *JSON-LD 1.1: A JSON-based Serialization for Linked Data*. W3C Recommendation, 16 juillet 2020. https://www.w3.org/TR/2020/REC-json-ld11-20200716/.
- Sporny, M.; Thibodeau Jr, T.; Herman, I.; Cohen, G.; Jones, M. B. (Eds.) (2025). *Verifiable Credentials Data Model v2.0*. W3C Recommendation, 15 mai 2025. https://www.w3.org/TR/vc-data-model-2.0/.
- STOMP Specification contributors (2012). *STOMP Protocol Specification, Version 1.2*, 22 octobre 2012. https://stomp.github.io/stomp-specification-1.2.html.
- Terbu, O.; Lodderstedt, T.; Yasuda, K.; Fett, D.; Heenan, J. (Eds.) (2025). *OpenID for Verifiable Presentations 1.0* (Final Specification), 9 juillet 2025. https://openid.net/specs/openid-4-verifiable-presentations-1_0-final.html.
- The Open Group (X/Open) (1991). *Distributed Transaction Processing: The XA Specification*. X/Open CAE Specification, document C193. ISBN 1-872630-24-3. https://publications.opengroup.org/c193.
- Thomson, M.; Benfield, C. (Eds.) (2022). *HTTP/2*. IETF, RFC 9113. https://www.rfc-editor.org/rfc/rfc9113.
- W3C / FIDO Alliance (Hodges, J.; Jones, J. C.; Jones, M. B.; Kumar, A.; Lundberg, E., Eds.) (2021). *Web Authentication: An API for accessing Public Key Credentials — Level 2*. W3C Recommendation, 8 avril 2021. https://www.w3.org/TR/webauthn-2/. *(contexte non cité)*
- W3C Distributed Tracing Working Group (2021). *Trace Context (Level 1)*. W3C Recommendation, 23 novembre 2021. https://www.w3.org/TR/trace-context/.
- W3C Distributed Tracing Working Group (2024). *Propagation format for distributed context: Baggage*. W3C Candidate Recommendation. https://www.w3.org/TR/baggage/. ⚠
- W3C OWL Working Group (2012). *OWL 2 Web Ontology Language Document Overview (Second Edition)*. W3C Recommendation, 11 décembre 2012. https://www.w3.org/TR/2012/REC-owl2-overview-20121211/.
- Wilde, E. (2019). *The Sunset HTTP Header Field*. IETF, RFC 8594. DOI 10.17487/RFC8594.
- World Wide Web Consortium (W3C) (2005). *SOAP Message Transmission Optimization Mechanism (MTOM)*. W3C Recommendation, 25 janvier 2005. https://www.w3.org/TR/2005/REC-soap12-mtom-20050125/.
- World Wide Web Consortium (W3C) (2006). *Web Services Addressing 1.0 — Core*. W3C Recommendation, 9 mai 2006. https://www.w3.org/TR/2006/REC-ws-addr-core-20060509/.
- World Wide Web Consortium (W3C) (2007). *SOAP Version 1.2 Part 1: Messaging Framework (Second Edition)*. W3C Recommendation, 27 avril 2007. https://www.w3.org/TR/2007/REC-soap12-part1-20070427/.
- World Wide Web Consortium (W3C) (2007). *Web Services Description Language (WSDL) Version 2.0 Part 1: Core Language*. W3C Recommendation, 26 juin 2007. https://www.w3.org/TR/2007/REC-wsdl20-20070626/.
- World Wide Web Consortium (W3C) (2007). *Web Services Policy 1.5 — Framework*. W3C Recommendation, 4 septembre 2007. https://www.w3.org/TR/2007/REC-ws-policy-20070904/.
- Wright, A.; Andrews, H.; Hutton, B. (Eds.); Dennis, G. (2022). *JSON Schema: A Media Type for Describing JSON Documents (Draft 2020-12)*. IETF Internet-Draft draft-bhutton-json-schema-01, 16 juin 2022. https://json-schema.org/draft/2020-12/json-schema-core.

## 3. Cadres de référence et modèles de maturité

- ATHENA Integrated Project (FP6) (2005). *Enterprise Interoperability Maturity Model (EIMM) — ATHENA Interoperability Framework*. Livrables A1/DA4. https://sintef-9012.github.io/athena-interoperability-framework/methodology/eimm.html.
- C4ISR Architecture Working Group (AWG), US DoD (1998). *Levels of Information Systems Interoperability (LISI)*. US Department of Defense, OASD (C3I), rapport technique du 30 mars 1998.
- Clark, T.; Jones, R. (1999). *Organisational Interoperability Maturity Model for C2*. Proceedings of the 1999 Command and Control Research and Technology Symposium (CCRTS), DoD CCRP.
- Guedria, W.; Chen, D.; Naudet, Y. (2008). *Interoperability Maturity Models — Survey and Comparison*. Dans *OTM 2008 Workshops* (EI2N), LNCS vol. 5333, Springer, p. 273-282. DOI 10.1007/978-3-540-88875-8_48.
- Guedria, W.; Chen, D.; Naudet, Y. (2009). *A Maturity Model for Enterprise Interoperability (MMEI)*. Dans *OTM 2009 Workshops* (EI2N), LNCS vol. 5872, Springer, p. 216-225. DOI 10.1007/978-3-642-05290-3_32.
- Guedria, W.; Naudet, Y.; Chen, D. (2011). *Enterprise Interoperability Maturity: A Model Using Fuzzy Metrics*. Dans *CAiSE 2011 Workshops*, LNBIP vol. 83, Springer, p. 69-80. DOI 10.1007/978-3-642-22056-2_8.
- NATO C3 Board, IP CaT (2024). *NATO Interoperability Standards and Profiles (NISP) — NATO Standard ADatP-34 (STANAG 5524), Vol. 1-3*. NISP Baseline 16, 5 septembre 2024. https://nhqc3s.hq.nato.int/apps/nisp/.
- SOA Manifesto Working Group (Arsanjani, A.; Booch, G.; Brown, P.; Chappell, D.; Erl, T.; Josuttis, N.; Krafzig, D.; Little, M.; et al.) (2009). *SOA Manifesto*. 2e International SOA Symposium, Rotterdam, 23 octobre 2009. http://www.soa-manifesto.org/.
- Tolk, A.; Diallo, S. Y.; Turnitsa, C. D. (2007). *Applying the Levels of Conceptual Interoperability Model in Support of Integratability, Interoperability, and Composability for System-of-Systems Engineering*. Journal of Systemics, Cybernetics and Informatics (JSCI), vol. 5, no 5, p. 65-74. ISSN 1690-4524. https://www.iiisci.org/journal/pdv/sci/pdfs/p468106.pdf.
- Tolk, A.; Muguira, J. A. (2003). *The Levels of Conceptual Interoperability Model (LCIM)*. Fall Simulation Interoperability Workshop (SIW), SISO, Orlando, paper 03F-SIW-007.
- Wang, W.; Tolk, A.; Wang, W. (2009). *The Levels of Conceptual Interoperability Model: Applying Systems Engineering Principles to Modeling and Simulation*. Proceedings of SpringSim'09. arXiv:0908.0191 / ACM DL 10.5555/1639809.1655398.

## 4. Réglementation européenne

- Commission européenne (DG DIGIT / ISA2) (2017). *New European Interoperability Framework* (Annexe 2 à COM(2017) 134 final), 23 mars 2017. CELEX:52017DC0134. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52017DC0134.
- Commission européenne (Digital Europe / Interoperable Europe) (2024). *European Interoperability Reference Architecture (EIRA) v6.1.0*, 31 mai 2024. https://interoperable-europe.ec.europa.eu/collection/european-interoperability-reference-architecture-eira/solution/eira/eira-v610-online-documentation.
- Parlement européen et Conseil de l'UE (2014). *Directive 2014/55/UE relative à la facturation électronique dans le cadre des marchés publics*. JO L 133, 6 mai 2014. CELEX:32014L0055. http://data.europa.eu/eli/dir/2014/55/oj.
- Parlement européen et Conseil de l'UE (2015). *Directive (UE) 2015/2366 (PSD2) — services de paiement dans le marché intérieur*. JO L 337, 23 décembre 2015. http://data.europa.eu/eli/dir/2015/2366/oj.
- Parlement européen et Conseil de l'UE (2023). *Règlement (UE) 2023/2854 (Data Act) — accès équitable aux données et leur utilisation*. JO L 2023/2854, 22 décembre 2023. http://data.europa.eu/eli/reg/2023/2854/oj.
- Parlement européen et Conseil de l'UE (2024). *Règlement (UE) 2024/903 du 13 mars 2024 établissant des mesures pour un niveau élevé d'interopérabilité du secteur public (acte pour une Europe interopérable)*. CELEX:32024R0903. http://data.europa.eu/eli/reg/2024/903/oj.
- Parlement européen et Conseil de l'UE (2024). *Règlement (UE) 2024/1183 modifiant le règlement (UE) no 910/2014 — cadre européen relatif à une identité numérique (eIDAS 2.0)*, 30 avril 2024. CELEX:32024R1183. http://data.europa.eu/eli/reg/2024/1183/oj.

## 5. Développements récents 2024-2026 (agents IA, lakehouse, sécurité post-quantique)

- Anthropic (2024). *Introducing the Model Context Protocol*, 25 novembre 2024. https://www.anthropic.com/news/model-context-protocol.
- Anthropic / Model Context Protocol contributors (2025). *Model Context Protocol Specification (version 2025-11-25)* (maintenu sous l'Agentic AI Foundation / Linux Foundation). https://modelcontextprotocol.io/specification/2025-11-25.
- Apache Software Foundation, Apache Gravitino (2025). *Apache Gravitino — Unified Metadata Lake*. https://gravitino.apache.org/.
- Apache Software Foundation, Apache Iceberg (2024). *Apache Iceberg Table Spec (versions 1, 2, 3)*. https://iceberg.apache.org/spec/.
- Apache Software Foundation, Apache Iceberg (2024). *Apache Iceberg REST Catalog — OpenAPI Specification*. https://github.com/apache/iceberg/blob/main/open-api/rest-catalog-open-api.yaml.
- Apache Kafka project (2024). *KIP-405: Kafka Tiered Storage*. https://cwiki.apache.org/confluence/display/KAFKA/KIP-405:+Kafka+Tiered+Storage.
- Apache Kafka project (2025). *Apache Kafka 4.0.0 Release Announcement*, 18 mars 2025. https://kafka.apache.org/blog/2025/03/18/apache-kafka-4.0.0-release-announcement/.
- Apache Kafka project (Schofield, A., et al.) (2025). *KIP-932: Queues for Kafka (Share Groups)*. https://cwiki.apache.org/confluence/display/KAFKA/KIP-932%3A+Queues+for+Kafka.
- Apache Software Foundation, Apache Polaris (2026). *Apache Polaris — Open Source Catalog for Apache Iceberg* (projet de premier niveau ASF, gradué 19 fév. 2026). https://polaris.apache.org/.
- Babaei Giglou, H.; D'Souza, J.; Auer, S. (2023). *LLMs4OL: Large Language Models for Ontology Learning*. Dans *The Semantic Web — ISWC 2023*, LNCS vol. 14265, Springer, p. 408-427. DOI 10.1007/978-3-031-47240-4_22.
- Bitol (LF AI & Data / Linux Foundation) (2025). *Open Data Contract Standard (ODCS) v3.1.0*, décembre 2025. https://github.com/bitol-io/open-data-contract-standard.
- Delta Lake Project (Linux Foundation) (2024). *Delta Lake — Delta Transaction Log Protocol (PROTOCOL.md)*. https://github.com/delta-io/delta/blob/master/PROTOCOL.md.
- Eclipse Foundation / International Data Spaces Association (IDSA) (2025). *Dataspace Protocol 2025-1*, mi-juillet 2025. https://eclipse-dataspace-protocol-base.github.io/DataspaceProtocol/2025-1/.
- Edge, D.; Trinh, H.; Cheng, N.; Bradley, J.; Chao, A.; Mody, A.; Truitt, S.; Larson, J. (2024). *From Local to Global: A Graph RAG Approach to Query-Focused Summarization*. arXiv preprint (Microsoft Research). arXiv:2404.16130.
- Ehtesham, A.; Singh, A.; Gupta, G. K.; Kumar, S. (2025). *A survey of agent interoperability protocols: MCP, ACP, A2A, and ANP*. arXiv preprint cs.AI. arXiv:2505.02279.
- Gaia-X European Association for Data and Cloud AISBL (2025). *Gaia-X Architecture Document (25.11 Release, nov. 2025)* et *Gaia-X Trust Framework 3.0 « Danube »*. https://docs.gaia-x.eu/technical-committee/architecture-document/25.11/. ⚠
- Google Developers (Google Cloud) (2025). *Google Cloud donates A2A to Linux Foundation*. https://developers.googleblog.com/en/google-cloud-donates-a2a-to-linux-foundation/.
- GraphQL Foundation (Linux Foundation) (2025). *GraphQL Specification (September 2025 edition)*, 8 septembre 2025. https://spec.graphql.org/September2025/.
- GraphQL Foundation, Composite Schemas Working Group (2025). *GraphQL Composite Schemas Specification* (travail en cours / draft). https://graphql.github.io/composite-schemas-spec/. ⚠
- Hardt, D.; Parecki, A.; Lodderstedt, T. (Eds.) (2026). *The OAuth 2.1 Authorization Framework* (Internet-Draft). IETF OAuth WG, draft-ietf-oauth-v2-1 (statut Internet-Draft, non encore RFC). https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/. ⚠
- Hou, X.; Zhao, Y.; Wang, S.; Wang, H. (2025). *Model Context Protocol (MCP): Landscape, Security Threats, and Future Research Directions*. arXiv preprint. arXiv:2503.23278.
- IBM (2024). *IBM Completes Acquisition of StreamSets and webMethods* (rachat des plateformes d'intégration de Software AG ; iPaaS hybride). Communiqué, 1er juillet 2024. https://newsroom.ibm.com/2024-07-01-IBM-Completes-Acquisition-of-StreamSets-and-webMethods,-Bolstering-its-Automation,-Data-and-AI-Portfolios.
- IBM Research (2025). *Agent Communication Protocol (ACP)* (projet BeeAI). https://github.com/i-am-bee/acp.
- IETF OAuth Working Group (Fett, D.; Tulshibagwale, A., Eds.) (2025). *Transaction Tokens* (Internet-Draft, travail en cours). draft-ietf-oauth-transaction-tokens. https://datatracker.ietf.org/doc/draft-ietf-oauth-transaction-tokens/. ⚠
- IETF WIMSE Working Group (2025). *Workload Identity in Multi System Environments (WIMSE) Architecture* (Internet-Draft, travail en cours). draft-ietf-wimse-arch. https://datatracker.ietf.org/doc/draft-ietf-wimse-arch/. ⚠
- ISO/IEC (2023). *Information technology — Artificial intelligence — Management system*. ISO/IEC 42001:2023. https://www.iso.org/standard/81230.html. *(contexte non cité)*
- JFrog Security Research ; NIST NVD (2025). *CVE-2025-6514 — mcp-remote OS command injection via untrusted MCP server connections*. NIST NVD. https://nvd.nist.gov/vuln/detail/CVE-2025-6514.
- Model Context Protocol contributors (Anthropic et al.) (2025). *Model Context Protocol — Authorization Specification*. https://modelcontextprotocol.io/specification/draft/basic/authorization. ⚠
- Model Context Protocol Project (Anthropic et al.) (2025). *Introducing the MCP Registry*. MCP Blog, 8 septembre 2025. https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/.
- National Institute of Standards and Technology (2024). *Module-Lattice-Based Key-Encapsulation Mechanism Standard (ML-KEM)*. NIST FIPS 203. DOI 10.6028/NIST.FIPS.203.
- National Institute of Standards and Technology (2024). *Module-Lattice-Based Digital Signature Standard (ML-DSA)*. NIST FIPS 204. DOI 10.6028/NIST.FIPS.204.
- National Institute of Standards and Technology (2024). *Stateless Hash-Based Digital Signature Standard (SLH-DSA)*. NIST FIPS 205. DOI 10.6028/NIST.FIPS.205.
- OpenAPI Initiative (Linux Foundation) (2025). *OpenAPI Specification v3.2.0*, 19 septembre 2025. https://spec.openapis.org/oas/v3.2.0.html.
- Tardieu, O.; Grove, D.; Bercea, G.-T.; Castro, P.; Cwiklik, J.; Epstein, E. (2023). *Reliable Actors with Retry Orchestration*. Proceedings of the ACM on Programming Languages (PACMPL), vol. 7, no PLDI, p. 1293-1316. DOI 10.1145/3591273.
- The Linux Foundation (2025). *Linux Foundation Launches the Agent2Agent Protocol Project*, 23 juin 2025. https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents.
- The Linux Foundation (2025). *Linux Foundation Welcomes the AGNTCY Project*, 29 juillet 2025. https://www.linuxfoundation.org/press/linux-foundation-welcomes-the-agntcy-project-to-standardize-open-multi-agent-system-infrastructure-and-break-down-ai-agent-silos.
- The Linux Foundation (2025). *Linux Foundation Announces the Formation of the Agentic AI Foundation (AAIF)* (MCP, goose, AGENTS.md), 9 décembre 2025. https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation.
- Unity Catalog Project (LF AI & Data / Linux Foundation) (2024). *Unity Catalog OSS — Open, Multi-modal Catalog for Data & AI*. https://github.com/unitycatalog/unitycatalog.
- Zaharia, M.; Ghodsi, A.; Xin, R.; Armbrust, M. (2021). *Lakehouse: A New Generation of Open Platforms that Unify Data Warehousing and Advanced Analytics*. CIDR 2021. https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf.

## 6. Ressources praticiennes et patrons

- Apache Pulsar project (ASF) (2024). *Apache Pulsar — Messaging Concepts*. https://pulsar.apache.org/docs/concepts-messaging/.
- Apache Software Foundation (2024). *Geo-Replication (Cross-Cluster Data Mirroring) — Apache Kafka Documentation*. https://kafka.apache.org/40/operations/geo-replication-cross-cluster-data-mirroring/. ⚠
- Beyer, B.; Jones, C.; Petoff, J.; Murphy, N. R. (dir.) (2016). *Site Reliability Engineering: How Google Runs Production Systems*. O'Reilly Media. ISBN 978-1-491-92912-4.
- Cadence Workflow (Uber) (2026). *Cadence: Distributed, Scalable, Durable Orchestration Engine*. https://github.com/cadence-workflow/cadence.
- Camunda Services GmbH (2026). *Camunda 8 Documentation — Zeebe Overview*. https://docs.camunda.io/docs/components/zeebe/zeebe-overview/. ⚠
- Cilium Authors / Isovalent / CNCF (2023). *Cilium Documentation (eBPF networking, observability and security)*. https://docs.cilium.io/. ⚠
- Confluent (2024). *Schema Registry for Confluent Platform*. https://docs.confluent.io/platform/current/schema-registry/index.html. ⚠
- Connect RPC Authors (Buf, CNCF) (2025). *The Connect Protocol*. https://connectrpc.com/docs/protocol/.
- Data Contract Initiative (2024). *Data Contract Specification (datacontract.com)*. NB : depuis ODCS v3.1.0, dépréciée au profit de l'Open Data Contract Standard (support annoncé jusqu'à fin 2026). https://datacontract.com/. ⚠
- Debezium project (Red Hat) (2025). *Debezium Documentation (Reference)*. https://debezium.io/documentation/. ⚠
- Dehghani, Z. (2022). *Data Mesh: Delivering Data-Driven Value at Scale*. O'Reilly Media. ISBN 978-1-492-09239-1.
- FIDO Alliance (2024). *FIDO User Authentication Certification Programs*. https://fidoalliance.org/fido-user-authentication-certification-programs/.
- Google / Protocol Buffers Authors (2024). *Protocol Buffers Language Specification (Proto3)*. https://protobuf.dev/reference/protobuf/proto3-spec/.
- Google LLC (2023). *Protocol Buffers — Encoding Specification*. https://protobuf.dev/programming-guides/encoding/.
- gRPC Authors (CNCF) (2025). *Core concepts, architecture and lifecycle*. https://grpc.io/docs/what-is-grpc/core-concepts/.
- Istio Authors / CNCF (2024). *Istio Documentation (service mesh)* [graduation CNCF, 12 juillet 2023]. https://istio.io/latest/docs/. ⚠
- Istio Authors / Solo.io et al. (2024). *Fast, Secure, and Simple: Istio's Ambient Mode Reaches General Availability in v1.24*. Istio Blog (CNCF), 7 novembre 2024. https://istio.io/latest/blog/2024/ambient-reaches-ga/.
- Kubernetes SIG Network (kubernetes-sigs/gateway-api) (2023). *Kubernetes Gateway API v1.0 (GA)*, 31 octobre 2023. https://github.com/kubernetes-sigs/gateway-api/releases/tag/v1.0.0.
- Li, W.; Lemieux, Y.; Gao, J.; Zhao, Z.; Han, Y. (2019). *Service Mesh: Challenges, State of the Art, and Future Research Opportunities*. 2019 IEEE SOSE, p. 122-127. DOI 10.1109/SOSE.2019.00026.
- Linkerd Authors / Buoyant / CNCF (2024). *Linkerd Documentation (service mesh)* [graduation CNCF, 28 juillet 2021]. https://linkerd.io/2/overview/. ⚠
- Majors, C.; Fong-Jones, L.; Miranda, G. (2022). *Observability Engineering: Achieving Production Excellence*. O'Reilly Media. ISBN 978-1-492-07644-5.
- Masse, M. (2011). *REST API Design Rulebook: Designing Consistent RESTful Web Service Interfaces*. O'Reilly Media. ISBN 978-1-4493-1050-9.
- MirrorMaker 2.0 (Dolan, R., KIP-382) (2019). *KIP-382: MirrorMaker 2.0*. https://cwiki.apache.org/confluence/display/KAFKA/KIP-382%3A+MirrorMaker+2.0.
- NATS project (Synadia / CNCF) (s.d.). *JetStream — NATS Documentation*. https://docs.nats.io/nats-concepts/jetstream. ⚠
- Newman, S. (2020). *Monolith to Microservices: Evolutionary Patterns to Transform Your Monolith*. O'Reilly Media. ISBN 978-1-492-04784-1.
- Newman, S. (2021). *Building Microservices: Designing Fine-Grained Systems* (2e édition). O'Reilly Media. ISBN 978-1-492-03402-5.
- OpenID Foundation (2024). *OpenID Certification Program & Conformance Suite*. https://openid.net/certification/.
- OpenPeppol AISBL (2024). *Peppol AS4 Profile (spécification eDelivery)*. https://docs.peppol.eu/edelivery/as4/specification/. ⚠
- OpenTelemetry Authors (CNCF) (2024). *OpenTelemetry Specification (API, SDK, OTLP)*. https://opentelemetry.io/docs/specs/otel/.
- OpenTelemetry Authors (CNCF) (2024). *OpenTelemetry Semantic Conventions*. https://opentelemetry.io/docs/specs/semconv/.
- Pact Foundation (2024). *Pact: Consumer-Driven Contract Testing — Documentation*. https://docs.pact.io/. ⚠
- Prud'hommeaux, E.; Boneva, I.; Labra Gayo, J. E.; Kellogg, G. (Eds.) (2019). *Shape Expressions Language 2.1 (ShEx)*. W3C Shape Expressions Community Group, Final Community Group Report, 8 octobre 2019. http://shex.io/shex-semantics/.
- RabbitMQ project (Broadcom/VMware) (s.d.). *AMQP 0-9-1 Protocol Specification*. https://www.rabbitmq.com/amqp-0-9-1-protocol. ⚠
- Richardson, C. (2018). *Microservices Patterns: With Examples in Java*. Manning Publications. ISBN 978-1-617-29454-9.
- Richardson, C. (s.d.). *Pattern: Transactional outbox*. microservices.io. https://microservices.io/patterns/data/transactional-outbox.html. ⚠
- Robinson, I. (2006). *Consumer-Driven Contracts: A Service Evolution Pattern*. martinfowler.com, 12 juin 2006. https://martinfowler.com/articles/consumerDrivenContracts.html.
- Ruecker, B. (2021). *Practical Process Automation: Orchestration and Integration in Microservices and Cloud Native Architectures*. O'Reilly Media. ISBN 978-1-492-06145-8. *(contexte non cité)*
- Service Mesh Interface (servicemeshinterface/smi-spec) / CNCF (2020). *Service Mesh Interface (SMI) Specification* (projet Sandbox, archivé en 2023). https://github.com/servicemeshinterface/smi-spec.
- SmartBear / PactFlow (2024). *PactFlow: Bi-Directional Contract Testing — Documentation*. https://docs.pactflow.io/. ⚠
- Solace Corporation (2024). *Understanding Event Meshes*. https://docs.solace.com/Get-Started/understanding-event-meshes.htm. ⚠
- SPIFFE Project (CNCF) (s.d.). *Secure Production Identity Framework for Everyone (SPIFFE) Specification / SPIRE* (projet diplômé). https://github.com/spiffe/spiffe. ⚠
- Sridharan, C. (2018). *Distributed Systems Observability: A Guide to Building Robust Systems*. O'Reilly Media. ISBN 978-1-492-03343-1.
- Stoplight (stoplightio) (2024). *Spectral: Open-Source API Description Linter*. https://github.com/stoplightio/spectral.
- Temporal Technologies (2026). *Temporal Platform Documentation (Durable Execution)*. https://docs.temporal.io/. ⚠
- Zhu, X.; She, G.; Xue, B.; et al. (2022). *Dissecting Service Mesh Overheads*. arXiv preprint. arXiv:2207.00592.

---

### Annexe — corrections appliquées à la vérification (19 entrées)

La passe de vérification adverse a **confirmé 217 références** et **corrigé 19** (aucune écartée comme non vérifiable). Exemples de corrections de métadonnées :

- Newman, *Monolith to Microservices* — année rectifiée à **2020**.
- Guedria et al., *Interoperability Maturity Models — Survey* — année rectifiée à **2008** (vs 2009).
- OMG *BPMN 2.0.2* — année rectifiée à **2013**.
- *RFC 7643* (SCIM Core) — liste d'auteurs corrigée (Hunt ; Grizzle ; Wahlstroem ; Mortimore).
- *W3C Trace Context* — éditeurs et date corrigés.
- *RFC 9728* et *RFC 8707* — auteurs corrigés.
- *OpenID for Verifiable Presentations* — éditeurs corrigés.

*Les entrées marquées ⚠ sont des ressources vivantes (doc produit, spec versionnée par date, travail en cours) : fixer la version/l'ancre exacte au moment de citer.*
