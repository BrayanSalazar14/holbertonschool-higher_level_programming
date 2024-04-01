-- creates the table unique_id on your MySQL server.
CREATE TABLE IF NOT EXISTS unique_id(
    id INTEGER,
    name VARCHAR(256),
    UNIQUE(id)
);