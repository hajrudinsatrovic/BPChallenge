## BPChallenge
***
The goal of this challenge is to code a RESTFUL GET endpoint at /users/<name> that takes uri paramaters with the user name and returns a json object with their job and description from the database (BusPatrol.db).


## INSTALLATION:
***
1) Before beginning, make sure you have one of the later versions of Python installed on your machine. Also, make sure you install certain modules like Flask and create an enviornment. Everything is well explained in the following link: https://flask.palletsprojects.com/en/1.1.x/installation/
2) Following basic installation, you should git clone the repository as followed: $ git clone https://github.com/hajrudinsatrovic/BPChallenge.git with HTTPS or SSH
3) Enter 'ls' and confirm that everything is now all files in your directory.

## FILES INCLUDED:
***
1) CodingChallenge.py - This is the main program that you will be running which will complete the main objective of this challenge. 
2) buspatrol.db - This is a sqlite database file which will need to retrieve data from. (Program will not work without this file!)
3) test.py - This file should not be of much relevance to you. This was mainly used as a template for the creator to ensure 'buspatrol.db' could be opened and could execute queries.
4) README.md - This is the present file you are reading.


## RUNNING THE PROGRAM:
***
1) Now that you have confirmed that you are correct directory and all files included are present you need to simply type 'python3' or 'python' with the name of the program which is listed as #1 under "FILES INCLUDED." So, it would look something like this: python3 CodingChallenge.py
2) Once you have run this command, you should receive a message stating:
* Serving Flask app "CodingChallenge" (lazy loading)
* Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
* Debug mode: on
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
3) This means the program has been successful and you are ready to retrieve whatever job title & job description you want from a specfic user from 'buspatrol.db'.
4) To actually now retrieve this information you would copy the http link into a browser and manually enter after the 5000/ users/<name> with name being an Employee you wish to view. 
Example: http://127.0.0.1:5000/users/kyle
5) Once you have typed in which /users/<name> you'd like to view and have clicked enter the browser should return a JSON object with the user's job title and job description.


