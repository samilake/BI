This projet consists of :






Please see below the original request in french: 



Mise en place d’un processus ETL avec SSIS 

Taches demandées

On s'intéresse à la mise en place de deux packages permettant le chargement de source vers staging et de staging vers le datawarehouse. On utilisera la source NorthWind et certaines des tables de ce schéma.

Source --> Staging --> DW

Partie 1: Chargement Source vers staging: Products, Suppliers et Inventory

Au niveau de visual studio, Créer un package SSIS qui s'occupera de ce chargement.
Note: La source pour inventory est le fichier csv: NorthwindDailyInventoryLevelsOneWeek.csv

Partie 2: Chargement de inventory

1- Créer un deuxième package qui s'occupera de ce chargement. 
On devra d'abord créer la BD DW. 

Étape 1: DataFlow - stg Products vers DimProduct. 
Celui-ci permettra le chargement du staging vers le DW pour DimProduct. 
L'approche utilisée sera SCD avec type 2.

Étape 2: DataFlow - stg Suppliers vers DimSupplier. 
Celui-ci permettra le chargement du staging vers le DW pour DimSupplier
L'approche utilisée sera SCD avec type 2.

Étape 3: DataFlow - Populate Fact table. 

