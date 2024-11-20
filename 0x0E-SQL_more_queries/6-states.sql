-- Creates the database hbtn_0d_usa and the table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use thedatabase
USE hbtn_0d_usa;
-- Create table
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE AUTO_INCREMENT NOT NULL, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
