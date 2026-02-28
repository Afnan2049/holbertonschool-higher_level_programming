-- Creates the MySQL server user user_0d_1 with all privileges
-- Create user if it doesn't already exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grant all privileges on all databases and tables
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

