#  IT Incident Analysis SPS ( local company )

## 🎯 Project Overview
This project simulates a real-world IT Data Analyst workflow. It focuses on monitoring and analyzing technical incidents (Routers, Firewalls, Switches) to optimize the **Mean Time To Resolution (MTTR)** and identify operational bottlenecks.

## 📈 Dashboard Preview
![Dashboard Preview](dashboard_preview.png) 
*Interactive dashboard built with Google Data Studio.*

## 🛠️ Technical Stack
*   Python: Synthetic data generation using `pandas` and `random` libraries.
*   Excel: Data cleaning, normalization, and KPI structuring.
*   Looker Studio: Interactive data visualization and reporting.
*   GitHub: Project documentation and version control.

## 🔍 Key Business Insights
*   Geographic Focus: Nouakchott records the highest volume of incidents, suggesting a need for increased technician allocation in this area.
*   Equipment Reliability: Routers and Firewalls are the most frequent points of failure.
*   Performance: The current average resolution time is **47 hours**. High-priority incidents are being monitored to reduce this delay.

## 🚀 How to Run the Project
1. Clone the repository.
2. Install dependencies: `pip install pandas`.
3. Run the generator: `python Scripts/generator.py` to create a fresh dataset.
4. Import the generated `SPS_incidents_data.xlsx` into Looker Studio.


*Developed by **Boubacar-tech** as part of a Data Analytics Portfolio.*



In french:

📊 Analyse des incidents IT SPS (entreprise locale)
🎯 Aperçu du projet
Ce projet simule un workflow réel d’analyste de données IT. Il se concentre sur le suivi et l’analyse des incidents techniques (routeurs, pare-feux, commutateurs) afin d’optimiser le temps moyen de résolution (MTTR) et d’identifier les goulots d’étranglement opérationnels.
📈 Aperçu du tableau de bord
�
Tableau de bord interactif créé avec Google Data Studio.
🛠️ Stack technique
Python : génération de données synthétiques avec les bibliothèques pandas et random.
Excel : nettoyage des données, normalisation et structuration des KPI.
Looker Studio : visualisation interactive des données et reporting.
GitHub : documentation du projet et gestion de version.
🔍 Principaux insights métier
Focus géographique : Nouakchott enregistre le plus grand volume d’incidents, ce qui suggère la nécessité d’augmenter l’allocation de techniciens dans cette zone.
Fiabilité des équipements : les routeurs et les pare-feux sont les points de défaillance les plus fréquents.
Performance : le temps moyen de résolution actuel est de 47 heures. Les incidents à haute priorité sont surveillés afin de réduire ce délai.
🚀 Comment exécuter le projet
Cloner le dépôt.
Installer les dépendances : pip install pandas.
Exécuter le générateur : python Scripts/generator.py pour créer un nouveau dataset.
Importer le fichier généré SPS_incidents_data.xlsx dans Looker Studio.
Développé par Boubacar-tech dans le cadre d’un portfolio en analyse de données.
