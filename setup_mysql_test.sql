-- create the database if it doesn't exists
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;

-- creating the new_user if it doesn't exist which will be identified by `hbnb_test_pwd`
CREATE USER IF NOT EXISTS 'hbnb_test_db'@'localhost' By `hbnb_test_pwd`;


-- granting all privileges on our database to user `hbnb_test_db`
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test_db'@'localhost';


-- grant selecting privilege our user `hbnb_test_db`
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test_db'@'localhost';


-- apply the changes
FLUSH PRIVILEGES;