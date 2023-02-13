PRAGMA foreign_keys = off;
BEGIN TRANSACTION;


DROP TABLE IF EXISTS student;
CREATE TABLE student (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, name VARCHAR (32));


DROP TABLE IF EXISTS category;
CREATE TABLE category (id INTEGER PRIMARY KEY NOT NULL UNIQUE, name VARCHAR(32));


DROP TABLE IF EXISTS course;
CREATE TABLE course (id INTEGER PRIMARY KEY NOT NULL UNIQUE, name VARCHAR(32));


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;





