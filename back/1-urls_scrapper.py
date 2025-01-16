import requests
from bs4 import BeautifulSoup

# URL de la page à scraper
url = "https://leagueoflegends.fandom.com/wiki/List_of_champions"

# Effectuer une requête GET
response = requests.get(url)

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Parser le contenu HTML de la page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Trouver le premier tableau sur la page
    table = soup.find('table')

    # Vérifier si le tableau a été trouvé
    if table:
        # Récupérer toutes les lignes du tableau
        rows = table.find_all('tr')

        # Récupérer les liens de la colonne "Champion"
        champion_links = []
        for row in rows:
            # Trouver la première colonne ("Champion") dans chaque ligne
            cell = row.find('td')
            if cell:
                link = cell.find('a', href=True)
                if link:
                    champion_links.append(link['href'])

        # Sauvegarder les liens dans un fichier texte
        with open('champion_links.txt', 'w', encoding='utf-8') as file:
            for link in champion_links:
                file.write(f"https://leagueoflegends.fandom.com{link}\n")

        print(f"{len(champion_links)} liens ont été extraits et sauvegardés dans 'champion_links.txt'.")
    else:
        print("Aucun tableau trouvé sur la page.")
else:
    print(f"La requête a échoué avec le code d'état : {response.status_code}")
