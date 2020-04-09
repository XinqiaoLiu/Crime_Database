-- MySQL dump 10.13  Distrib 8.0.19, for macos10.15 (x86_64)
--
-- Host: 127.0.0.1    Database: CS411
-- ------------------------------------------------------
-- Server version	8.0.19

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
-- Table structure for table `district_income1`
--

DROP TABLE IF EXISTS `district_income1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `district_income1` (
  `Rank` int DEFAULT NULL,
  `Neighborhood` text,
  `Population` text,
  `Home Value` text,
  `Median Income` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `district_income1`
--

LOCK TABLES `district_income1` WRITE;
/*!40000 ALTER TABLE `district_income1` DISABLE KEYS */;
INSERT INTO `district_income1` VALUES (1,'North Center','34,931','545,871','99,384'),(2,'Loop','32,384','331,150','98,220'),(3,'Lake View','97,804','373,419','88,165'),(4,'Lincoln Park','64,965','508,008','99,720'),(5,'Edison Park','11,128','345,364','98,327'),(6,'Lincoln Square','41,305','381,276','72,563'),(7,'Near North Side','83,049','434,335','97,802'),(8,'Logan Square','73,470','338,254','67,769'),(9,'Forest Glen','18,298','421,818','112,032'),(10,'West Town','84,995','407,865','81,403'),(11,'Albany Park','51,193','273,641','58,075'),(12,'Norwood Park','37,477','293,731','77,558'),(13,'Irving Park','55,070','291,907','62,620'),(14,'Jefferson Park','26,594','282,741','69,751'),(15,'Edgewater','48,951','241,938','51,873'),(16,'Near South Side','21,930','318,671','80,646'),(17,'Dunning','43,244','229,478','60,896'),(18,'Mount Greenwood','18,990','224,582','91,682'),(19,'Avondale','37,884','282,354','49,249'),(20,'West Ridge','73,660','235,196','54,223'),(21,'Beverly','20,831','289,660','99,102'),(22,'Pottage Park','64,285','248,275','59,222'),(23,'Hyde Park','24,100','272,248','56,899'),(24,'Montclare','12,903','197,208','52,361'),(25,'Bridgeport','32,495','270,989','46,467'),(26,'Uptown','55,359','205,151','47,665'),(27,'Hermosa','24,225','229,088','39,659'),(28,'North Park','18,562','282,400','62,644'),(29,'West Elsdon','19,771','164,933','53,245'),(30,'Belmont Cragin','77,859','204,209','46,654'),(31,'Rogers Park','53,183','195,897','38,837'),(32,'Clearing','24,934','174,810','61,588'),(33,'Brighton Park','44,212','168,703','39,500'),(34,'Garfield Ridge','35,441','197,874','69,182'),(35,'Near West Side','61,845','248,351','64,399'),(36,'West Lawn','33,314','161,496','52,390'),(37,'Kenwood','14,112','250,519','47,591'),(38,'Ashburn','43,133','159,289','66,956'),(39,'O\'hare','12,706','154,657','47,915'),(40,'South Lawndale','73,519','138,019','32,212'),(41,'Lower West Side','33,150','208,108','40,724'),(42,'Mckinley Park','16,026','199,955','43,639'),(43,'Morgan Park','23,647','186,465','69,655'),(44,'Gage Park','40,693','128,630','40,566'),(45,'Hegewisch','9,039','140,800','61,614'),(46,'Armour Square','13,391','221,250','27,790'),(47,'Archer Heights','13,239','187,340','46,363'),(48,'Humboldt Park','55,833','154,009','36,095'),(49,'Calumet Heights','13,240','152,919','49,176'),(50,'Douglas','19,514','145,570','39,212'),(51,'Washington Heights','26,845','130,192','49,725'),(52,'East Side','22,550','117,919','44,652'),(53,'Austin','97,012','149,598','36,124'),(54,'Grand Boulevard','22,603','158,817','36,187'),(55,'Avalon Park','9,638','159,970','45,242'),(56,'South Shore','47,197','167,563','26,786'),(57,'Chicago Lawn','53,841','124,714','34,909'),(58,'Oakland','5,180','157,000','35,228'),(59,'West Garfield Park','17,277','140,887','24,266'),(60,'Woodlawn','22,658','130,409','25,807'),(61,'East Garfield Park','20,100','150,056','27,141'),(62,'Auburn Gresham','45,607','115,671','32,470'),(63,'New City','41,153','110,614','32,588'),(64,'Roseland','42,306','111,072','39,535'),(65,'Chatham','30,760','100,130','35,343'),(66,'North Lawndale','35,417','126,400','26,510'),(67,'West Pullman','27,416','99,938','36,883'),(68,'South Chicago','27,113','101,252','32,122'),(69,'Grand Crossing','32,217','112,668','30,799'),(70,'Pullman','6,565','107,912','38,397'),(71,'South Deering','14,598','88,955','37,207'),(72,'Burnside','2,423','100,900','25,642'),(73,'West Englewood','30,662','90,438','30,441'),(74,'Fuller Park','2,348','109,700','22,962'),(75,'Washington Park','11,871','104,058','24,556'),(76,'Englewood','25,858','70,261','23,317'),(77,'Riverdale','7,361','24,186','15,894');
/*!40000 ALTER TABLE `district_income1` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-07 22:08:22
