--- prepares a MySQL server for the project---
--Create the database if it doesn't exist---
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
---Create the user if it doesn't exit---
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
---Grant all privileges on the databse to the user---
GRANT ALL PRIVILEGE ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
---Grant SELECT privilege on the schema database to the user---
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';