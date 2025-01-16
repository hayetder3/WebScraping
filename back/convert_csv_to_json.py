import csv
import json

# Spécifiez le chemin du fichier CSV
csv_file = 'champion_data.csv'  # Assurez-vous que le CSV est dans le même dossier
json_file = 'champion_data.json'  # Le fichier JSON sera créé ici

# Ouvrir le fichier CSV et lire les données
with open(csv_file, mode='r', encoding='utf-8') as f:
    csv_reader = csv.DictReader(f)
    
    # Convertir chaque ligne du CSV en un dictionnaire
    champions = [row for row in csv_reader]

# Sauvegarder les données sous forme de JSON
with open(json_file, mode='w', encoding='utf-8') as f:
    json.dump(champions, f, ensure_ascii=False, indent=4)

print(f"Conversion terminée. Le fichier JSON est sauvegardé sous {json_file}.")
