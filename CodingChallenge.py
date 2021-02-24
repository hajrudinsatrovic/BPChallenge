# --------------------------------------------------------------------------
# Simple web server route that serves database information from buspatrol.db 
# By Hajrudin Satrovic
# --------------------------------------------------------------------------
import sqlite3
import sys
from flask import Flask, jsonify, request
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)

class Challenge(Resource):
    def get(self, name):
        """Opens the database 'buspatrol.db' to retrieve information from and 
        returns the job description and job title of the user requested."""
        try: 
            conn = sqlite3.connect('buspatrol.db')

            cur = conn.cursor()
            cur.execute('SELECT TITLE FROM JOBS, USERS WHERE USERS.NAME == ? AND USERS.job == JOBS.id', (name,))
            #Here, we write the query to get the job title of the user that has been requested and then execute it. 
            #The attribute 'job' from USERS has the same values when corresponded to 'id' from JOBS for each user. 
            title = cur.fetchall()

            cur.execute('SELECT DESCRIPTION FROM JOBS, USERS WHERE USERS.NAME == ? AND USERS.job == JOBS.id', (name,))
            #Similarly, we write the query to retrieve the job description of the user that has been requested and then execute it. 
            description = cur.fetchall()

        except lite.Error as e:
            print ("Error {}:".format(e.args[0]))
            sys.exit(1)

        return jsonify(
                {"job_title": title, "job_description":description})
            
        conn.close()

api.add_resource(Challenge, "/users/<name>")

if __name__ == "__main__":
   app.run(debug=True)
