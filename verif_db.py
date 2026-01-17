import sqlite3

def verifier_donnees():
    conn = sqlite3.connect('marche_data.db')
    cursor = conn.cursor()

    print("--- 📊 RAPPORT DE VÉRIFICATION SQL ---")

    # 1. Compter le nombre total d'offres
    cursor.execute("SELECT COUNT(*) FROM offres")
    total = cursor.fetchone()[0]
    print(f"✅ Nombre total d'offres en base : {total}")

    # 2. Afficher les 5 premières lignes pour vérifier la structure
    print("\n🔍 Aperçu des 5 premières lignes :")
    cursor.execute("SELECT id, titre_poste, entreprise, salaire_annuel FROM offres LIMIT 5")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # 3. Une requête plus complexe : Salaire moyen par type de contrat
    print("\n💰 Salaire moyen par type de contrat :")
    cursor.execute("""
        SELECT type_contrat, ROUND(AVG(salaire_annuel), 2) 
        FROM offres 
        GROUP BY type_contrat
    """)
    stats = cursor.fetchall()
    for s in stats:
        print(f"- {s[0]} : {s[1]} €")

    conn.close()

if __name__ == "__main__":
    verifier_donnees()