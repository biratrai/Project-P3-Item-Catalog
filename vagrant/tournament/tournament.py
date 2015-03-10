#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    c = db.cursor()
    c.execute("DELETE from scores")
    db.commit()
    db.close()

def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    c = db.cursor()
    c.execute("DELETE from players")
    db.commit()
    db.close()

def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    c = db.cursor()
    c.execute("SELECT COUNT(*) FROM players")

    """ This fetchall statement fetches rows of a query result set and returns a list of tuples. """
    count = c.fetchall()

    db.commit()
    db.close()
    
    return int(count[0][0])

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    c = db.cursor()
    
    # Cleaning the input with bleach
    bleached_name = bleach.clean(name, strip=True)
    c.execute("INSERT INTO players (player_name) VALUES (%s)", (bleached_name,))
    db.commit()
    db.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    c = db.cursor()
    c.execute("select player_id,player_name,wins,matches from Standings Order by wins desc;")
    db.commit()

    """ This fetchall statement fetches rows of a query result set and returns a list of tuples which contains (id, name, wins, matches): """
    results = c.fetchall()
    db.close()
    return results
    
def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    c = db.cursor()
    c.execute("INSERT INTO scores (winner_id,loser_id) VALUES (%s,%s)",(winner,loser,))
    db.commit()
    db.close()

def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    standings = [(record[0], record[1]) for record in playerStandings()]

    # If there are players less than 2 raise an ValueError message
    if len(standings) < 2:
        raise ValueError("Not enough players.")

    first_pair = standings[0::2]
    second_pair = standings[1::2]

    # This function returns a list of tuples, where the i-th tuple contains the i-th element from each of the first_pair and second_pair
    new_pairings = zip(first_pair, second_pair) 

    # Unpacking the tuple after zip
    first,second = new_pairings[0]
    third,fourth = new_pairings[1]

    # Making a tuple which contains (id1, name1, id2, name2) 
    result = (first+second,third+fourth)
    
    return result


