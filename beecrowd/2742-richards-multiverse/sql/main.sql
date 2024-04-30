--- URI Online Judge SQL
--- Copyright URI Online Judge
--- www.urionlinejudge.com.br
--- Problem 2742

CREATE TABLE dimensions(
	id INTEGER PRIMARY KEY,
	name varchar(255)
);

CREATE TABLE life_registry(
	id INTEGER PRIMARY KEY,
	name VARCHAR(255),
	omega NUMERIC,
	dimensions_id INTEGER REFERENCES dimensions (id)
);


INSERT INTO dimensions(id, name)
VALUES 
      (1, 'C774'),
      (2, 'C784'),
      (3, 'C794'),
      (4, 'C824'),
      (5, 'C875');
      
INSERT INTO life_registry(id, name, omega, dimensions_id)
VALUES
	  (1, 'Richard Postman', 5.6, 2),	
	  (2, 'Simple Jelly', 1.4, 1),	
	  (3, 'Richard Gran Master', 2.5, 1),	
	  (4, 'Richard Turing', 6.4, 4),	
	  (5, 'Richard Strall',	1.0, 3);
  
  /* Show all possible Richards from dimensions C875 and C774, together with their probability of existing (N).
   * N = omega * 1,618, with 3 decimal places. Order by omega, in descending order */
  SELECT l.name AS name, ROUND(1.618*l.omega, 3) AS "Fator N" FROM life_registry l
    INNER JOIN dimensions d ON d.id = l.dimensions_id
    WHERE d.name IN ('C875', 'C774') AND l.name LIKE '%Richard%'
    ORDER BY "Fator N";

  /*  Execute this query to drop the tables */
  -- DROP TABLE life_registry, dimensions; --
