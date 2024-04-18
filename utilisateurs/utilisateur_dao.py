import database 
class UtilisateurDao:
    connect= database.connexion()
    cursor= connect.cursor()

    @classmethod 
    def add_utilisateur(cls, nom, prenom, age, email, password, role ):
        try:
            sql = "INSERT INTO utilisateur(Nom_util, Prenom_util, Age_util, Email_util, Password_util, Role) VALUES(%s, %s, %s, %s, %s, %s)"
            params =(nom, prenom, age, email,password, role)
            cls.cursor.execute(sql, params)
            cls.connect.commit()
            print(f'Mr/Mme {nom} {prenom} a été(e) ajouté(e) avec succès!')
        except Exception as e:
            if " Duplicate entry" in str(e):
                print(f" Cet {email}: existe deja pour un autre utilsateur , veillez utiliser un autre email")
            else:
                print("Erreur d'insertion !", e)
    

    @classmethod
    def rechercher_utilisateur(cls, nom):
        try:
            sql = "SELECT * FROM utilisateur WHERE Nom_util = %s"
            cls.cursor.execute(sql, (nom,))
            utilisateur = cls.cursor.fetchone()
            if utilisateur:
                print(utilisateur)  
            else:
                print(f"Aucun utilisateur avec le nom {nom} trouvé.")
        except Exception as e:
            print("Erreur lors de l'affichage de l'utilisateur !", e)

    @classmethod
    def modifier_utilisateur(cls, id, nom, prenom, age, email, password, role):
        try:
            sql = f"UPDATE utilisateur SET Nom_util=%s, Prenom_util=%s, Age_util=%s, Email_util=%s, Password_util=%s, Role=%s WHERE Id_util={id}"
            params = (nom, prenom, age, email, password, role)
            cls.cursor.execute(sql, params)
            cls.connect.commit()
            print(f"Utilisateur avec l'Identifiant {id} a été modifié avec succès!")
            return True
        except Exception as e:
            print("Erreur de modification !", e)
            return False
        
        
    @classmethod
    def afficher_utilisateur(cls):
        try:
            sql = "SELECT * FROM utilisateur"
            cls.cursor.execute(sql)
            utilisateur = cls.cursor.fetchall()
            if not utilisateur:
                sms = "Aucune personne à afficher dans votre liste."
            else:
                sms = "Liste des personnes :"
                for row in utilisateur:
                    id, nom, prenom, age, email, password, role = row
                    sms += f"\n Id:{id} Nom: {nom}, Prenom: {prenom}, Age: {age}, Email:{email}, Password{password}, Role{role}"
        except Exception as e:
            sms = f"Une erreur s'est produite lors de l'affichage des informations de la personne : {e}"
        return sms
        """
            if utilisateur:
                print(utilisateur)  
            else:
                print(f"Aucun utilisateur avec le nom {nom} trouvé.")
            """
            #except Exception as e:
            #print("Erreur lors de l'affichage de l'utilisateur !", e)


    




      
