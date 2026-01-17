from fpdf import FPDF
import sqlite3

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Rapport d\'Analyse : Marche de l\'Emploi Data 2026', 0, 1, 'C')
        self.ln(10)

def generer_rapport():
    # 1. Recuperation des chiffres cles via SQL
    conn = sqlite3.connect('marche_data.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM offres")
    total_offres = cursor.fetchone()[0]
    
    cursor.execute("SELECT AVG(salaire_annuel) FROM offres")
    salaire_moyen = round(cursor.fetchone()[0], 2)
    conn.close()

    # 2. Construction du PDF
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 12)

    pdf.cell(0, 10, f"Nombre total d'opportunites analysees : {total_offres}", 0, 1)
    pdf.cell(0, 10, f"Salaire moyen constate : {salaire_moyen} euros / an", 0, 1)
    pdf.ln(10)

    # 3. Insertion du graphique que tu as genere precedemment
    pdf.image('dashboard_tech_sql.png', x=10, y=50, w=180)
    
    pdf.output('Rapport_Final_Noura.pdf')
    print("🚀 Rapport 'Rapport_Final_Noura.pdf' genere avec succes !")

if __name__ == "__main__":
    generer_rapport()