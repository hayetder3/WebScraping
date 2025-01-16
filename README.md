# WebScraping
Scrapping et affichage des champions de League of Legends
# Champion List React App

Cette application React affiche une liste de champions avec des informations telles que le nom, l'image, la santé, la vitesse de déplacement, l'armure, et les dégâts d'attaque. Les données sont récupérées à partir d'un fichier JSON contenant des informations sur chaque champion.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les outils suivants sur votre machine :

- [Node.js](https://nodejs.org/) (version 12 ou plus)
- [npm](https://www.npmjs.com/) (généralement installé avec Node.js)

## Installation

1. Clonez ce repository sur votre machine :

```bash
git clone https://github.com/hayetder3/WebScraping.git
## Pourquoi utiliser Selenium et BeautifulSoup ?

Dans ce projet, nous utilisons **Selenium** et **BeautifulSoup** pour extraire et analyser les données web. Voici les raisons pour lesquelles ces deux bibliothèques ont été choisies :

### **Selenium**
Selenium est une bibliothèque puissante pour l'automatisation de la navigation sur le web. Il permet de simuler des interactions avec des pages web dynamiques, c'est-à-dire celles qui nécessitent des actions comme des clics, le défilement ou l'attente d'éléments dynamiques pour se charger. Il est particulièrement utile dans les cas suivants :
- **Interagir avec des pages dynamiques** : Si le contenu de la page dépend d'actions utilisateur (comme cliquer sur un bouton ou faire défiler la page), Selenium peut simuler ces interactions.
- **Gestion des pages JavaScript** : Selenium peut exécuter du code JavaScript, ce qui permet d'extraire des données de pages web générées dynamiquement.
- **Tests automatisés** : Selenium est souvent utilisé pour tester des applications web de manière automatisée, mais il peut également être utilisé pour le scraping des données.

### **BeautifulSoup**
BeautifulSoup est une bibliothèque Python pour l'analyse de documents HTML et XML. Elle est utilisée pour extraire facilement des informations spécifiques à partir de pages web statiques ou semi-dynamiques. Voici pourquoi nous l'utilisons :
- **Facilité d'extraction** : BeautifulSoup permet de naviguer facilement dans le DOM (Document Object Model) d'une page web, ce qui rend l'extraction des informations très simple.
- **Compatibilité avec Selenium** : Après avoir utilisé Selenium pour charger une page et interagir avec elle, nous utilisons BeautifulSoup pour analyser et extraire les données HTML de manière plus concise.
- **Structure des données** : BeautifulSoup simplifie la recherche d'éléments spécifiques dans une page HTML, que ce soit par balise, classe, id, etc., ce qui est idéal pour collecter les informations que nous voulons extraire.

En combinant Selenium et BeautifulSoup, nous avons un outil puissant pour extraire et analyser des données provenant de sites web dynamiques de manière efficace.
