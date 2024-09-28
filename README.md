# Solutions Engineer - Coding Challenge

## Consignes

- Collecter les données de l'API Lucca :
	- salariés (**users**) : 
		- Ceux actuellement en poste, ceux qui l'ont quittés et ceux qui vont la rejoindre
		- Choix libre des informations pertinentes
	- contrats (**?**) : 
		- Type de contrat
		- Date de début et fin (s'il n'est plus en poste)
		- Titre du poste
		- Département
		- Choix libre des informations pertinentes
	- départements (**departments**) :
		- Reconstruire la hiérarchie des départements
		- Choix libre des informations pertinentes
- Stocker les données en local
	- Choix libre du format (CSV, JSON, BDD, ...)

## Contraintes et critères

- Choix architecture libre cependant :
	- Récupération des données dans un temps raisonnable (dizaines de minutes)
		- _Suivre le temps d'exécution du job_
		- _Limite des calls API : 60 requêtes par seconde_
		- _Limite de données dans l'objet retourné ?_
		