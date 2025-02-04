from student_database import StudentDatabase

# Instancier la base de données
db = StudentDatabase()

# ➤ Ajouter un étudiant
new_student = {
    'sid': 2,
    'username': 'moufid',
    'email': 'moufidteixeira@gmail.com',
    'year': 2025,
    'department': 'Informatique'
}
db.insert(new_student)

# ➤ Récupérer tous les étudiants
# students = db.fetch_all()
# print("📋 Liste des étudiants :", students)

# ➤ Mettre à jour un étudiant
updated_student = {
    'username': 'john_updated',
    'email': 'john.new@example.com',
    'year': 2026,
    'department': 'IA'
}
# db.update(1, updated_student)

# ➤ Supprimer un étudiant
# db.delete(1)

# ➤ Fermer la connexion
# db.close_connection()
