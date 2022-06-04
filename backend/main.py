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
    tid = request.args.get("tid", default=None)
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

# disiplin tablosu ilk 10 leagues/cards?lid=12
@app.route('/leagues/cards', methods=['GET'])
def get_league_cards():
    lid = request.args.get("lid", default=None)
    return league_cards(lid)

# maçtaki home takım statikleri /matches/statistics/home?mid=65
@app.route('/matches/statistics/home', methods=['GET'])
def get_match_statistics_home():
    mid = request.args.get("mid", default=None)
    return home_statistics(mid)

# maçtaki away takım statikleri /matches/statistics/away?mid=65
@app.route('/matches/statistics/away', methods=['GET'])
def get_match_statistics_away():
    mid = request.args.get("mid", default=None)
    return away_statistics(mid)

# takım playerlerı /teams/players?tid=65
@app.route('/teams/players', methods=['GET'])
def get_team_players():
    tid = request.args.get("tid", default=None)
    return team_players(tid)

# takım fixtures /teams/fixtures?tid=65
@app.route('/teams/fixtures', methods=['GET'])
def get_team_fixtures():
    tid = request.args.get("tid", default=None)
    return team_fixtures(tid)


# gol krallığı ilk 10 leagues/scorers?lid=12
@app.route('/teams/scorers', methods=['GET'])
def get_teams_scorers():
    lid = request.args.get("lid", default=None)
    return team_scorers(lid)

# asist krallığı ilk 10 leagues/assisters?lid=12
@app.route('/teams/assisters', methods=['GET'])
def get_teams_assisters():
    lid = request.args.get("lid", default=None)
    return team_assisters(lid)

# disiplin tablosu ilk 10 leagues/cards?lid=12
@app.route('/teams/cards', methods=['GET'])
def get_league_cards():
    lid = request.args.get("lid", default=None)
    return league_cards(lid)

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
    query = f"SELECT count(*)*2 as weeks FROM plays as p, league as l, team as t WHERE p.home_tid=t.tid and l.lid=t.lid and l.lid={lid} GROUP BY home_tid LIMIT 1;"
    cursor.execute(query)
    weeks_json = convert_to_json(cursor)
    query = f"SELECT lid, name FROM league WHERE lid={lid}"
    cursor.execute(query)
    league_json = convert_to_json(cursor)
    final_json = league_json[:-2] + ", \"weeks\": " + weeks_json + "}]"
    return final_json

def league_fixtures(lid, week):
    cursor = conn.cursor()
    query = f"""SELECT P.mid, P.home_tid, P.away_tid, M.week, M.date, T1.name as home_team, concat(M.home_goals," - ", M.away_goals) as score, T2.Name as away_team, M.referee
    FROM plays as P, matches as M, team as T1, team as T2, league as L 
    WHERE P.mid = M.mid and T1.tid = P.home_tid and T2.tid = P.away_tid and T1.lid = L.lid and L.lid = {lid}  and M.week = {week}
    ORDER BY M.date ASC;"""
    cursor.execute(query)
    fixtures_json = convert_to_json(cursor)
    query = f"SELECT lid, name FROM league WHERE lid={lid}"
    cursor.execute(query)
    league_json = convert_to_json(cursor)
    final_json = league_json[:-2] + ", \"fixtures\": " + fixtures_json + "}]"
    return final_json

def team_info(tid):
    cursor = conn.cursor()
    query = f"SELECT * FROM team WHERE tid = {tid}"
    cursor.execute(query)
    return convert_to_json(cursor)

def league_scorers(lid):
    cursor = conn.cursor()
    query = f"""SELECT Pl.pid, T.tid, T.name as team_name, concat(Pl.fname," ", Pl.lname) as name, Count(*) as played_match, Sum(P.mins_played) as played_min, Sum(P.total_goals) as goals, Sum(P.assists) as assists , Sum(P.total_goals)/Count(*) as goal_per_match
    FROM plays_in as P , player as Pl, league as L, team as T, (SELECT T.tid ,Sum(P.total_goals) as team_goals
    FROM plays_in as P , player as Pl, league as L, team as T
    WHERE P.pid = Pl.pid and Pl.tid = T.tid and T.lid= L.lid and L.lid = {lid}
    group by T.tid
    order by team_goals DESC) as team_total
    WHERE P.pid = Pl.pid and Pl.tid = T.tid and T.lid= L.lid and L.lid = {lid} and team_total.tid= T.tid
    group by P.pid
    order by goals DESC
    LIMIT 10;"""
    cursor.execute(query)
    scorers_json = convert_to_json(cursor)
    query = f"SELECT lid, name FROM league WHERE lid={lid}"
    cursor.execute(query)
    league_json = convert_to_json(cursor)
    final_json = league_json[:-2] + ", \"scorers\": " + scorers_json + "}]"
    return final_json

def league_assisters(lid):
    cursor = conn.cursor()
    query = f"""SELECT Pl.pid, T.tid, T.name as team_name, concat(Pl.fname," ", Pl.lname) as name, Count(*) as played_match, Sum(P.mins_played) as played_min, Sum(P.total_goals) as goals, Sum(P.assists) as assists , Sum(P.assists)/Count(*) as assists_per_match
    FROM plays_in as P , player as Pl, league as L, team as T, (SELECT T.tid ,Sum(P.total_goals) as team_goals
    FROM plays_in as P , player as Pl, league as L, team as T
    WHERE P.pid = Pl.pid and Pl.tid = T.tid and T.lid= L.lid and L.lid = {lid}
    group by T.tid
    order by team_goals DESC) as team_total
    WHERE P.pid = Pl.pid and Pl.tid = T.tid and T.lid= L.lid and L.lid = {lid} and team_total.tid= T.tid
    group by P.pid
    order by assists DESC
    LIMIT 10;"""
    cursor.execute(query)
    assisters_json = convert_to_json(cursor)
    query = f"SELECT lid, name FROM league WHERE lid={lid}"
    cursor.execute(query)
    league_json = convert_to_json(cursor)
    final_json = league_json[:-2] + ", \"assisters\": " + assisters_json + "}]"
    return final_json

def league_cards(lid):
    cursor = conn.cursor()
    cursor.execute("SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));")
    query = f"""SELECT red.pid, red.tid, red.team, red.name, red.played_match, red.played_min, red.red_cards, yellow.yellow_cards, red_cards+yellow.yellow_cards as total_cards
    FROM
    (SELECT Pl.pid, T.tid, T.name as team, concat(Pl.fname," ", Pl.lname) as name, Count(*) as played_match, Sum(P.mins_played) as played_min, Sum(P.red_cards) as red_cards
    FROM plays_in as P , player as Pl, league as L, team as T
    WHERE P.pid = Pl.pid and Pl.tid = T.tid and T.lid= L.lid and L.lid = {lid}
    group by P.pid
    order by red_cards DESC) as red,
    (SELECT Pl.pid, T.tid, T.name as team, concat(Pl.fname," ", Pl.lname) as name, Count(*) as played_match, Sum(P.mins_played) as played_min, Sum(P.yellow_cards) as yellow_cards
    FROM plays_in as P , player as Pl, league as L, team as T
    WHERE P.pid = Pl.pid and Pl.tid = T.tid and T.lid= L.lid and L.lid = {lid}
    group by P.pid
    order by red_cards DESC) as yellow
    WHERE red.pid = yellow.pid
    order by total_cards desc
    limit 10;"""
    cursor.execute(query)
    cards_json = convert_to_json(cursor)
    query = f"SELECT lid, name FROM league WHERE lid={lid}"
    cursor.execute(query)
    league_json = convert_to_json(cursor)
    final_json = league_json[:-2] + ", \"cards\": " + cards_json + "}]"
    return final_json

def home_statistics(mid):
    cursor = conn.cursor()
    query = f"""SELECT T1.tid, T1.name as team, PI.mid, PI.pid, PI.number, concat(P.fname," ", P.lname) as name,  PI.position, PI.mins_played, PI.yellow_cards, PI.red_cards, PI.passes, PI.total_shots, PI.on_shots, PI.saves, PI.conceded_goals, PI.total_goals, PI.assists, PI.rating
    FROM matches as M, team as T1, plays as PL, player as P, plays_in as PI
    WHERE M.mid = PL.mid and PI.mid = M.mid and PI.pid = P.pid and P.tid= T1.tid and PL.home_tid = T1.tid and M.mid={mid}
    ORDER BY mins_played DESC;"""
    cursor.execute(query)
    statistics_json = convert_to_json(cursor)
    query = f"""SELECT L.lid, L.name, T1.name as team, M.home_goals
    FROM matches as M, team as T1, plays as PL, league as L
    WHERE M.mid = PL.mid and PL.home_tid = T1.tid and T1.lid = L.lid and M.mid={mid}"""
    cursor.execute(query)
    league_json = convert_to_json(cursor)
    final_json = league_json[:-2] + ", \"statistics\": " + statistics_json + "}]"
    return final_json

def away_statistics(mid):
    cursor = conn.cursor()
    query = f"""SELECT T2.tid, T2.name as team, PI.mid, PI.pid, PI.number, concat(P.fname," ", P.lname) as name,  PI.position, PI.mins_played, PI.yellow_cards, PI.red_cards, PI.passes, PI.total_shots, PI.on_shots, PI.saves, PI.conceded_goals, PI.total_goals, PI.assists, PI.rating
    FROM matches as M, team as T2, plays as PL, player as P, plays_in as PI
    WHERE M.mid = PL.mid and PI.mid = M.mid and PI.pid = P.pid and P.tid= T2.tid and  PL.away_tid = T2.tid and M.mid={mid}
    ORDER BY mins_played DESC;"""
    cursor.execute(query)
    statistics_json = convert_to_json(cursor)
    query = f"""SELECT L.lid, L.name , T2.name as team, M.away_goals
    FROM matches as M, team as T2, plays as PL, league as L
    WHERE M.mid = PL.mid and PL.away_tid = T2.tid and T2.lid = L.lid and M.mid={mid}"""
    cursor.execute(query)
    league_json = convert_to_json(cursor)
    final_json = league_json[:-2] + ", \"statistics\": " + statistics_json + "}]"
    return final_json

def team_players(tid):
    cursor = conn.cursor()
    query = f"""SELECT PI.pid, number, PI.position, P.nation, concat(P.fname," ", P.lname) as name,(2022 - year(P.birthdate)) as age, count(*) as played_match, sum(PI.mins_played) as mins_played, sum(PI.total_goals) as goals, sum(PI.assists) as assists, sum(PI.yellow_cards) as yellow_cards, sum(PI.red_cards) as red_cards, sum(PI.total_shots) as total_shots, sum(PI.on_shots) as on_shots, sum(PI.saves) as saves, sum(PI.conceded_goals) as conceded_goals, TRUNCATE(avg(PI.rating),2) as avg_rating
    FROM player as P, plays_in as PI, team as T, league as L
    WHERE PI.pid = P.pid and P.tid = T.tid and T.tid={tid} and T.lid = L.lid
    GROUP BY PI.pid
    ORDER BY number"""
    cursor.execute(query)
    statistics_json = convert_to_json(cursor)
    query = f"""SELECT L.lid, L.name,T.tid, T.name as team
    FROM team as T, league as L
    WHERE T.lid = L.lid and T.tid={tid};"""
    cursor.execute(query)
    league_json = convert_to_json(cursor)
    final_json = league_json[:-2] + ", \"players\": " + statistics_json + "}]"
    return final_json

def team_fixtures(tid):
    cursor = conn.cursor()
    query = f"""SELECT P.mid, P.home_tid, P.away_tid, M.week, M.date, T1.name as home_team, concat(M.home_goals," - ", M.away_goals) as score, T2.Name as away_team, M.referee
    FROM plays as P, matches as M, team as T1, team as T2 
    WHERE P.mid = M.mid and (P.home_tid ={tid} or P.away_tid = {tid}) and T1.tid = P.home_tid and T2.tid = P.away_tid 
    ORDER BY M.week asc"""
    cursor.execute(query)
    statistics_json = convert_to_json(cursor)
    query = f"""SELECT L.lid, L.name,T.tid, T.name as team
    FROM team as T, league as L
    WHERE T.lid = L.lid and T.tid={tid};"""
    cursor.execute(query)
    league_json = convert_to_json(cursor)
    final_json = league_json[:-2] + ", \"fixtures\": " + statistics_json + "}]"
    return final_json

def team_matches(tid):
    cursor = conn.cursor()
    cursor.execute('SELECT P.*, M.*, T1.name as home_team, T2.Name as away_team FROM plays as P, matches as M, team as T1, team as T2 WHERE P.mid = M.mid and (P.home_tid = ' + str(tid) + ' or P.away_tid = ' + str(tid) + ') and T1.tid = P.home_tid and T2.tid = P.away_tid order by M.week asc')
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
# gol krallığı ilk 10 leagues/scorers?lid=12 +
# asist krallığı ilk 10 leagues/assisters?lid=12 +
# disiplin tablosu ilk 10 leagues/cards?lid=12
# takım idyi verince select all döndüren bi qurery teams?tid=123 +
# takımlar listesi * ve isim sırasıda göre leagues/teams?lid=12 +

# def league_standings(lid):
#     cursor = conn.cursor()
#     query = f"SELECT tid, name, played,won,draw,loss, goals_for,goals_against,goalsDiff,points FROM team as T WHERE lid={lid}  ORDER BY T.rank asc;"
#     cursor.execute(query)
#     standings_json = convert_to_json(cursor)
#     query = f"SELECT lid, name FROM league WHERE lid={lid}"
#     cursor.execute(query)
#     league_json = convert_to_json(cursor)
#     final_json = league_json[:-2] + ", \"standings\": " + standings_json + "}]"
#     return final_json