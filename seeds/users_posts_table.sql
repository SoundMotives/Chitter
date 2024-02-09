    -- file: seeds/users_posts_table.sql

-- Create the table without the foreign key first.
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email text,
    password text,
    name text,
    username text
);

-- Create the table with the foreign key second.
CREATE TABLE IF NOT EXISTS posts (
    id SERIAL PRIMARY KEY,
    content text,
    time_post TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    -- The foreign key name is always {other_table_singular}_id
    user_id int,
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
