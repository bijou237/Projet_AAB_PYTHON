import database 
class UtilisateurDao:
    connect= database.connexion()
    cursor= connect.cursor()

    @classmethod 
    def add_utilisateur(cls, id, nom, prenom, age, email,password, role ):
        try:
            email_aff = cls.verification_email(cls.Id_util)
            if email_aff and email == email_aff:

                sql = "INSERT INTO utilisateur(Nom_util, Prenom_util, Age_util, Email_util, Password_util, Role) VALUES(%s, %s, %s, %s, %s, %s)"
                params =(nom, prenom, age, email,password, role)
                cls.cursor.execute(sql, params)
                cls.connect.commit()
                print(f'Mr/Mme {nom} {prenom} a été(e) ajouté(e) avec succès!')
            else: print(f"{email} Ce mail existe deja pour un autre utilisateur")
        except Exception as e:
            print("Erreur d'insertion !", e)

        #verification de l'existence d'un email
    @classmethod
    def verification_email(cls, Id_util):
        sql = "SELECT Email_util FROM utilisateur WHERE Id_util = %s"
        cls.cursor.execute(sql, (Id_util,))
        email = cls.cursor.fetchone()
        if email:
            return email[0]
        else: 
            print(f"{email} existe dejà!")



        





            
