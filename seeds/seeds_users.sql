-- (file: spec/seeds_users.sql)

-- Write your SQL seed here. 

-- First, you'd need to truncate the table - this is so our table is emptied between each test run,
-- so we can start with a fresh state.
-- (RESTART IDENTITY resets the primary key)

DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS posts CASCADE;  -- This drops the dependent foreign key constraint as well


-- TRUNCATE TABLE posts CASCADE; -- This should drop dependent foreign key constraints
-- TRUNCATE TABLE users CASCADE;

-- -- Delete all rows from the dependent table first
-- DELETE FROM posts;
-- -- Delete all rows from the main table
-- DELETE FROM users;

-- Create the table without the foreign key first.
-- CREATE SEQUENCE IF NOT EXISTS users_id_sequence;(NOT REQUIRED BECAUSE WE'RE USING SERIAL?)
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email text,
    password text,
    name text,
    username text
);

-- Create the table with the foreign key second.
-- CREATE SEQUENCE IF NOT EXISTS posts_id_sequence; (NOT REQUIRED BECAUSE WE'RE USING SERIAL?)
CREATE TABLE IF NOT EXISTS posts (
    id SERIAL PRIMARY KEY,
    content text,
    time_post text,
    -- The foreign key name is always {other_table_singular}_id
    user_id int,
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);



-- Below this line there should only be `INSERT` statements.
-- Replace these statements with your own seed data.

INSERT INTO users (email, password, name, username) VALUES ('dod@hotmail.com', 'passass', 'Dave', 'DoD');
INSERT INTO users (email, password, name, username) VALUES ('dad@hotmail.com', 'passass123', 'Dad', 'Daddy');   

INSERT INTO posts (content, time_post, user_id) VALUES ('Just posting something for lols', '2024-02-02 00:00:00', 1);
INSERT INTO posts (content, time_post, user_id) VALUES ('This is my first post!','2024-02-02 00:00:02', 2);   