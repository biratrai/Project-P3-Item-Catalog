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

	3. Once it is up and running, type vagrant ssh to log into it. This will log your terminal in to the virtual machine, and you'll get a Linux shell prompt
    4. Then go to the folder fullstack/vagrant/fullstack-project2 and type python tournament_test.py.
    You'll get the following 





  
