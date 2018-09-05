This project consists of :

- Implementation of a datamart from Northwind DB
- Inital Load of datamart (ETL SQL process)
- Creation and processing of a cube (SSAS).
- Creation of reports (SSRS)

Please see below the original request in french: 

Implémentation d’un data mart

Dans ce projet, il faut modéliser un data mart pour la BD Northwind. 

Présentation de l’entreprise

La  compagnie « Northwind Foods » veut une solution BI qui va fournir des informations aux managers et aux employés sur les produits commandés par les clients. En effet les rapports qu’ils ont utilisés jusque-là sont devenus inadéquats et le nombre d’erreurs a augmenté sur ces rapports.
La compagnie dispose de plusieurs succursales, mais l’accent va être mis sur la BD OLTP disponible au niveau de la succursale mère. Cette BD offre une structure efficace pour les transactions. Les autres succursales utilisent un système similaire. On pense que si le data mart à construire pour facilement recevoir les données des autres succursales après un traitement ETL efficace
Donc la source principale, voir unique, pour ce data mart est la BD Northwind OLTP actuelle (voir à la fin du document).
Aussi, la compagnie est d’avis que le processus des ventes devrait être la priorité à cette étape.

Summary

The Northwind Foods Company wants a BI Solution that will provide information to managers and employees about what products are being order by its customers. Currently reports have become more inaccurate and the solution must assist in solving that problem.
Expectations

- The solution will store and present verified data.
- The solution will allow for simple ad hoc queries.
- The solution must include a data warehouse that is easy to use.
- The solution should include an OLAP cube.
- The solution should be simple to keep development and maintenance costs at a minimum.
- A working prototype should be available in a short period of time.

Votre travail, consiste donc à construire un data mart qui répond à ce besoin.

Vous devrez procéder en respectant la planification définie dans le fichier Excel fourni sur le R. 

Ce fichier est un fichier de départ qui devra être complété au fur et à mesure que vous avancez dans  le travail. Il servira de documentation du projet.

Les étapes proposées correspondent à celles du cycle de vie proposé par Kimball(partie modélisation des données) :

- Analyse de source de données
- Modélisation de data mart
- Implémentation du data mart
- Chargement de données dans le data mart
- Création et traitement de cube

Livrables:

- Fichier Excel mis à jour (StarterBISolutionWorksheets.xlsx)

- Modèle dimensionnel: 
  * diagramme du MLD
  * script de création du data mart
  * Base de données(fichier .mbf ou .bak)

- ETL :
  * script de chargement du data mart
  * package SSIS de chargement ETL (projet Visual Studio)

- SSAS
  * cube(projet Visual Studio)
