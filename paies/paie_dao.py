import database
class PaieDao:
    connect = database.connexion()
    cursor = connect.cursor()

    @classmethod
    def payer_evenement(cls, Nomprenom, Numerocarte, dateexp, CVV):
        try:
            Sql= "INSERT INTO paie(NomPrenom_paie, Numcarte_paie, Dateexp_paie, CVV_paie) VALUES(%s, %s, %s, %s)"
            params = (Nomprenom, Numerocarte, dateexp, CVV)
            cls.cursor.execute(Sql, params)
            cls.connect.commit() 
            message = ("Votre paiement a été effectué avec Succès !")
        except Exception as error:
            message = ("Une erreur c'est produit lors de votre paiement veiller suivre les etapes !", error)
        return message
    
    
        
    