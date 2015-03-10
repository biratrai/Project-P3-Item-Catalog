-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Drop Database if already present
DROP DATABASE tournament;

-- Create Database 'Tournament'
CREATE DATABASE tournament;

--DROP TABLE IF EXISTS players CASCADE; -- Drop table players if exists
--DROP TABLE IF EXISTS scores CASCADE;  -- Drop tbale scores if exists

-- Creating Connection to the database
\connect tournament

-- Create Player Table
CREATE TABLE players(
   player_id smallserial PRIMARY KEY, -- Declaring a self incrementing unique id 
   player_name varchar(255) NOT NULL  -- Declaring varchar which must not be null
   
);

-- Create Scores Table
CREATE TABLE scores(
	match_id smallserial PRIMARY KEY, -- Declaring a self incrementing unique id 
	winner_id INT ,  -- The winning id of the player
	loser_id INT ,  -- The losing id of the player
	FOREIGN KEY (winner_id) references players(player_id), -- Declaring Foreign Key relationship
	FOREIGN KEY (loser_id) references players(player_id) -- Declaring Foreign Key relationship
);

-- Create View Wins which has count of wins of a player
CREATE VIEW Wins AS 
	select players.player_id, players.player_name, count(scores.winner_id) as wins
	from players 
	left join scores
    on players.player_id = scores.winner_id
    group by players.player_id
    order by wins desc;                        

-- Create View Loss which has count of loss of a player
CREATE VIEW Loss AS	
	select players.player_id, players.player_name, count(scores.loser_id) as loss
    from players 
    left join scores
    on players.player_id = scores.loser_id
    group by players.player_id
    order by loss desc;

-- Create View Standings which has count of wins and total matches played
CREATE VIEW Standings AS
	select players.player_id, players.player_name, Wins.wins, loss+wins as matches 
	from players,Wins,Loss 
	where players.player_id = Wins.player_id and Wins.player_id = Loss.player_id


