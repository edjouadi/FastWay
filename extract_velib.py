import requests
import json
import os
from datetime import datetime

# Endpoints officiels de l'API Open Data Vélib Métropole
URL_STATION_INFO = "https://velib-metropole-opendata.smovengo.cloud/opendata/Velib_Metropole/station_information.json"
URL_STATION_STATUS = "https://velib-metropole-opendata.smovengo.cloud/opendata/Velib_Metropole/station_status.json"

def fetch_data(url):
    """Exécute la requête HTTP et récupère le JSON brut de l'API"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() # Lève une erreur si l'API est en panne (ex: erreur 500)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur lors de la récupération des données : {e}")
        return None

def save_to_local(data, data_type):
    """Sauvegarde le JSON en local dans le dossier correspondant"""
    if not data:
        print(f"⚠️ Pas de données à sauvegarder pour {data_type}")
        return
    
    # Génération d'un timestamp propre pour le nom du fichier (Ex: 20260615_143000)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data/raw/{data_type}/{data_type}_{timestamp}.json"
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"✅ Fichier sauvegardé avec succès : {filename}")

def main():
    print("🚀 Démarrage de l'extraction des données Vélib...")
    
    # 1. Extraction et sauvegarde des informations des stations (Fixes : nom, capacité...)
    print("📥 Récupération de 'station_information'...")
    info_data = fetch_data(URL_STATION_INFO)
    save_to_local(info_data, "station_information")
    
    # 2. Extraction et sauvegarde des statuts des stations (Dynamiques : vélos dispos...)
    print("📥 Récupération de 'station_status'...")
    status_data = fetch_data(URL_STATION_STATUS)
    save_to_local(status_data, "station_status")
    
    print("🏁 Fin de l'extraction local.")

if __name__ == "__main__":
    main()