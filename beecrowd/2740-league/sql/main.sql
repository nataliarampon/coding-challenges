--- URI Online Judge SQL
--- Copyright URI Online Judge
--- www.urionlinejudge.com.br
--- Problem 2740

CREATE TABLE league(
  position INTEGER,
  team CHARACTER VARYING (255)
);


INSERT INTO league(position, team)
VALUES (1, 'The Quack Bats'),
       (2, 'The Responsible Hornets'),
       (3, 'The Bawdy Dolphins'),
       (4, 'The Abstracted Sharks'),
       (5, 'The Nervous Zebras'),
       (6, 'The Oafish Owls'),
       (7, 'The Unequaled Bison'),
       (8, 'The Keen Kangaroos'),
       (9, 'The Left Nightingales'),
       (10, 'The Terrific Elks'),
       (11, 'The Lumpy Frogs'),
       (12, 'The Swift Buffalo'),
       (13, 'The Big Chargers'),
       (14, 'The Rough Robins'),
       (15, 'The Silver Crocs');

  /* Show the three best ranked teams prepended by "Podium: " and the worst two prepended by "Demoted: " */
  (SELECT 'Podium: ' || team as name FROM league
    ORDER BY position ASC
    LIMIT 3)
  
  UNION ALL

  (SELECT 'Demoted: ' || team as name FROM league
    WHERE position > (SELECT MAX(position) - 2 FROM league));


  /*  Execute this query to drop the tables */
  -- DROP TABLE league; --
