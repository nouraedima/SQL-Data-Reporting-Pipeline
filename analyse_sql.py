import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def analyse_top_tech():
    # 1. Connexion à la base de données
    conn = sqlite3.connect('marche_data.db')
    
    # 2. Utilisation de Pandas pour lire une requête SQL complexe
    # On demande au SQL de compter les technos et de les trier
    query = """
        SELECT techno_principale, COUNT(*) as nombre
        FROM offres 
        GROUP BY techno_principale 
        ORDER BY nombre DESC
    """
    df = pd.read_sql_query(query, conn)
    conn.close()

    # 3. Création du graphique professionnel
    plt.figure(figsize=(10, 6))
    plt.bar(df['techno_principale'], df['nombre'], color='skyblue', edgecolor='navy')
    
    plt.title('Technologies les plus demandées sur le marché Data 2026', fontsize=14)
    plt.xlabel('Outils / Langages', fontsize=12)
    plt.ylabel('Nombre d\'offres', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Sauvegarde du nouveau dashboard
    plt.savefig('dashboard_tech_sql.png')
    print("✅ Nouveau dashboard 'dashboard_tech_sql.png' généré avec succès !")
    plt.show()

if __name__ == "__main__":
    analyse_top_tech()