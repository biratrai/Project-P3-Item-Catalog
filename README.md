# Project-P3-Item-Catalog
This is the third project of the Full Stack Nano Degree from Udacity

This project was developed under the [**Full-Stack-Developer Nano Degree Program**](https://www.udacity.com/course/nd004) offered by Udacity.

**How to Run the Application**
-----------------------------------------------------------

First, you need to install VirtualBox and Vagrant on your machine.

Then, you'll need to clone this repository to your local machine.

Go to the vagrant directory in the cloned repository, then open a terminal window and type $ vagrant up to launch your virtual machine. This will take some time in your first run, because it needs to install some dependencies.

Once it is up and running, type $ vagrant ssh to log into it. This will log your terminal in to the virtual machine, and you'll get a Linux shell prompt.

Go inside the Catalog directory and run the database_setup.py and enter_data.py accordingly to setup database and populate with fake datas.

Run the runserver.py python file, This will launch the application.

You can check out the page from your browser at http://localhost:8000.
