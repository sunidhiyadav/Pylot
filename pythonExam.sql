-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: pythonexamdb
-- ------------------------------------------------------
-- Server version	5.7.10

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `friendlists`
--

DROP TABLE IF EXISTS `friendlists`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `friendlists` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `friend_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_friendLists_users_idx` (`user_id`),
  KEY `fk_friendLists_friends_idx` (`friend_id`),
  CONSTRAINT `fk_friendLists_friends` FOREIGN KEY (`friend_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_friendLists_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `friendlists`
--

LOCK TABLES `friendlists` WRITE;
/*!40000 ALTER TABLE `friendlists` DISABLE KEYS */;
INSERT INTO `friendlists` VALUES (40,4,1),(41,1,4),(42,1,2),(43,2,1),(44,1,7),(45,7,1);
/*!40000 ALTER TABLE `friendlists` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `alias` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `dob` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Sunidhi','Yadav','syadav','sunidhi@yadav.com','$2b$12$uuAwVZSv9T5tiAbuA5daxO2b/kscIzB17zPcmWRs.rRLmTysBHJli','2016-09-25 14:32:14','2016-09-25 14:32:14',NULL),(2,'Test','Test','TT','test@test.com','$2b$12$y9PKVjrTKJ7oRFPeE.xwNufjtgjxKM9wvUMGu2re9VG1WTgQ8bUqG','2016-09-25 15:24:44','2016-09-26 08:14:55',NULL),(4,'Antara','Sri','Pikki','antara@sri.com','$2b$12$EDWviXmNmV11xERtP3mEZOtOseUXbQt5R6.CgU8OeHXEDM1Gj8ck6','2016-09-26 09:57:49','2016-09-26 09:57:49',NULL),(5,'Abcd','Abcd','abcd','abcd@abcd.com','$2b$12$y.Jqnx9M6z1cam6Vmu9tCuo4SlDzsFreTXUhVeZOWl/uMeYmiBLwu','2016-09-26 09:58:23','2016-09-26 09:58:23',NULL),(6,'Gracee','Li','Grace','grace@li.com','$2b$12$oIyZhvZAKq.6KQ33xoxxCeW/LpNG3xwt93OL7sUaFLHQkqMRBxaAC','2016-09-26 11:53:56','2016-09-26 11:53:56',NULL),(7,'Mark','Spencer','Mark','mark@spencer.com','$2b$12$4MsSlSKMA/AeEkMSlWZBdu7jQlGjwPBBAqFM3gp.NFtjev1DHOxqa','2016-09-26 12:44:32','2016-09-26 12:44:32','2016-09-13');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-09-26 13:28:02
