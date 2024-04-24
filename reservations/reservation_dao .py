import database
class ReservationDao:
    connexion = database.connexion()
    cursor = connexion.cursor()

    @classmethod
    def recupere_Nom_event(cls, nom):
        sql = """
                SELECT evenement.Nom_event,  reservation.Nom_Event 
                FROM evenement 
                INNER JOIN reservation 
                ON evenement.Nom_event = reservation.Nom_Event where reservation.Nom_Event = %s
              """
        cls.cursor.execute(sql, (nom,))
        nom_event = cls.cursor.fetchone()
        if nom_event:
            message = nom_event[0]
        else:
            message = "le Nom n'existe pas "
        return message
        
    @classmethod
    def recupere_Nom_utilisateur(cls , nom):
        sql = """
                SELECT utilisateur.Nom_util, reservation.Nom_util 
                FROM utilisateur 
                INNER JOIN reservation 
                ON utilisateur.Nom_util = reservation.Nom_util where reservation.Nom_util = %s
            """
        cls.cursor.execute(sql , (nom,))
        nom_util = cls.cursor.fetchone()
        if nom_util:
            return nom_util[0]
        else:
            return "Le nom n'existe pas."

    @classmethod    
    def reservation_place(cls,nom_event, nom_util, place):
        try:
            nom_event = cls.recupere_Nom_event()
            nom_util = cls.recupere_Nom_utilisateur()
            sql = "INSERT INTO reservation (Nom_Event, Nom_util, Nombreplaces_event) VALUES (%s, %s, %s)"
            valeurs = (nom_event, nom_util, place)
            cls.cursor.execute(sql, valeurs)
            cls.connexion.commit()
            sms = "La réservation a été effectuée avec succès !"
        except Exception as e:
            sms = f"Une erreur s'est produite lors de votre réservation : {e}"
        print(sms)

    @classmethod
    def annuler_reservation_par_nom(cls, nom_utilisateur):
        try:
             # Si une réservation a été trouvée, annuler la réservation correspondante
            sql_delete = "DELETE FROM reservation WHERE Nom_util = %s"
            cls.cursor.execute(sql_delete, (nom_utilisateur,))
            cls.connexion.commit()
            return "La réservation a été annulée avec succès !"
        except Exception as e:
            return f"Une erreur s'est produite lors de l'annulation de la réservation : {e}"


