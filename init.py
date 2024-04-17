from utilisateurs.utilisateur_dao import UtilisateurDao
from paies.paie_dao import PaieDao

utilisateur_dao = UtilisateurDao
utilisateur1 = utilisateur_dao.add_utilisateur('Math', 'tresor', '35', 'ef@test.com', '12345', 'Admin')
print(utilisateur1)

#paie_Dao = PaieDao
#paie = PaieDao.payer_evenement('Bijoubitak', 123457825874, '2026-04-03', 564)
#print(paie)


