import pandas as pd
import Randon
from datetime import datetime, timedelta

# Nombre d'incidents
n = 400

sites = ["Nouakchott", "Zouerate", "Nouadhibou", "Kaedi"]
equipements = ["Routeur", "Serveur", "Switch", "Antenne", "Firewall"]
priorites = ["Haute", "Moyenne", "Basse"]
techniciens = ["Ahmed", "Mohamed", "Sidi", "Oumar", "Mariam"]
statuts = ["Résolu", "En cours", "En attente"]

data = []

start_date = datetime(2025, 7, 1)

for i in range(1, n+1):
    incident = [
        i,
        start_date + timedelta(days=random.randint(0,180)),
        random.choice(sites),
        random.choice(equipements),
        random.choice(priorites),
        random.randint(1, 72),
        random.choice(techniciens),
        random.randint(5000, 200000),
        random.choice(statuts)
    ]
    data.append(incident)

columns = [
    "Incident_ID", "Date", "Site", "Type_Equipement",
    "Priorite", "Temps_Resolution_Heures",
    "Technicien", "Cout_Estime_MRU", "Statut"
]

df = pd.DataFrame(data, columns=columns)

df.head()
df["Site"].value_counts()
from google.colab import files
files.download("SPS_incident_analysis_clean.csv")
