## BPChallenge
***
The goal of this challenge is to code a RESTFUL GET endpoint at /users/<name> that takes uri paramaters with the user name and returns a json object with their job and description from the database (buspatrol.db). This challenge involved using python3, flask, and sqlite to create a webserver route.


## Files Included: 
***
1) CodingChallenge.py - This is the main program for this challenge which you will run to execute a webserver route that retrieves specfic information. 
2) BusPatrol.db - This is a database file that includes all the relevant information and contents needed to be returned. (WILL NOT WORK WITHOUT THIS DATABASE FILE PRESENT IN SAME DIRECTORY).
3) test.py - This program should not be relevant to you. The creator used this as a template to make sure the database could be opened and queries could be executed.
4) README.md - This file is the one you are presently viewing.


## Installation: 
***
1) First, you want to make sure you have Python3 installed on your machine. Python3 can be installed from their official website. Also, once installed make sure you have Flask installed and you have created an enviornment. Everything you need to know about that is well explained in detail in the following link: https://flask.palletsprojects.com/en/1.1.x/installation/
2) Once you have completed installation, you want to clone the repository onto your machine. Ex: git clone https://github.com/hajrudinsatrovic/BPChallenge.git
3) Confirm everything has been cloned by typing 'ls' and making sure all FILES INCLUDED are present.


## How To Run:
***
1) Now that you are ready to run the program, confirm you are in the correct working directory and proceed by typing python or python3 following the name of the first file in 'Files Included.' Ex: python3 CodingChallenge.py
2) Once the program has been run, you should see the following message:
 * Serving Flask app "CodingChallenge" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
- This means that everything has been successful and you are ready to retrieve user info.
3) We take the http link that they have provided in the message and paste onto our browser.
4) Once we paste it, we manually type in /users/<name> with name being whichever Employee you'd wish to view the job title and job description of.
Example: http://127.0.0.1:5000/users/kyle (This should return Kyle's job title and job description!)
5) This can be done as many times as you wish manually. 
