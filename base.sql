--clear all tables

DROP TABLE books;
DROP TABLE authors;
DROP TABLE category;
DROP TABLE publisher;

--create new tables
CREATE TABLE IF NOT EXISTS authors (
	id INTEGER NOT NULL PRIMARY KEY,
	firstname VARCHAR NOT NULL,
	lastname VARCHAR NOT NULL);
CREATE TABLE IF NOT EXISTS category (
	id INTEGER NOT NULL PRIMARY KEY,
	title VARCHAR NOT NULL);
CREATE TABLE IF NOT EXISTS publisher (
	id INTEGER NOT NULL PRIMARY KEY,
	title VARCHAR NOT NULL);
CREATE TABLE IF NOT EXISTS books (
	id INTEGER NOT NULL PRIMARY KEY,
	title VARCHAR NOT NULL,
	author INTEGER NOT NULL REFERENCES authors (id),
	category INTEGER NOT NULL REFERENCES category (id) DEFAULT 0,
	description VARCHAR,
	publisher INTEGER NOT NULL REFERENCES publisher (id) DEFAULT 0,
	rating FLOAT NOT NULL DEFAULT 0.0,
	votes INTEGER default 0);

--insert default values
INSERT INTO authors(id, firstname, lastname) VALUES (0, 'ND', 'ND');
INSERT INTO category(id, title) VALUES (0, 'ND');
INSERT INTO publisher(id, title) VALUES (0, 'ND');