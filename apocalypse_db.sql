CREATE DATABASE  IF NOT EXISTS `apocalypse` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `apocalypse`;
-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: apocalypse
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `daily_current_ladder`
--

DROP TABLE IF EXISTS `daily_current_ladder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `daily_current_ladder` (
  `user_nickname` varchar(15) NOT NULL,
  `user_max_daily_points` int NOT NULL,
  KEY `user_nickname` (`user_nickname`),
  CONSTRAINT `daily_current_ladder_ibfk_1` FOREIGN KEY (`user_nickname`) REFERENCES `players` (`nickname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `daily_current_ladder`
--

LOCK TABLES `daily_current_ladder` WRITE;
/*!40000 ALTER TABLE `daily_current_ladder` DISABLE KEYS */;
INSERT INTO `daily_current_ladder` VALUES ('Ds',0);
/*!40000 ALTER TABLE `daily_current_ladder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `daily_past_ladder`
--

DROP TABLE IF EXISTS `daily_past_ladder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `daily_past_ladder` (
  `user_nickname` varchar(15) NOT NULL,
  `user_past_daily_points` int NOT NULL,
  KEY `user_nickname` (`user_nickname`),
  CONSTRAINT `daily_past_ladder_ibfk_1` FOREIGN KEY (`user_nickname`) REFERENCES `players` (`nickname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `daily_past_ladder`
--

LOCK TABLES `daily_past_ladder` WRITE;
/*!40000 ALTER TABLE `daily_past_ladder` DISABLE KEYS */;
INSERT INTO `daily_past_ladder` VALUES ('Ds',0);
/*!40000 ALTER TABLE `daily_past_ladder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory` (
  `user_nickname` varchar(15) NOT NULL,
  `space_ship1` tinyint(1) DEFAULT '1',
  `space_ship2` tinyint(1) NOT NULL,
  `space_ship3` tinyint(1) NOT NULL,
  KEY `user_nickname` (`user_nickname`),
  CONSTRAINT `inventory_ibfk_1` FOREIGN KEY (`user_nickname`) REFERENCES `players` (`nickname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES ('Ds',1,1,0);
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `monthly_current_ladder`
--

DROP TABLE IF EXISTS `monthly_current_ladder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `monthly_current_ladder` (
  `user_nickname` varchar(15) NOT NULL,
  `user_max_monthly_points` int NOT NULL,
  KEY `user_nickname` (`user_nickname`),
  CONSTRAINT `monthly_current_ladder_ibfk_1` FOREIGN KEY (`user_nickname`) REFERENCES `players` (`nickname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `monthly_current_ladder`
--

LOCK TABLES `monthly_current_ladder` WRITE;
/*!40000 ALTER TABLE `monthly_current_ladder` DISABLE KEYS */;
INSERT INTO `monthly_current_ladder` VALUES ('Ds',0);
/*!40000 ALTER TABLE `monthly_current_ladder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `monthly_past_ladder`
--

DROP TABLE IF EXISTS `monthly_past_ladder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `monthly_past_ladder` (
  `user_nickname` varchar(15) NOT NULL,
  `user_past_monthly_points` int NOT NULL,
  KEY `user_nickname` (`user_nickname`),
  CONSTRAINT `monthly_past_ladder_ibfk_1` FOREIGN KEY (`user_nickname`) REFERENCES `players` (`nickname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `monthly_past_ladder`
--

LOCK TABLES `monthly_past_ladder` WRITE;
/*!40000 ALTER TABLE `monthly_past_ladder` DISABLE KEYS */;
INSERT INTO `monthly_past_ladder` VALUES ('Ds',0);
/*!40000 ALTER TABLE `monthly_past_ladder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `players`
--

DROP TABLE IF EXISTS `players`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `players` (
  `nickname` varchar(15) NOT NULL,
  `login` varchar(15) NOT NULL,
  `user_password` varchar(15) NOT NULL,
  PRIMARY KEY (`nickname`),
  UNIQUE KEY `login` (`login`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `players`
--

LOCK TABLES `players` WRITE;
/*!40000 ALTER TABLE `players` DISABLE KEYS */;
INSERT INTO `players` VALUES ('Ds','popiks711','dima200327');
/*!40000 ALTER TABLE `players` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `statistics`
--

DROP TABLE IF EXISTS `statistics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `statistics` (
  `user_nickname` varchar(20) NOT NULL,
  `max_points` int NOT NULL,
  `total_points` int NOT NULL,
  `games_played` int NOT NULL,
  `max_daily_points` int NOT NULL,
  `max_weekly_points` int NOT NULL,
  `max_monthly_points` int NOT NULL,
  KEY `user_nickname` (`user_nickname`),
  CONSTRAINT `statistics_ibfk_1` FOREIGN KEY (`user_nickname`) REFERENCES `players` (`nickname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `statistics`
--

LOCK TABLES `statistics` WRITE;
/*!40000 ALTER TABLE `statistics` DISABLE KEYS */;
INSERT INTO `statistics` VALUES ('Ds',396,749,9,396,396,396);
/*!40000 ALTER TABLE `statistics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `weekly_current_ladder`
--

DROP TABLE IF EXISTS `weekly_current_ladder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `weekly_current_ladder` (
  `user_nickname` varchar(15) NOT NULL,
  `user_max_weekly_points` int NOT NULL,
  KEY `user_nickname` (`user_nickname`),
  CONSTRAINT `weekly_current_ladder_ibfk_1` FOREIGN KEY (`user_nickname`) REFERENCES `players` (`nickname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `weekly_current_ladder`
--

LOCK TABLES `weekly_current_ladder` WRITE;
/*!40000 ALTER TABLE `weekly_current_ladder` DISABLE KEYS */;
INSERT INTO `weekly_current_ladder` VALUES ('Ds',0);
/*!40000 ALTER TABLE `weekly_current_ladder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `weekly_past_ladder`
--

DROP TABLE IF EXISTS `weekly_past_ladder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `weekly_past_ladder` (
  `user_nickname` varchar(15) NOT NULL,
  `user_past_weekly_points` int NOT NULL,
  KEY `user_nickname` (`user_nickname`),
  CONSTRAINT `weekly_past_ladder_ibfk_1` FOREIGN KEY (`user_nickname`) REFERENCES `players` (`nickname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `weekly_past_ladder`
--

LOCK TABLES `weekly_past_ladder` WRITE;
/*!40000 ALTER TABLE `weekly_past_ladder` DISABLE KEYS */;
INSERT INTO `weekly_past_ladder` VALUES ('Ds',0);
/*!40000 ALTER TABLE `weekly_past_ladder` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-29  2:42:04
