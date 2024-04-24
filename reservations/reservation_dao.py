import database
class ReservationDao:
    connexion = database.connexion()
    cursor = connexion.cursor()
        
    @classmethod
    def ajouter_reservation(cls , non_event,nom_util,place):
        requete = "INSERT INTO reservation (Nom_Event, Nom_util, Nombreplaces_event) VALUES (%s, %s, %s)"
        try:
            valeurs = (non_event, nom_util, place)
            cls.cursor.execute(requete, valeurs)
            cls.connexion.commit()
            message= f"Mr/Mme {nom_util} Votre réservation pour l'evenement {non_event}  a été effectuée avec succès !"
        except Exception as e:
            message= f"Une erreur s'est produite lors de votre réservation : {e}"
        return message


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


