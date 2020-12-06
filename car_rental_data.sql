DROP DATABASE IF EXISTS car_rental_database;
CREATE DATABASE car_rental_database;
USE car_rental_database;

/* Customer table associated to the customer class in the spring boot project*/
/* the customer id is auto incremented and while inserting an object the id is not specified it's added by the database */
/* The type are the same as the attribute types in the spring boot project*/

CREATE TABLE Customer (
  customerid int NOT NULL AUTO_INCREMENT,
  username varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  firstname varchar(50) NOT NULL,
  lastname varchar(50) NOT NULL,
  phone varchar(50) DEFAULT NULL,
  email varchar(50) DEFAULT NULL,
  country varchar(50) NOT NULL,
  city varchar(50) NOT NULL,
  province varchar(50) NOT NULL,
  postal varchar(50) NOT NULL,
  activation BOOLEAN,
  PRIMARY KEY (customerid)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO Customer(username,`password`,firstname,lastname,phone,email,country,city,province,postal,activation) VALUES ('babara86','12333333','Babara','MacCaffrey','781-932-9754','babara86@gmail.com','canada','Montreal','QC','HQ11',false);
INSERT INTO Customer(username,`password`,firstname,lastname,phone,email,country,city,province,postal,activation) VALUES ('Ines0413','456789','Ines','Brushfield','804-427-9456','Ines0413@gmail.com','canada','Toronto','ON','HQ11',false);
INSERT INTO Customer(username,`password`,firstname,lastname,phone,email,country,city,province,postal,activation) VALUES ('freddiddi','000000','Freddi','Boagey','719-724-7869','freddiddi@outlook.com','canada','Calgary','AB','HQ11',false);
INSERT INTO Customer(username,`password`,firstname,lastname,phone,email,country,city,province,postal,activation) VALUES ('Amburrrrrrr','a123123','Ambur','Roseburgh','407-231-8017','Amburrrrrrr@163.com','canada','Vancouver','BC','HQ11',false);
INSERT INTO Customer(username,`password`,firstname,lastname,phone,email,country,city,province,postal,activation) VALUES ('clemmie7373','999999','Clemmie','Betchley','489-734-7890','clemmie7373@yahoo.com','canada','Montreal','QC','HQ11',false);
INSERT INTO Customer(username,`password`,firstname,lastname,phone,email,country,city,province,postal,activation) VALUES ('twiddekkkkkk','a666666','Elka','Twiddell','312-480-8498','twiddekkkkkk@gamil.com','canada','Toronto','ON','HQ11',false);
INSERT INTO Customer(username,`password`,firstname,lastname,phone,email,country,city,province,postal,activation) VALUES ('dowsin1234','a456456','Ilene','Dowson','615-641-4759','dowsin1234@gmail.com','canada','Toronto','ON','HQ11',false);
INSERT INTO Customer(username,`password`,firstname,lastname,phone,email,country,city,province,postal,activation) VALUES ('naseeeeed56','0000000','Thacher','Naseby','941-527-3977','naseeeeed56@outlook.com','canada','Montreal','QC','HQ11',false);
INSERT INTO Customer(username,`password`,firstname,lastname,phone,email,country,city,province,postal,activation) VALUES ('romola1992','111222333','Romola','Rumgay','559-181-3744','romola1992@yahoo.com','canada','Vancouver','BC','HQ11',false);
INSERT INTO Customer(username,`password`,firstname,lastname,phone,email,country,city,province,postal,activation) VALUES ('mynettttt1969','b999888','Levy','Mynett','404-246-3370','mynettttt1969@gmail.com','canada','Calgary','AB','HQ11',false);



/* Employee table associated to the Employee class in the spring boot project*/
/* the Employee id is auto incremented and while inserting an object the id is not specified it's added by the database */
/* The type are the same as the attribute types in the spring boot project*/
/* the managers activation is true at the time of creation*/

CREATE TABLE Employee (
  employeeid int NOT NULL AUTO_INCREMENT,
  `password` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  position varchar(50) NOT NULL,
  email varchar(50) DEFAULT NULL,
  activation BOOLEAN,
  PRIMARY KEY (employeeid)
  
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO Employee(`password`,`name`,position,email,activation) VALUES ('101101101','Yovonnda','Finance','Yovonnda101@hotmail.com',false);
INSERT INTO Employee(`password`,`name`,position,email,activation) VALUES ('102102102','Ava','Finance','Nortunen102@hotmail.com',false);
INSERT INTO Employee(`password`,`name`,position,email,activation) VALUES ('103103103','Sayer','Staff','Sayer103@hotmail.com',false);
INSERT INTO Employee(`password`,`name`,position,email,activation) VALUES ('104104104','Mindy','Staff','Minday104@hotmail.com',false);
INSERT INTO Employee(`password`,`name`,position,email,activation) VALUES ('105105105','Keriann','Manager','Keriann105@hotmail.com',true);
INSERT INTO Employee(`password`,`name`,position,email,activation) VALUES ('201201201','Alaster','Staff','Alaster201@hotmail.com',false);
INSERT INTO Employee(`password`,`name`,position,email,activation) VALUES ('202202202','North','Staff','North202@hotmail.com',false);
INSERT INTO Employee(`password`,`name`,position,email,activation) VALUES ('203203203','Elladine','Manager','Elladine203@hotmail.com',true);
INSERT INTO Employee(`password`,`name`,position,email,activation) VALUES ('204204204','Nisse','Staff','Nisse204@hotmail.com',false);
INSERT INTO Employee(`password`,`name`,position,email,activation) VALUES ('301301301','Guthrey','Manager','Guthrey301@hotmail.com',true);
INSERT INTO Employee(`password`,`name`,position,email,activation) VALUES ('302302302','Kass','Staff','Kass302@hotmail.com',false);
INSERT INTO Employee(`password`,`name`,position,email,activation) VALUES ('303303303','Virge','Staff','Virge303@hotmail.com',false);
INSERT INTO Employee(`password`,`name`,position,email,activation) VALUES ('304304304','Mirilla','Staff','Mirilla@hotmail.com',false);


/* Car table associated to the Car class in the spring boot project*/
/* the Car id is auto incremented and while inserting an object the id is not specified it's added by the database */
/* The type are the same as the attribute types in the spring boot project*/
CREATE TABLE Car (
  carid int NOT NULL AUTO_INCREMENT,
  entrydate varchar (50) NOT NULL,
  kmdriven int NOT NULL,
  releaseyear int NOT NULL,
  condi varchar(50) NOT NULL,
  pricekm int NOT NULL,
  state BOOLEAN,
  brand varchar(50) NOT NULL,
  model varchar(50) NOT NULL,
  style VARCHAR(50) NOT NULL,
  priceday int NOT NULL,

  
  PRIMARY KEY (carid)
  
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO Car(entrydate,kmdriven,releaseyear,condi,pricekm,state,brand,model,style,priceday) VALUES ('2019-10-24',20,2019,'verygood',1,false,'Ford','Fiesta','fullsize',45);
INSERT INTO Car(entrydate,kmdriven,releaseyear,condi,pricekm,state,brand,model,style,priceday) VALUES ('2018-05-06',100,2017,'good',1,true,'Renault','Kadjar','standard',45);
INSERT INTO Car(entrydate,kmdriven,releaseyear,condi,pricekm,state,brand,model,style,priceday) VALUES ('2019-10-24',50,2019,'very good',1,true,'BMW','X5','standardsuv',52);
INSERT INTO Car(entrydate,kmdriven,releaseyear,condi,pricekm,state,brand,model,style,priceday) VALUES ('2018-12-09',200,2016,'good',1,false,'Peugeot','3008','premiumsuv',58);
INSERT INTO Car(entrydate,kmdriven,releaseyear,condi,pricekm,state,brand,model,style,priceday) VALUES ('2019-08-29',1000,2018,'good',1,false,'Citroen','C3','minivan',60);


/* Bill table associated to the Bill class in the spring boot project*/
/* the Bill id is auto incremented and while inserting an object the id is not specified it's added by the database */
/* The type are the same as the attribute types in the spring boot project*/
CREATE TABLE Bill (
  billid int NOT NULL AUTO_INCREMENT,
  carid int NOT NULL,
  customerid int NOT NULL,
  carbill int NOT NULL,
  startdate varchar(50) NOT NULL,
  enddate varchar(50) NOT NULL,
  cardinfo varchar(50) NOT NULL,
 


  
  PRIMARY KEY (billid)
  
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO Bill(carid,customerid,carbill,startdate,enddate,cardinfo) VALUES (2,1,230,'2020-11-20','2020-11-25','cardinfo1');
INSERT INTO Bill(carid,customerid,carbill,startdate,enddate,cardinfo) VALUES (3,2,410,'2020-11-19','2020-11-26','cardinfo2');

/* Report table associated to the Report class in the spring boot project*/
/* the Report id is auto incremented and while inserting an object the id is not specified it's added by the database */
/* The type are the same as the attribute types in the spring boot project*/
CREATE TABLE Report (
  reportid int NOT NULL AUTO_INCREMENT,
  reportdate varchar(50) NOT NULL,
  revenue int NOT NULL,
  durationreported varchar(50) NOT NULL,
 


  
  PRIMARY KEY (reportid)
  
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO Report(reportdate,revenue,durationreported) VALUES ('2020-11-20',1400,'2020-11-25');
INSERT INTO Report(reportdate,revenue,durationreported) VALUES ('2020-11-19',560,'2020-11-26');

