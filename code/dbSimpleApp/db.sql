/*
id,line
*/
DROP TABLE IF EXISTS lines;

CREATE TABLE IF NOT EXISTS lines 
(   id INTEGER PRIMARY KEY,
    line TEXT,
    modiffied TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);