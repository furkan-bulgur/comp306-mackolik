from flask import Flask, request
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
def get_league():
    lid = request.args.get("lid", default=None)
    return leagues(lid)

# takımlar listesi * ve isim sırasıda göre leagues/teams?lid=12 +
@app.route('/leagues/teams', methods=['GET'])
def get_league_teams():
    lid = request.args.get("lid", default=None)
    return league_teams(lid)

# Puan durumu ordered leagues/standings?lid=12 +
@app.route('/leagues/standings', methods=['GET'])
def get_league_standings():
    lid = request.args.get("lid", default=None)
    return league_standings(lid)

# ligde kaçta hafta olduğunun döndüren leagues/weeks?lid=12 +
@app.route('/leagues/weeks', methods=['GET'])
def get_league_weeks():
    lid = request.args.get("lid", default=None)
    return league_weeks(lid)

# hafta velig parameteliyle o haftanın fistrü maçalrı leagues/fixtures?lid=12&week=21 +
@app.route('/leagues/fixtures', methods=['GET'])
def get_league_fixtures():
    lid = request.args.get("lid", default=None)
    week = request.args.get("week", default=None)
    return league_fixtures(lid,week)

# takım idyi verince select all döndüren bi qurery teams?tid=123 
@app.route('/teams', methods=['GET'])
def get_team_info():
    tid = request.args.get("lid", default=None)
    return team_info(tid)

# gol krallığı ilk 10 leagues/scorers?lid=12
@app.route('/leagues/scorers', methods=['GET'])
def get_league_scorers():
    lid = request.args.get("lid", default=None)
    return league_scorers(lid)

# asist krallığı ilk 10 leagues/assisters?lid=12
@app.route('/leagues/assisters', methods=['GET'])
def get_league_assisters():
    lid = request.args.get("lid", default=None)
    return league_assisters(lid)

@app.route('/matches', methods=['GET'])
def get_team_matches():
    return team_matches(165)

def leagues(lid=None):
    cursor = conn.cursor()
    query = "SELECT * FROM league" if lid is None else f"SELECT * FROM league WHERE lid = {lid}"
    cursor.execute(query)
    return convert_to_json(cursor)

def league_teams(lid):
    cursor = conn.cursor()
    query = f"SELECT * FROM team WHERE lid = {lid} ORDER BY team.name ASC"
    cursor.execute(query)
    return convert_to_json(cursor)

def league_standings(lid):
    cursor = conn.cursor()
    query = f"SELECT tid, T.rank, name, played,won,draw,loss, goals_for,goals_against,goalsDiff,points FROM team as T WHERE lid={lid}  ORDER BY T.rank asc;"
    cursor.execute(query)
    standings_json = convert_to_json(cursor)
    query = f"SELECT lid, name FROM league WHERE lid={lid}"
    cursor.execute(query)
    league_json = convert_to_json(cursor)
    final_json = league_json[:-2] + ", \"standings\": " + standings_json + "}]"
    return final_json

def league_weeks(lid):
    cursor = conn.cursor()
    query = f"SELECT count(*)*2 as weeks FROM 306db.plays as p, league as l, team as t WHERE p.home_tid=t.tid and l.lid=t.lid and l.lid={lid} GROUP BY home_tid LIMIT 1;"
    cursor.execute(query)
    return convert_to_json(cursor)

def league_fixtures(lid, week):
    cursor = conn.cursor()
    query = f"""SELECT P.*, M.*, T1.name as home_team, T2.Name as away_team
    FROM 306db.plays as P, 306db.matches as M, 306db.team as T1, 306db.team as T2, 306db.league as L 
    WHERE P.mid = M.mid and T1.tid = P.home_tid and T2.tid = P.away_tid and T1.lid = L.lid and L.lid = {lid}  and M.week = {week} 
    ORDER BY M.date ASC;"""
    cursor.execute(query)
    return convert_to_json(cursor)

def team_info(tid):
    cursor = conn.cursor()
    query = f"SELECT * FROM team WHERE tid = {tid}"
    cursor.execute(query)
    return convert_to_json(cursor)

def league_scorers(lid):
    cursor = conn.cursor()
    query = f"""SELECT Pl.pid, T.name, concat(Pl.fname," ", Pl.lname) as name, Count(*) as played_match, Sum(P.mins_played) as played_min, Sum(P.total_goals) as goals, Sum(P.assists) as assists , team_total.team_goals as total_goals
    FROM 306db.plays_in as P , player as Pl, league as L, team as T, (SELECT T.tid ,Sum(P.total_goals) as team_goals
    FROM 306db.plays_in as P , player as Pl, league as L, team as T
    WHERE P.pid = Pl.pid and Pl.tid = T.tid and T.lid= L.lid and L.lid = {lid}
    group by T.tid
    order by team_goals DESC) as team_total
    WHERE P.pid = Pl.pid and Pl.tid = T.tid and T.lid= L.lid and L.lid = {lid} and team_total.tid= T.tid
    group by P.pid
    order by goals DESC
    LIMIT 10;"""
    cursor.execute(query)
    return convert_to_json(cursor)

def league_assisters(lid):
    cursor = conn.cursor()
    query = f"""SELECT Pl.pid, T.name, concat(Pl.fname," ", Pl.lname) as name, Count(*) as played_match, Sum(P.mins_played) as played_min, Sum(P.total_goals) as goals, Sum(P.assists) as assists , team_total.team_goals as total_goals
    FROM 306db.plays_in as P , player as Pl, league as L, team as T, (SELECT T.tid ,Sum(P.total_goals) as team_goals
    FROM 306db.plays_in as P , player as Pl, league as L, team as T
    WHERE P.pid = Pl.pid and Pl.tid = T.tid and T.lid= L.lid and L.lid = {tid}
    group by T.tid
    order by team_goals DESC) as team_total
    WHERE P.pid = Pl.pid and Pl.tid = T.tid and T.lid= L.lid and L.lid = {tid} and team_total.tid= T.tid
    group by P.pid
    order by assists DESC
    LIMIT 10;"""
    cursor.execute(query)
    return convert_to_json(cursor)

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


def convert_to_json(cursor):
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    result = cursor.fetchall()
    json_data=[]
    for result in result:
            json_data.append(dict(zip(row_headers,result)))
    return json.dumps(json_data, cls=DatetimeEncoder)


class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return super().default(obj)
        except TypeError:
            return str(obj)



# Puan durumu ordered leagues/standings?lid=12 +
# ligde kaçta hafta olduğunun döndüren leagues/weeks?lid=12 +
# hafta velig parameteliyle o haftanın fistrü maçalrı leagues/fixtures?lid=12&week=21 +
# gol krallığı ilk 10 leagues/scorers?lid=12
# asist krallığı ilk 10 leagues/assisters?lid=12
# disiplin tablosu ilk 10 leagues/cards?lid=12
# takım idyi verince select all döndüren bi qurery teams?tid=123 +
# takımlar listesi * ve isim sırasıda göre leagues/teams?lid=12 +

