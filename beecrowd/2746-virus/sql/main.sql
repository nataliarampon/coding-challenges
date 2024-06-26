--- URI Online Judge SQL
--- Copyright URI Online Judge
--- www.urionlinejudge.com.br
--- Problem 2746

CREATE TABLE virus (
  id INTEGER,
  name VARCHAR(255)
);


INSERT INTO virus(id, name)
VALUES 
      (1, 'H1RT'),
      (2, 'H7H1'),
      (3, 'HUN8'),
      (4, 'XH1HX'),
      (5, 'XXXX');

/* Show all virus names replacing the substring 'H1' with 'X' */
SELECT REPLACE(name, 'H1', 'X') as name FROM virus;
  
  /*  Execute this query to drop the tables */
  -- DROP TABLE virus; --
