from utilisateurs.utilisateur_dao import UtilisateurDao

utilisateur_dao = UtilisateurDao
utilisateur1 = utilisateur_dao.add_utilisateur('Math', 'tresor', '35', 'def@test.com', '12345', 'Admin')
print(utilisateur1)

