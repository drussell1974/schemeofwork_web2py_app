CREATE USER IF NOT EXISTS 'drussell1974'@'%' IDENTIFIED BY 'password1.';
GRANT ALL PRIVILEGES ON cssow_api.* TO 'drussell1974'@'%';
SELECT User, Host, password_expired FROM mysql.user WHERE User = 'drussell1974';
CREATE DATABASE IF NOT EXISTS cssow_api;
