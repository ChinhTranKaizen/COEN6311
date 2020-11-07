DROP DATABASE IF EXISTS `carsys_database`;
CREATE DATABASE `carsys_database`;
USE `carsys_database`;

CREATE TABLE `customers` (
  `customer_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `birth_date` date DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `city` varchar(50) NOT NULL,
  `province` varchar(50) NOT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO `customers` VALUES (1,'babara86','12333333','Babara','MacCaffrey','1986-03-28','781-932-9754','babara86@gmail.com','Montreal','QC');
INSERT INTO `customers` VALUES (2,'Ines0413','456789','Ines','Brushfield','1986-04-13','804-427-9456','Ines0413@gmail.com','Toronto','ON');
INSERT INTO `customers` VALUES (3,'freddiddi','000000','Freddi','Boagey','1985-02-07','719-724-7869','freddiddi@outlook.com','Calgary','AB');
INSERT INTO `customers` VALUES (4,'Amburrrrrrr','a123123','Ambur','Roseburgh','1974-04-14','407-231-8017','Amburrrrrrr@163.com','Vancouver','BC');
INSERT INTO `customers` VALUES (5,'clemmie7373','999999','Clemmie','Betchley','1973-11-07','489-734-7890','clemmie7373@yahoo.com','Montreal','QC');
INSERT INTO `customers` VALUES (6,'twiddekkkkkk','a666666','Elka','Twiddell','1991-09-04','312-480-8498','twiddekkkkkk@gamil.com','Toronto','ON');
INSERT INTO `customers` VALUES (7,'dowsin1234','a456456','Ilene','Dowson','1964-08-30','615-641-4759','dowsin1234@gmail.com','Toronto','ON');
INSERT INTO `customers` VALUES (8,'naseeeeed56','0000000','Thacher','Naseby','1993-07-17','941-527-3977','naseeeeed56@outlook.com','Montreal','QC');
INSERT INTO `customers` VALUES (9,'romola1992','111222333','Romola','Rumgay','1992-05-23','559-181-3744','romola1992@yahoo.com','Vancouver','BC');
INSERT INTO `customers` VALUES (10,'mynettttt1969','b999888','Levy','Mynett','1969-10-13','404-246-3370','mynettttt1969@gmail.com','Calgary','AB');




CREATE TABLE `employees` (
  `employee_id` int(11) NOT NULL,
  `password` varchar(50) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `job_title` varchar(50) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`employee_id`)
  
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO `employees` VALUES (101,'101101101','Yovonnda','Magrannell','Executive Secretary','Yovonnda101@hotmail.com');
INSERT INTO `employees` VALUES (102,'102102102','Ava','Nortunen','technical maintainer','Nortunen102@hotmail.com');
INSERT INTO `employees` VALUES (103,'103103103','Sayer','Matterson','Staff','Sayer103@hotmail.com');
INSERT INTO `employees` VALUES (104,'104104104','Mindy','Crissil','Staff','Minday104@hotmail.com');
INSERT INTO `employees` VALUES (105,'105105105','Keriann','Alloisi','manager','Keriann105@hotmail.com');
INSERT INTO `employees` VALUES (201,'201201201','Alaster','Scutchin','Staff','Alaster201@hotmail.com');
INSERT INTO `employees` VALUES (202,'202202202','North','de Clerc','Staff','North202@hotmail.com');
INSERT INTO `employees` VALUES (203,'203203203','Elladine','Rising','manager','Elladine203@hotmail.com');
INSERT INTO `employees` VALUES (204,'204204204','Nisse','Voysey','technical maintainer','Nisse204@hotmail.com');
INSERT INTO `employees` VALUES (301,'301301301','Guthrey','Iacopetti','Executive Secretary','Guthrey301@hotmail.com');
INSERT INTO `employees` VALUES (302,'302302302','Kass','Hefferan','Staff','Kass302@hotmail.com');
INSERT INTO `employees` VALUES (303,'303303303','Virge','Goodrum','Staff','Virge303@hotmail.com');
INSERT INTO `employees` VALUES (304,'304304304','Mirilla','Janowski','technical maintainer','Mirilla@hotmail.com');
