-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : ven. 26 avr. 2024 à 02:55
-- Version du serveur : 10.4.32-MariaDB
-- Version de PHP : 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `projet_aab`
--

-- --------------------------------------------------------

--
-- Structure de la table `evenement`
--

CREATE TABLE `evenement` (
  `Id_event` int(15) NOT NULL,
  `Nom_event` varchar(45) NOT NULL,
  `Date_event` varchar(45) NOT NULL,
  `Heure_event` varchar(45) NOT NULL,
  `Prix_event` varchar(45) NOT NULL,
  `Nombreplaces_event` varchar(45) NOT NULL,
  `Lieu_event` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `evenement`
--

INSERT INTO `evenement` (`Id_event`, `Nom_event`, `Date_event`, `Heure_event`, `Prix_event`, `Nombreplaces_event`, `Lieu_event`) VALUES
(1, 'cinema', '2024-04-30', '15:00', '30', '100', 'boul corbusier salle A'),
(2, 'Diner', '2024-05-12', '13:00', '80', '120', 'Saveurs du 237_227');

-- --------------------------------------------------------

--
-- Structure de la table `paie`
--

CREATE TABLE `paie` (
  `Id_paie` int(15) NOT NULL,
  `NomPrenom_paie` varchar(45) NOT NULL,
  `Numcarte_paie` int(45) NOT NULL,
  `Dateexp_paie` varchar(45) NOT NULL,
  `CVV_paie` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `paie`
--

INSERT INTO `paie` (`Id_paie`, `NomPrenom_paie`, `Numcarte_paie`, `Dateexp_paie`, `CVV_paie`) VALUES
(1, 'Bijoubitak', 2147483647, '2026-04-03', 564);

-- --------------------------------------------------------

--
-- Structure de la table `reservation`
--

CREATE TABLE `reservation` (
  `Id_reserv` int(15) NOT NULL,
  `Nom_Event` varchar(45) NOT NULL,
  `Nom_util` varchar(45) NOT NULL,
  `Nombreplaces_event` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `reservation`
--

INSERT INTO `reservation` (`Id_reserv`, `Nom_Event`, `Nom_util`, `Nombreplaces_event`) VALUES
(5, 'AQUAMAN 2', 'Bijou', '5'),
(6, 'AMAZONES', 'Armel', '2'),
(14, 'REVOLUTION', 'Armel', '8'),
(15, 'REVOLUTION', 'Armel', '8'),
(16, 'REVOLUTION', 'Armel', '8'),
(17, 'REVOLUTION', 'Armel', '8'),
(18, 'SPIDER MAN2', 'bijou', '2'),
(19, 'SPIDER MAN2', 'bijou', '2'),
(20, 'SPIDER MAN2', 'bijou', '2'),
(21, 'AMAZONES', 'Moi', '5'),
(22, 'AMAZONES', 'clarisse', '5');

-- --------------------------------------------------------

--
-- Structure de la table `utilisateur`
--

CREATE TABLE `utilisateur` (
  `Id_util` int(45) NOT NULL,
  `Nom_util` varchar(45) NOT NULL,
  `Prenom_util` varchar(45) NOT NULL,
  `Age_util` varchar(45) NOT NULL,
  `Email_util` varchar(45) NOT NULL,
  `Password_util` varchar(100) NOT NULL,
  `Role` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `utilisateur`
--

INSERT INTO `utilisateur` (`Id_util`, `Nom_util`, `Prenom_util`, `Age_util`, `Email_util`, `Password_util`, `Role`) VALUES
(2, 'Armel', 'Motinye', '40', 'armo@gmail.com', '12356', 'Utilisateur'),
(5, 'Bijou', 'tresor', '35', 'clar@test.com', '12345', 'Admin'),
(7, 'Math', 'tresor', '35', 'def@test.com', '12345', 'Admin'),
(10, 'Math', 'tresor', '35', 'ef@test.com', '12345', 'Admin'),
(12, 'Bijou', 'Bijouta', '55', 'bijou@.com', '1234', 'admin');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `evenement`
--
ALTER TABLE `evenement`
  ADD PRIMARY KEY (`Id_event`);

--
-- Index pour la table `paie`
--
ALTER TABLE `paie`
  ADD PRIMARY KEY (`Id_paie`);

--
-- Index pour la table `reservation`
--
ALTER TABLE `reservation`
  ADD PRIMARY KEY (`Id_reserv`);

--
-- Index pour la table `utilisateur`
--
ALTER TABLE `utilisateur`
  ADD PRIMARY KEY (`Id_util`),
  ADD UNIQUE KEY `Email_util` (`Email_util`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `evenement`
--
ALTER TABLE `evenement`
  MODIFY `Id_event` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT pour la table `paie`
--
ALTER TABLE `paie`
  MODIFY `Id_paie` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `reservation`
--
ALTER TABLE `reservation`
  MODIFY `Id_reserv` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT pour la table `utilisateur`
--
ALTER TABLE `utilisateur`
  MODIFY `Id_util` int(45) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
