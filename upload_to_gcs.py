import os
from google.cloud import storage

# Configuration
BUCKET_NAME = "fastway-raw-storage-elias" 
KEY_PATH = "gcp-key.json" # Nom du fichier clé qu'on vient de placer ici

def upload_local_files_to_gcs(local_folder, bucket_name):
    """Parcourt le dossier local et synchronise les JSON vers le bucket GCS"""
    
    # Initialisation du client avec la clé JSON de sécurité
    if os.path.exists(KEY_PATH):
        storage_client = storage.Client.from_service_account_json(KEY_PATH)
        print("🔐 Authentification réussie via la clé de compte de service.")
    else:
        print(f"❌ Erreur : Le fichier de clé {KEY_PATH} est introuvable à la racine.")
        return
    
    try:
        bucket = storage_client.bucket(bucket_name)
        print(f"🔄 Connexion établie au bucket : {bucket_name}")
    except Exception as e:
        print(f"❌ Impossible d'accéder au bucket {bucket_name}. Erreur : {e}")
        return

    # Parcourir les dossiers locaux
    for root, _, files in os.walk(local_folder):
        for file in files:
            if file.endswith('.json'):
                local_path = os.path.join(root, file)
                
                # Structure cible dans GCS
                relative_path = os.path.relpath(local_path, local_folder)
                gcs_blob_path = f"raw/{relative_path}".replace("\\", "/")
                
                blob = bucket.blob(gcs_blob_path)
                
                print(f"⬆️ Upload en cours : {file} ➔ gs://{bucket_name}/{gcs_blob_path}")
                blob.upload_from_filename(local_path)

    print("✅ Fin de la synchronisation ! Tous les fichiers locaux sont sur GCS.")

if __name__ == "__main__":
    LOCAL_DATA_DIR = "./data/raw"
    if os.path.exists(LOCAL_DATA_DIR):
        upload_local_files_to_gcs(LOCAL_DATA_DIR, BUCKET_NAME)