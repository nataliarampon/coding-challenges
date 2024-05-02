--- URI Online Judge SQL
--- Copyright URI Online Judge
--- www.urionlinejudge.com.br
--- Problem 2745

CREATE TABLE people (
  id INTEGER PRIMARY KEY,
  name CHARACTER VARYING (255),
  salary NUMERIC
);


INSERT INTO people(id, name, salary)
VALUES 
      (1, 'James M. Tabarez', 883),
      (2, 'Rafael T. Hendon', 4281),
      (3, 'Linda J. Gardner', 4437),
      (4, 'Nicholas J. Conn', 8011),
      (5, 'Karol A. Morales', 2508),
      (6, 'Lolita S. Graves', 8709);

/* All person with salaries higher than 3000 must pay 10% in taxes.
 * Show the people's name and their taxes with 2 decimal palces. */
 SELECT name, ROUND(0.1 * salary, 2) AS tax FROM people
  WHERE salary > 3000;
  
  /*  Execute this query to drop the tables */
  -- DROP TABLE people; --
