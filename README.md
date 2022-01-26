## Usage

1. Update the mysql credential and database name in main.py
2. For runing this code, you can run with 
 ```
 python3 -m uvicorn main:app --reload
 ```

 or 
 ```
 python3 main.py
 ```

## DB

~~~~sql

CREATE TABLE `movies` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  `description` text NOT NULL,
  `rating` int(11) DEFAULT '0',
  `playing_date` datetime NOT NULL,
  `created_date` datetime NOT NULL,
  `last_updated` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

~~~~