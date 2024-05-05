--- URI Online Judge SQL
--- Copyright URI Online Judge
--- www.urionlinejudge.com.br
--- Problem 3001

CREATE TABLE products (
id numeric PRIMARY KEY,
name varchar(50),
type char,
price numeric
);

GRANT SELECT ON products TO sql_user;

INSERT INTO products (id , name, type, price)
VALUES
(1, 'Monitor',  'B', 0),
(2, 'Headset',  'A', 0),
(3, 'PC Case',  'A', 0),
(4, 'Computer Desk', 'C', 0),
(5, 'Gaming Chair', 'C', 0),
(6, 'Mouse',  'A', 0);

/* Given that for type A, price is 20.0; for type B, price is 70.0; and for type C, price is 530.5.ABORT
 * Show product name and price, ordered by product type ascending and then by product ID descending. */
SELECT name, CASE
    WHEN type = 'A' THEN 20.0
    WHEN type = 'B' THEN 70.0
    ELSE 530.5
  END AS price
  FROM products
  ORDER BY price ASC, id DESC;

/*  Execute this query to drop the tables */
-- DROP TABLE products;