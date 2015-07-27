# fullstack-project2

This is the second project for the FullStack Nano Degree for **Courses:
    Intro to Relational Databases**

The project contains the files related to the 
**Projects:p2: Tournament Results**
Files Included:
-------------
There are three files included.
  - tournament.sql
  - tournament.py
  - tournament_test.py

**tournament.sql**:
This file contains all the schema for the underlying database. For the project we have created two tables: **_player_** and **_scores_**.
The player table contains unique id and name of a every player.
The scores table contains unique id and name of every winning and losing player in every game.

**tournament.py**
This file contains all the python code which is used to connect to the **tournament.db** database and all the adjoining queries that will make the backend logic for the project.

**tournament_test.py**
This is the file given to us by the course instructor. It has python code that checks whether the functions built in tournament.py is implemented correctly and the test runs successfully.

Downloading
-----------

The project can be either downloaded using the **Clone in Desktop** or direct **Download Zip** the zip file.

Running the Project
-----------
Perform the following steps:

	1. Copy paste the folder to the fullstack/vagrant directory
	2. Using the terminal, change directory to fullstack/vagrant (cd fullstack/vagrant), then type vagrant up to launch your virtual machine.

Note: If you haven't installed vagrant follow this [link](https://www.udacity.com/wiki/ud197/install-vagrant) on how to install vagrant.

	3. Once it is up and running, type vagrant ssh to log into it. This will log your terminal in to the virtual machine, and you'll get a Linux shell prompt. 
	4. Create database 'tournament.db'. To successfully create the database type psql tournament at the terminal. After that you'll be prompted into the psql prompt. To insert the two tables (PLAYERS and SCORES) copy the schema from the tournament.sql file and run the two query which will create players and scores table. To check for the list of tables within the database type \dt at the termimal, which will show players and scores table listed. And to quit from the terminal type \q or Control-D (^D).
	Or, type psql -f tournament.sql to build the tables if you don't want manual approach.
	5. Quit from the psql prompt. Go to the folder fullstack/vagrant/fullstack-project2 and type python tournament_test.py.
    
 You'll get the following successful scenario:
 
![alt text](https://github.com/biratrai/fullstack-project2/blob/master/successresult/success%20result.png)





  
