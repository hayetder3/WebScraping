# Projet de Scraping - League of Legends Champions

Ce projet permet de récupérer des informations sur les champions de **League of Legends** à partir du site web **Fandom**. Les données extraites incluent le nom du champion, l'URL de son image, ainsi que des statistiques comme la santé, la vitesse de déplacement, l'armure et les dégâts d'attaque.

## Prérequis

- **Python 3.x** installé sur ta machine.
- **Google Chrome** ou tout autre navigateur compatible avec **ChromeDriver**.
- **ChromeDriver** installé et correctement configuré.

## Pourquoi utiliser **Selenium** et **BeautifulSoup** ?

### **Selenium**
Selenium est utilisé pour automatiser la navigation et interagir avec des pages web dynamiques. Il permet de simuler des actions comme cliquer, faire défiler la page ou attendre que certains éléments (comme des images) soient chargés avant de continuer. 

- **Avantages** :
  - Interagit avec des pages qui nécessitent l'exécution de JavaScript.
  - Permet d'attendre que les éléments de la page soient visibles ou interactifs avant de les récupérer.
  - Utile pour récupérer des éléments qui sont générés dynamiquement après le chargement initial de la page.

### **BeautifulSoup**
BeautifulSoup est utilisé pour analyser le contenu HTML des pages web. Une fois la page chargée via Selenium, BeautifulSoup permet de naviguer facilement dans le DOM et d'extraire des informations spécifiques.

- **Avantages** :
  - Simple à utiliser pour extraire des informations à partir du HTML statique.
  - Très efficace pour chercher des éléments par balise, id, ou classe.
  - Complémentaire à Selenium : nous l'utilisons après le chargement complet de la page pour simplifier l'extraction des données.

En combinant **Selenium** et **BeautifulSoup**, nous obtenons un processus robuste qui peut gérer les pages web dynamiques tout en permettant une extraction rapide et précise des données.

### Bibliothèques Python nécessaires :

- **requests** : pour envoyer des requêtes HTTP.
- **BeautifulSoup4** : pour analyser les pages HTML.
- **Selenium** : pour interagir avec des pages dynamiques.

Tu peux installer ces bibliothèques avec la commande suivante :

```bash

pip install requests beautifulsoup4 selenium

**Cloner le projet** : Utilisez `git clone` pour récupérer le projet depuis GitHub (ou un autre service de gestion de version).
   
2. **Installer les dépendances** : Une fois dans le répertoire du projet, exécutez `npm install` pour installer toutes les dépendances nécessaires listées dans `package.json`.

3. **Démarrer l'application en mode développement** : Utilisez `npm start` pour démarrer le serveur de développement. L'application sera accessible à l'adresse [http://localhost:3000](http://localhost:3000) dans votre navigateur.

4. **Créer une version optimisée** : Exécutez `npm run build` pour générer une version prête pour la production dans le dossier `build/`.
