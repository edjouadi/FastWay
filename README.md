# 🚴 Moteur de Recommandation de Mobilité Urbaine (Paris)

## 📌 Présentation du Projet
Ce projet fait partie de mon portfolio de Data Engineering. L'objectif est de construire un pipeline de données de bout en bout (End-to-End) capable d'ingérer des données ouvertes (Open Data) de la métropole parisienne en temps réel, de les transformer en utilisant une architecture moderne, afin d'alimenter un moteur de recommandation d'itinéraires selon l'heure, la météo et la qualité de l'air.

### Stack Technique
* **Ingestion :** Python (Requests), Google Cloud Storage (GCS)
* **Entrepôt de Données :** Google BigQuery
* **Transformation & Qualité :** dbt (Data Build Tool), Great Expectations
* **Orchestration / CI-CD :** GitHub Actions
* **Restitution :** Metabase / Looker Studio

---

## 🏗️ Architecture du Pipeline (En cours)



1. **Extraction :** Script Python requêtant les API Vélib Métropole, Île-de-France Mobilités (RATP) et OpenWeatherMap.
2. **Landing Zone :** Stockage des fichiers bruts au format JSON dans un bucket Google Cloud Storage.
3. **DWH (Raw) :** Chargement automatique des données brutes dans Google BigQuery.
4. **Transformation (dbt) :** Passage d'une architecture Medallion (Staging -> Intermediate -> Marts) pour nettoyer, enrichir et agréger les données.
5. **Observabilité :** Tests de qualité des données automatisés via Great Expectations.

---

## 🛠️ Installation et Lancement Local

### Prérequis
* Python 3.10+
* Un compte Google Cloud Platform (GCP)

### Configuration de l'environnement
1. Cloner le dépôt :
   ```bash
   git clone [https://github.com/edjouadi/fastway.git](https://github.com/edjouadi/fastway.git)
   cd fastway

   pip install -r requirements.txt

   python extract_velib.py

   