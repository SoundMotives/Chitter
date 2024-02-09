-- (file: spec/seeds_users.sql)

-- Write your SQL seed here. 

-- First, you'd need to truncate the table - this is so our table is emptied between each test run,
-- so we can start with a fresh state.
-- (RESTART IDENTITY resets the primary key)

TRUNCATE TABLE users RESTART IDENTITY; -- replace with your own table name.
TRUNCATE TABLE posts RESTART IDENTITY; -- replace with your own table name.

-- Below this line there should only be `INSERT` statements.
-- Replace these statements with your own seed data.

INSERT INTO users (email, password, name, username) VALUES ('dod@hotmail.com', 'passass', 'Dave', 'DoD');
INSERT INTO users (email, password, name, username) VALUES ('dad@hotmail.com', 'passass123', 'Dad', 'Daddy');   

INSERT INTO posts (content, user_id) VALUES ('Just posting something for lols', 1);
INSERT INTO posts (content, user_id) VALUES ('This is my first post!', 2);   