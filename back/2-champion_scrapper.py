import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Fonction pour extraire les informations du champion à partir de l'URL
def scrape_champion(driver, url, writer):
    print(f"Scraping champion data from {url}...")
    
    # Définit un temps limite de 10 secondes pour charger la page
    try:
        driver.get(url)
        # Attendre que l'image soit visible dans un délai de 10 secondes
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img.pi-image-thumbnail")))
    except TimeoutException:
        print(f"Timeout exceeded for {url}, skipping...")
        return None

    # Extraire le nom du champion depuis l'URL
    name_value = url.split('/')[4]  # Extrait le nom entre "wiki/" et "/LoL"
    
    # Essayer d'extraire l'URL de l'image, sinon mettre une valeur par défaut
    try:
        image_url_value = driver.find_element(By.CSS_SELECTOR, "img.pi-image-thumbnail").get_attribute("src")
    except Exception as e:
        print(f"Erreur lors de l'extraction de l'image pour {name_value}: {e}")
        image_url_value = "N/A"  # Valeur par défaut si l'image n'est pas trouvée

    print("Name and image retrieved.")

    # Générer dynamiquement les IDs pour chaque champion
    health_id = f"Health_{name_value}_lvl"
    movement_speed_id = f"MovementSpeed_{name_value}"
    armor_id = f"Armor_{name_value}_lvl"
    attack_damage_id = f"AttackDamage_{name_value}_lvl"

    # Extraire les valeurs pour chaque statistique
    try:
        health_value = driver.find_element(By.ID, health_id).text.strip()
    except:
        health_value = "N/A"

    try:
        movement_speed_value = driver.find_element(By.ID, movement_speed_id).text.strip()
    except:
        movement_speed_value = "N/A"

    try:
        armor_value = driver.find_element(By.ID, armor_id).text.strip()
    except:
        armor_value = "N/A"

    try:
        attack_damage_value = driver.find_element(By.ID, attack_damage_id).text.strip()
    except:
        attack_damage_value = "N/A"

    # Si aucune donnée n'a été trouvée, ignorer le champion
    if health_value == "N/A" and movement_speed_value == "N/A" and armor_value == "N/A" and attack_damage_value == "N/A":
        print(f"No data found for {name_value}, skipping...")
        return None

    # Nettoyer les valeurs si nécessaire (supprimer + ou –)
    health_value = health_value.replace('+', '').replace('–', '-').strip()
    armor_value = armor_value.replace('+', '').replace('–', '-').strip()
    attack_damage_value = attack_damage_value.replace('+', '').replace('–', '-').strip()

    # Afficher les résultats
    print(f"Name: {name_value}")
    print(f"Image URL: {image_url_value}")
    print(f"Health: {health_value}")
    print(f"Movement Speed: {movement_speed_value}")
    print(f"Armor: {armor_value}")
    print(f"Attack Damage: {attack_damage_value}")
    
    # Écrire les résultats dans le CSV à chaque itération
    writer.writerow([name_value, image_url_value, health_value, movement_speed_value, armor_value, attack_damage_value])

# Configuration du navigateur
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-extensions")  # Réduit le temps de chargement
chrome_options.add_argument("--disable-dev-shm-usage")  # Empêche l'utilisation excessive de la mémoire
chrome_options.add_argument("--blink-settings=imagesEnabled=false")  # Désactive le chargement des images
service = Service('/usr/local/bin/chromedriver')  # Chemin exact vers ChromeDriver

# Lire les URLs depuis champion_links.txt
with open('champion_links.txt', 'r') as f:
    urls = f.readlines()

# Scraper chaque URL et écrire dans le CSV au fur et à mesure
csv_file = 'champion_data.csv'
try:
    driver = webdriver.Chrome(service=service, options=chrome_options)
    print("ChromeDriver lancé avec succès.")
except Exception as e:
    print(f"Erreur lors de l'ouverture de ChromeDriver: {e}")
    exit()

try:
    for url in urls:
        url = url.strip()
        with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if not file.tell() > 0:  # Vérifie si le fichier est vide, et ajoute l'en-tête si c'est le cas
                writer.writerow(["Name", "Image URL", "Health", "Movement Speed", "Armor", "Attack Damage"])
            champion_data = scrape_champion(driver, url, writer)
            if champion_data:
                print(f"Data for {champion_data[0]} saved.")

except Exception as e:
    print(f"Erreur lors du scraping des champions: {e}")
finally:
    driver.quit()

print(f"Scraping terminé. Les données sont sauvegardées dans {csv_file}.")
