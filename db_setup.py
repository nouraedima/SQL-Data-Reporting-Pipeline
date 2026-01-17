import sqlite3

def initialiser_db():
    # Connexion au fichier de base de données (il sera créé automatiquement)
    conn = sqlite3.connect('marche_data.db')
    cursor = conn.cursor()

    # Création de la table 'offres'
    # On définit des types de données SQL : TEXT, INTEGER, REAL (pour les chiffres)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS offres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titre_poste TEXT NOT NULL,
            entreprise TEXT,
            ville TEXT,
            salaire_annuel REAL,
            techno_principale TEXT,
            type_contrat TEXT,
            date_importation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()
    print("✅ La base de données 'marche_data.db' est prête !")

if __name__ == "__main__":
    initialiser_db()