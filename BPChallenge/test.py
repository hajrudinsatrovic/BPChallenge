# --------------------------------------------------------------------------
# Not part of coding challenge. Used to test if database could be opened and if I could execute a query on it.
# By Hajrudin Satrovic
# --------------------------------------------------------------------------
import sqlite3
import sys
from flask import Flask, jsonify, request
from flask_restful import Api, Resource

try: 
    conn = sqlite3.connect('buspatrol.db')
    print("Database has been opened")

    userinput = input("Enter your name: ") 
    cur = conn.cursor()
    cur.execute('SELECT TITLE, DESCRIPTION FROM JOBS, USERS WHERE USERS.NAME == ? AND USERS.job == JOBS.id', (userinput,))

    
    row = cur.fetchall()

    for i in row:
        print(i)

except lite.Error as e:
    print ("Error {}:".format(e.args[0]))
    sys.exit(1)

finally:
    if conn:
        conn.close()