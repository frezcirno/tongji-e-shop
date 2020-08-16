-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: webhw
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
-- Dumping data for table `cart`
--

LOCK TABLES `cart` WRITE;
/*!40000 ALTER TABLE `cart` DISABLE KEYS */;
INSERT INTO `cart` VALUES (1,1,1,1);
/*!40000 ALTER TABLE `cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `image`
--

LOCK TABLES `image` WRITE;
/*!40000 ALTER TABLE `image` DISABLE KEYS */;
/*!40000 ALTER TABLE `image` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `item`
--

LOCK TABLES `item` WRITE;
/*!40000 ALTER TABLE `item` DISABLE KEYS */;
INSERT INTO `item` VALUES (1,'同济纪念品纯棉卫衣红色',159,'1.png','暖暖的很贴心','2020-08-16 16:15:10'),(2,'花瓶',99,'100.png','我是个花瓶','2020-08-16 16:15:16'),(3,'同济围脖蓝色',59,'12.jpg','暖暖的很贴心','2020-08-16 16:15:26'),(4,'同济明信片西游记主题',13,'13.jpg','同济大学纪念品原创文艺手绘','2020-08-16 16:15:44'),(5,'同济大学出版社大学德语四级应试全攻略',35,'15.png','少年学德语吗','2020-08-16 16:16:05'),(6,'国立同济大学T恤简洁',59,'3.png','暖暖的很贴心','2020-08-16 16:16:29'),(7,'同济1907帆布袋蓝色加厚',20,'5.png','必备帆布袋','2020-08-16 16:16:50'),(8,'同济主题雨伞红色大号',45,'6.png','为你遮风挡雨','2020-08-16 16:17:09'),(9,'同济2018戊戌徽章',30,'7.png','纪念礼品校徽樱花季徽章礼盒胸针配饰logo','2020-08-16 16:17:24'),(10,'同济诗歌主题明信片大漠沙如雪',10,'9.jpg','同济大学纪念品原创文艺手绘','2020-08-16 16:17:47'),(11,'同济作业本小号',2,'bjb.jpg','物美价廉轻松笔记本办公用品','2020-08-16 16:17:55'),(12,'东方明珠木质模型小号',35,'dfmz.jpg','上海浦东特色旅游纪念礼品','2020-08-16 16:18:08'),(13,'同济帆布袋典雅白色',20,'fbd.jpg','樱花图书馆','2020-08-16 16:18:26'),(14,'同济明信片',5,'gwjd.jpg','同济大学纪念品原创文艺手绘','2020-08-16 16:18:37'),(15,'同济四季猫主题明信片',30,'mtj.jpg','同济大学纪念品四季猫原创文艺手绘','2020-08-16 16:18:56'),(16,'同济大学木质拼插模型',55,'mzpc.jpg','把学校带回家吧','2020-08-16 16:19:11'),(17,'同济食堂特供红烧大排',2.5,'tjdp.jpg','好吃','2020-08-16 16:19:31'),(18,'同济食堂特供铜火锅',60,'tjhg.jpg','温暖冬日','2020-08-16 16:19:46'),(19,'同济食堂特供中西面点',7.5,'tjmd.jpg','好吃','2020-08-16 16:20:05'),(20,'同济食堂特质打卤面条',8,'tjmt.jpg','emmm','2020-08-16 16:20:29'),(21,'同济青团豆沙馅',5,'tjqt.jpg','好吃','2020-08-16 16:20:43'),(22,'同济青团肉松馅',8,'tjqt2.jpg','好吃','2020-08-16 16:20:52'),(23,'同济大排档-小龙虾',30,'tjxlx.jpg','好吃','2020-08-16 16:21:15'),(24,'同济食堂特供月饼五仁',4,'tjyb.jpg','好吃','2020-08-16 16:21:30'),(25,'同济食堂特供鲜肉月饼',8,'tjyb2.jpg','一般','2020-08-16 16:21:42'),(26,'同济食堂特供樱花饼',3.5,'tjyhb.jpg','好吃','2020-08-16 16:21:56'),(27,'同济校徽徽章纪念品',30,'xz.jpg','纪念礼品校徽樱花季徽章礼盒胸针配饰logo','2020-08-16 16:22:17'),(28,'同济立体纸雕明信片',23.6,'zd.jpg','把学校带回家吧','2020-08-16 16:22:44');
/*!40000 ALTER TABLE `item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `order`
--

LOCK TABLES `order` WRITE;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
/*!40000 ALTER TABLE `order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `order_item`
--

LOCK TABLES `order_item` WRITE;
/*!40000 ALTER TABLE `order_item` DISABLE KEYS */;
/*!40000 ALTER TABLE `order_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'frezcirno','2277861660@qq.com',NULL,'123456','2020-08-16 14:30:50','http://www.2cto.com/uploadfile/2014/0321/20140321081401358.jpg');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-16 21:20:48
