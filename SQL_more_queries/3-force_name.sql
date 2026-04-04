-- Creates the table force_name on the MySQL server
-- The table has an id (INT) and a name (VARCHAR(256)) that cannot be null
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);

