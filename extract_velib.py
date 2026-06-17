import requests
import json
import os
from datetime import datetime

URL_STATION_INFO = "https://velib-metropole-opendata.smovengo.cloud/opendata/Velib_Metropole/station_information.json"
URL_STATION_STATUS = "https://velib-metropole-opendata.smovengo.cloud/opendata/Velib_Metropole/station_status.json"

def fetch_data(url):
    """Exécute la requête HTTP et récupère le JSON brut de l'API"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur lors de la récupération des données : {e}")
        return None

def save_to_local(data, data_type):
    """Sauvegarde le JSON sur une seule ligne (compatible BigQuery)"""
    if not data:
        print(f"⚠️ Pas de données à sauvegarder pour {data_type}")
        return
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data/raw/{data_type}/{data_type}_{timestamp}.json"
    
    # 💡 L'ASTUCE : Pas d'indentation, tout est écrit sur une seule ligne compacte
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
    print(f"✅ Fichier compact sauvegardé : {filename}")

def main():
    print("🚀 Démarrage de l'extraction des données Vélib...")
    
    print("📥 Récupération de 'station_information'...")
    info_data = fetch_data(URL_STATION_INFO)
    save_to_local(info_data, "station_information")
    
    print("📥 Récupération de 'station_status'...")
    status_data = fetch_data(URL_STATION_STATUS)
    save_to_local(status_data, "station_status")
    
    print("🏁 Fin de l'extraction local.")

if __name__ == "__main__":
    main()