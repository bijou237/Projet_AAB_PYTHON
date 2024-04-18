import database

class EvenementDAO:
    connect= database.connexion()
    cursor= connect.cursor()
    @classmethod
    def ajouter_evenement(cls, NomEvent, DateEvent, HeureEvent, PrixEvent, Nombre_placesEvent, LieuEvent):
        
        try:
            sql = "INSERT INTO evenement (Nom_Event, Date_Event, Heure_Event, Prix_Event, Nombreplaces_Event, Lieu_Event) VALUES (%s, %s, %s, %s, %s, %s)"
            data = (NomEvent, DateEvent, HeureEvent, PrixEvent, Nombre_placesEvent, LieuEvent)
            cls.cursor.execute(sql, data)
            cls.connect.commit()
        except Exception as error:
            print("error", error)
    

    @classmethod
    def modifier_evenement(cls, id_event, nom, date, heure, prix, nombreplaces, lieu):
        
        sql = f"UPDATE evenement SET Nom_Event=%s, Date_Event=%s, Heure_Event=%s, Prix_Event=%s, Nombreplaces_Event=%s, Lieu_Event=%s WHERE ID_Event={id_event}"
        try:
            data = (nom, date, heure, prix, nombreplaces, lieu)
            cls.cursor.execute(sql, data)
            cls.connect.commit()
            message = "success"
        except Exception as error:
            message = "failed"
            print (error)
        return message
    
        
    @classmethod
    def supprimer_evenement(cls, id_event):
       
        sql = f"DELETE FROM evenement WHERE Id_event = {id_event}"
        cls.cursor.execute(sql)
        cls.connect.commit()
      
        
    @classmethod
    def afficher_evenements(cls):
        try:
            
            sql = "SELECT * FROM evenement"
            cls.cursor.execute(sql)
            result = cls.cursor.fetchall()
            if not result:
                message = "La liste est vide"
            else:
                message= "La Liste des evenements"
                for i in result:
                    Id, nom, date, heure, prix, nombreplace, lieu = i
                    message += f"\n id_event: {Id}, {nom}, {date}, {heure}, {prix}, {nombreplace}, {lieu}"
        except Exception as error: 
            message = "error", error
        return message