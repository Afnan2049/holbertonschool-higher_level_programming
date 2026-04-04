-- Creates the table id_not_null with a default value for id
-- The table has an id (INT) with default value 1 and a name (VARCHAR(256))
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);

