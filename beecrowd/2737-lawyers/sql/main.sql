--- URI Online Judge SQL
--- Copyright URI Online Judge
--- www.urionlinejudge.com.br
--- Problem 2737

CREATE TABLE lawyers(
  register INTEGER PRIMARY KEY,
  name VARCHAR(255),
  customers_number INTEGER
 );
  
  
 INSERT INTO lawyers(register, name, customers_number)
 VALUES (1648, 'Marty M. Harrison', 5),
	(2427, 'Jonathan J. Blevins', 15),
	(3365, 'Chelsey D. Sanders', 20),
	(4153, 'Dorothy W. Ford', 16),
	(5525, 'Penny J. Cormier', 6);

/* Show the name and number of customers of the lawyer with the most customers, 
 * the one with the least customers, and the average number of customers.
 * The average should be shown after a field named 'Average', as an integer. */

 /* ATTENTION!! Need to remove SELECT * FROM in the submission, as it's a syntax
  * difference between SQLite and PostgreSQL */

 SELECT * FROM 
 (SELECT name, customers_number FROM lawyers 
  WHERE customers_number = (SELECT MAX(customers_number) FROM lawyers)
  OR customers_number = (SELECT MIN(customers_number) FROM lawyers)
  ORDER BY customers_number DESC)

 UNION ALL

 SELECT 'Average', ROUND(AVG(customers_number), 0) FROM lawyers;
  
  /*  Execute this query to drop the tables */
  -- DROP TABLE lawyers; --
