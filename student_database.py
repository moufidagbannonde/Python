import pymongo
from datetime import datetime


class StudentDatabase:
    def __init__(self, db_name="tasks", collection_name="students"):
        try:
            self.client = pymongo.MongoClient("mongodb://localhost:27017/")
            self.database = self.client[db_name]
            self.collection = self.database[collection_name]
            print("✅ Bien connecté à MongoDB et collection sélectionnée.")
        except Exception as e:
            print(f"❌ Erreur de connexion à MongoDB : {e}")

    def insert(self, student):
        try:
            data = {
                'username': student['username'],
                'email': student['email'],
                'year': student['year'],
                'department': student['department'],
                'createdAt': datetime.utcnow()
            }
            sid = self.collection.insert_one(data).inserted_id
            print(f"✅ Étudiant ajouté avec succès avec l'ID {sid} !")
        except Exception as e:
            print(f"❌ Erreur d'insertion : {e}")

    def fetch_all(self):
        return list(self.collection.find())

    def update(self, sid, student):
        try:
            data = {
                'username': student['username'],
                'email': student['email'],
                'year': student['year'],
                'department': student['department']
            }
            result = self.collection.update_one({'_id': sid}, {"$set": data})
            if result.matched_count > 0:
                print("✅ Mise à jour réussie.")
            else:
                print("❌ Aucun étudiant trouvé avec cet ID.")
        except Exception as e:
            print(f"❌ Erreur de mise à jour : {e}")

    def delete(self, sid):
        try:
            result = self.collection.delete_one({'_id': sid})
            if result.deleted_count > 0:
                print("✅ Suppression réussie.")
            else:
                print("❌ Aucun étudiant trouvé avec cet ID.")
        except Exception as e:
            print(f"❌ Erreur de suppression : {e}")

    def close_connection(self):
        self.client.close()
        print("✅ Connexion MongoDB fermée.")

