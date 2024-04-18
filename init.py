from utilisateurs.utilisateur_dao import UtilisateurDao
from paies.paie_dao import PaieDao
from evenements.evenement_dao import EvenementDAO 


utilisateur_dao = UtilisateurDao
#utilisateur1 = utilisateur_dao.add_utilisateur('Math', 'tresor', '35', 'ef@test.com', '12345', 'Admin')
#print(utilisateur1)

#paie_Dao = PaieDao
#paie = PaieDao.payer_evenement('Bijoubitak', 123457825874, '2026-04-03', 564)
#print(paie)

#Utilisateur2 = utilisateur_dao.rechercher_utilisateur("Bijou")
#print(Utilisateur2)

#Utilisateur3 = utilisateur_dao.modifier_utilisateur(2,"Armel","Motinye", "40","armo@gmail.com", 12356, "Utilisateur" )
#print(Utilisateur3)

#Utilisateur4 = utilisateur_dao.afficher_utilisateur()
#print(Utilisateur4)


Evenement = EvenementDAO
#evenement = Evenement.ajouter_evenement("Diner", "2024-05-12", "13:00", "80", "120", "Saveurs du 237_227")

# Affichage des événements
print("Liste des événements après ajout :")
evenements = Evenement.afficher_evenements()
#for event in evenements:
print(evenements)


#evenement.nom_event("Updated Event")
#event = Evenement.modifier_evenement(1, "cinema", "2024-04-30", "15:00", "30", "100", "boul corbusier salle A")
#print(event)

#Suppression de l'événement

#annuler = Evenement.supprimer_evenement(3)
#print(annuler)



