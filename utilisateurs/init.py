from utilisateur_dao import UtilisateurDao
from utilisateur import Utilisateur



utilisateur1 = Utilisateur('Bijou', 'tresor', '35', 'bij@test.com', '12345', 'Admin')
add = UtilisateurDao.add_utilisateur()
print(utilisateur1)
#utilisateur_dao = UtilisateurDao()
#utilisateur1_id = utilisateur_dao.add_utilisateur(utilisateur1)

#print(utilisateur1)
