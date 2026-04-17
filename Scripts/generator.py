import pandas as pd
import random
from datetime import datetime, timedelta

# Configuration constants
NUM_INCIDENTS = 400
DATE_RANGE_DAYS = 180
MIN_RESOLUTION_HOURS = 1
MAX_RESOLUTION_HOURS = 72
MIN_COST_MRU = 5000
MAX_COST_MRU = 200000

SITES = ["Nouakchott", "Zouerate", "Nouadhibou", "Kaedi"]
EQUIPEMENTS = ["Routeur", "Serveur", "Switch", "Antenne", "Firewall"]
PRIORITES = ["Haute", "Moyenne", "Basse"]
TECHNICIENS = ["Ahmed", "Mohamed", "Sidi", "Oumar", "Mariam"]
STATUTS = ["Résolu", "En cours", "En attente"]

start_date = datetime(2025, 7, 1)
data = []

# Generate incidents
for i in range(1, NUM_INCIDENTS + 1):
    incident = [
        i,
        start_date + timedelta(days=random.randint(0, DATE_RANGE_DAYS)),
        random.choice(SITES),
        random.choice(EQUIPEMENTS),
        random.choice(PRIORITES),
        random.randint(MIN_RESOLUTION_HOURS, MAX_RESOLUTION_HOURS),
        random.choice(TECHNICIENS),
        random.randint(MIN_COST_MRU, MAX_COST_MRU),
        random.choice(STATUTS)
    ]
    data.append(incident)

# Create DataFrame
columns = [
    "Incident_ID", "Date", "Site", "Type_Equipement",
    "Priorite", "Temps_Resolution_Heures",
    "Technicien", "Cout_Estime_MRU", "Statut"
]
df = pd.DataFrame(data, columns=columns)

# Save to CSV
output_file = "SPS_incident_analysis_clean.csv"
df.to_csv(output_file, index=False)

# Display analysis
print(df.head())
print(df["Site"].value_counts())

# Download from Colab (if running in Google Colab)
try:
    from google.colab import files
    files.download(output_file)
except ImportError:
    print(f"File saved locally as '{output_file}'")
