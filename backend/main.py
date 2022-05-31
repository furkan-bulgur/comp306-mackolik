from flask import Flask
import mysql.connector
import json
from dotenv import load_dotenv
import os
from datetime import date, datetime

load_dotenv()

app = Flask(__name__)
conn = mysql.connector.connect(user=os.environ.get("DB_USER"), 
                                password=os.environ.get("PASSWORD"),
                                host=os.environ.get("HOST"),
                                database=os.environ.get("DATABASE"))

@app.route('/')
def landing():
    return "Welcome to Mackolik"

@app.route('/leagues')
def leagues():
    cursor = conn.cursor()
    cursor.execute("SELECT lid, name FROM league")
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    result = cursor.fetchall()
    json_data=[]
    for result in result:
            json_data.append(dict(zip(row_headers,result)))
    return json.dumps(json_data)

@app.route('/api', methods=['GET'])
def get_league_teams():
    return league_teams(39)

@app.route('/team', methods=['GET'])
def get_team_info():
    return team_info(165)

@app.route('/matches', methods=['GET'])
def get_team_matches():
    return team_matches(165)


def league_teams(lid):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM team WHERE lid = ' + str(lid))
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    result = cursor.fetchall()
    json_data=[]
    for result in result:
            json_data.append(dict(zip(row_headers,result)))
    return json.dumps(json_data)

def team_info(tid):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM player WHERE tid=' + str(tid))
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    result = cursor.fetchall()
    json_data=[]
    for result in result:
            json_data.append(dict(zip(row_headers,result)))
    print(json.dumps(json_data, cls=DatetimeEncoder))
    return json.dumps(json_data, cls=DatetimeEncoder)

def team_matches(tid):
    cursor = conn.cursor()
    cursor.execute('SELECT P.*, M.*, T1.name as home_team, T2.Name as away_team FROM 306db.plays as P, 306db.matches as M, 306db.team as T1, 306db.team as T2 WHERE P.mid = M.mid and (P.home_tid = ' + str(tid) + ' or P.away_tid = ' + str(tid) + ') and T1.tid = P.home_tid and T2.tid = P.away_tid order by M.week asc')
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    result = cursor.fetchall()
    json_data=[]
    for result in result:
            json_data.append(dict(zip(row_headers,result)))
    print(json.dumps(json_data, cls=DatetimeEncoder))
    return json.dumps(json_data, cls=DatetimeEncoder)

class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return super().default(obj)
        except TypeError:
            return str(obj)