-- creating database if not exists
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;

-- creating the new user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' BY `hbnb_dev_pwd`;

-- granting  all access to our database hbnbdev_db
GRANT ALL PRIVILEGES ON `hbnb_dv_db`.* TO 'hbnb_dev_db'@'localhost';

-- granting select privileges 
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev_db'@'localhost';

FLUSH PRIVILEGES;