create database music_streaming_app;
use music_streaming_app;
create table playlists (playlist_id int primary key
, name varchar(30),
created_by varchar(30));
insert into playlists values (1,'amit','Bollywood Hits'),
(2,"neha",'Chill Vibes'),
(3,'daksh','Workout Mix');
select name, created_by  from playlists
where name="amit";

/*
Example: Food Delivery App (Zomato)

In a food delivery app like Zomato, SQL databases store information about restaurants, users, orders, and food items.

Let's understand Table, Row, and Column using a simple example.

1. Table

A table is a collection of related data organized into rows and columns.

Example: A Restaurants table stores information about restaurants available on Zomato.

2. Column

A column represents a specific attribute or field of data.

In the Restaurants table:

Restaurant_ID → Unique restaurant identification
Name → Restaurant name
Location → Restaurant location
Rating → Restaurant rating
3. Row

A row represents a single record or entry in a table.

For example, information about one restaurant is stored in one row.

Example: Restaurants Table
Restaurant_ID	Name	Location	Rating
101	Domino's	Ahmedabad	4.5
102	Honest	Vadodara	4.2
103	Swiggy Cafe	Surat	4.0
Explanation
Table: The entire Restaurants table containing all restaurant information.
Column: Name contains restaurant names such as Domino's, Honest, and Swiggy Cafe.
Row: The first row contains information about Domino's.
SQL Example
CREATE TABLE Restaurants (
    Restaurant_ID INT,
    Name VARCHAR(50),
    Location VARCHAR(50),
    Rating DECIMAL(2,1)
);

Output: A table named Restaurants is created with four columns.

Key Differences
Feature	          Table	                   Column	          Row
Meaning	          Collection of data	Attribute/field	     Single record
Direction	       Contains rows and columns	Vertical	    Horizontal
Example	           Restaurants	                  Name	      Domino's record
Purpose	           Stores related data	Defines data type	Stores one entry