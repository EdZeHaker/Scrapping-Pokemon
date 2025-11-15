# Pokémon Scraper

Un projet Python permettant de scraper automatiquement les informations et images de Pokémon depuis un site web, puis de les stocker localement.  
Ce script récupère notamment :

- Les images de Pokémon  
- Le nom des Pokémon  
- Sauvegarde propre dans un dossier `images/`
- 
## Structure du projet

Pokemon_scrap/  
│── Pokemon.py  
│── images/  
│ ├── Bulbasaur.avif  
│ ├── Charmander.avif  
│ ├── Charmeleon.avif  
│ ├── Ivysaur.avif  
│ └── Venusaur.avif  
└── README.md  

## Technologies utilisées

- `Python 3`
- `requests`
- `beautifulsoup4`
- `os`
- `urllib`

## Fonctionnement

1. Le script envoie une requête au site web ciblé.  
2. Il analyse le HTML avec **BeautifulSoup**.  
3. Il extrait les informations (noms + URL des images).  
4. Il télécharge automatiquement les images dans le dossier `images/`.

## Exécution 

Installe d’abord les dépendances :

`pip install requests beautifulsoup4`

Exécute ensuite le script :

`python3 Pokemon.py`

Les images téléchargées apparaîtront dans le dossier images/.

---

**Améliorations possibles**
- Ajouter un export CSV des données des Pokémon
- Scraper les stats complètes (type, HP, attaques…)
- Créer une interface graphique simple
- Ajouter un mode multi-pages

**Licence**  
Projet réalisé dans un cadre personnel / éducatif.
Usage libre et modifiable.
