-- Creates the database hbtn_0d_usa and the table states
-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use the database
USE hbtn_0d_usa;
-- Create the table if it doesn't exist
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

