--  a script that prepares a MySQL server for the project
CREATE DATATBASE IF NOT EXIST hbnb_dev_db;
CREATE USER IF NOT EXIST 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES 'hbnb_dev_db'.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON 'performance_schema'.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
