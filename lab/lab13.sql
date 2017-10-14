.read sp17data.sql
.read su17data.sql

CREATE TABLE obedience AS
  select seven, image from students;

CREATE TABLE smallest_int AS
  select time, smallest from students where smallest > 5 order by smallest limit 20;

CREATE TABLE greatstudents AS
  select a.date, a.color, a.pet, a.number, b.number from students as a, sp17students as b where a.date = b.date and a.color = b.color and a.pet = b.pet;

CREATE TABLE sevens AS
  select seven from students as a, checkboxes as b where a.time = b.time and number = 7 and "7" = "True";

CREATE TABLE matchmaker AS
  select a.pet, a.beets, a.color, b.color from students as a, students as b where a.time < b.time and a.pet = b.pet and a.beets = b.beets;
