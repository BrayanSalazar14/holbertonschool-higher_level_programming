--  lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
INSERT INTO second_table(score, name) VALUES(18, "Aria");
INSERT INTO second_table(score, name) VALUES(12, "Aria");
SELECT score, name FROM second_table ORDER BY score DESC;