import sqlite3
import random

def alimenter_db():
    # Connexion à la base que tu viens de créer
    conn = sqlite3.connect('marche_data.db')
    cursor = conn.cursor()

    # Listes pour générer des données réalistes et variées
    postes = ["Data Analyst", "Data Scientist", "Data Engineer", "BI Consultant"]
    entreprises = ["Airbus", "Capgemini", "Thales", "Startup AI", "Banque Populaire"]
    villes = ["Toulouse", "Paris", "Lyon", "Bordeaux"]
    technos = ["Python", "SQL", "Power BI", "Tableau", "AWS", "Spark"]
    contrats = ["Alternance", "Stage", "CDI", "CDD"]

    print("⏳ Injection des données dans SQL en cours...")

    for _ in range(200):  # On commence avec 200 offres robustes
        titre = random.choice(postes)
        entreprise = random.choice(entreprises)
        ville = random.choice(villes)
        techno = random.choice(technos)
        contrat = random.choice(contrats)
        # Simulation d'un salaire cohérent (ex: 35k à 60k)
        salaire = round(random.uniform(35000, 60000), 2)

        # LA REQUÊTE SQL : On insère les données dans les colonnes précises
        cursor.execute('''
            INSERT INTO offres (titre_poste, entreprise, ville, salaire_annuel, techno_principale, type_contrat)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (titre, entreprise, ville, salaire, techno, contrat))

    conn.commit()
    conn.close()
    print("✅ 200 offres structurées ont été injectées dans 'marche_data.db' !")

if __name__ == "__main__":
    alimenter_db()