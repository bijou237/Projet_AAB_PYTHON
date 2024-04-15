import database 
from utilisateur import Utilisateur
class UtilisateurDao:
    connect= database.connexion()
    cursor= connect.cursor()

    @classmethod 
    def add_utilisateur(cls,nom, prenom, age, email,password, role ):
        try:
            sql = "INSERT INTO utilisateur(Nom_util, Prenom_util, Age_util, Email_util, Password_util, Role_util) VALUES(%s, %s, %s, %s, %s, %s)"
            params =(nom, prenom, age, email,password, role)
            cls.cursor.execute(sql, params)
            cls.connect.commit()
            print(f'Mr/Mme {nom, prenom} a été(e) ajouté(e) avec succès!')
        except Exception as e:
            print("Erreur d'insertion !")
    





            
