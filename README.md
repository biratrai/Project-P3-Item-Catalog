# Project-P3-Item-Catalog
This is the third project of the Full Stack Nano Degree from Udacity

This project was developed under the [**Full-Stack-Developer Nano Degree Program**](https://www.udacity.com/course/nd004) offered by Udacity.

**How to Run the Application**
-----------------------------------------------------------

1. First, you need to install VirtualBox and Vagrant on your machine.
2. Then, you'll need to clone this repository to your local machine.
3. Go to the vagrant directory in the cloned repository, then open a terminal window and type $ vagrant up to launch your virtual machine. This will take some time in your first run, because it needs to install some dependencies.
4. Once it is up and running, type $ vagrant ssh to log into it. This will log your terminal in to the virtual machine, and you'll get a Linux shell prompt.
5. Go inside the Catalog directory and run the database_setup.py and enter_data.py accordingly to setup database and populate with fake datas.
6. Run the runserver.py python file, This will launch the application.
7. You can check out the page from your browser at http://localhost:8000.

**Getting the JSON API**
-----------------------------------------------------------
1. The general API end point is : http://localhost:8000/fullstack/p1/JSON
2. You can change the project name to fullstack/frontend/android/ios/others and project number to p1-p6 if it exists.
