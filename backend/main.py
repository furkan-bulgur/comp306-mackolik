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
cursor = conn.cursor()
cursor.execute("SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));")

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


# takımın gol tablosu team/scorers?tid=12
@app.route('/teams/scorers', methods=['GET'])
def get_team_scorers():
    tid = request.args.get("tid", default=None)
    return team_scorers(tid)

# takımın asisst tablosu teams/assisters?tid=12
@app.route('/teams/assisters', methods=['GET'])
def get_team_assisters():
    tid = request.args.get("tid", default=None)
    return team_assisters(tid)

#  takım disiplin tablosu  teams/cards?tid=12
@app.route('/teams/cards', methods=['GET'])
def get_team_cards():
    tid = request.args.get("tid", default=None)
    return team_cards(tid)

#  player info  /players?pid=644
@app.route('/players', methods=['GET'])
def get_player():
    pid = request.args.get("pid", default=None)
    return player(pid)

@app.route('/funfacts', methods=['GET'])
def get_funfacts():
    return funfacts()

# İngiltere liginde en az 25 maç oynayan oyuncular arasından maç başı ortalama ratinglere göre sezonun en iyi ilk 11'i (4-4-2) formasyonunda
#  fun fact1  /funfacts1
@app.route('/funfacts1', methods=['GET'])
def get_funfacts1():
    return funfacts1()

#İngiltere liginde en az 15 maçta görev alan hakemlerin yönettiği maçlarda ev sahibi takımın maç kazanma yüzdesi 
#  fun fact2  /funfacts2
@app.route('/funfacts2', methods=['GET'])
def get_funfacts2():
    return funfacts2()    

# İspnaya liginde her posizyonda en çok gol atan oyuncular ve attıkları goller
#  fun fact3  /funfacts3
@app.route('/funfacts3', methods=['GET'])
def get_funfacts3():
    return funfacts3()  

#liglerin yaş ortalaması
#  fun fact4  /funfacts4
@app.route('/funfacts4', methods=['GET'])
def get_funfacts4():
    return funfacts4() 

#liglerin yaş ortalaması
#  fun fact5  /funfacts5
@app.route('/funfacts4', methods=['GET'])
def get_funfacts5():
    return funfacts5() 

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
    players_json = convert_to_json(cursor)
    query = f"""SELECT L.lid, L.name,T.tid, T.name as team
    FROM team as T, league as L
    WHERE T.lid = L.lid and T.tid={tid};"""
    cursor.execute(query)
    league_json = convert_to_json(cursor)
    final_json = league_json[:-2] + ", \"players\": " + players_json + "}]"
    return final_json

def team_fixtures(tid):
    cursor = conn.cursor()
    query = f"""SELECT P.mid, P.home_tid, P.away_tid, M.week, M.date, T1.name as home_team, concat(M.home_goals," - ", M.away_goals) as score, T2.Name as away_team, M.referee
    FROM plays as P, matches as M, team as T1, team as T2 
    WHERE P.mid = M.mid and (P.home_tid ={tid} or P.away_tid = {tid}) and T1.tid = P.home_tid and T2.tid = P.away_tid 
    ORDER BY M.week asc"""
    cursor.execute(query)
    fixtures_json = convert_to_json(cursor)
    query = f"""SELECT L.lid, L.name,T.tid, T.name as team
    FROM team as T, league as L
    WHERE T.lid = L.lid and T.tid={tid};"""
    cursor.execute(query)
    league_json = convert_to_json(cursor)
    final_json = league_json[:-2] + ", \"fixtures\": " + fixtures_json + "}]"
    return final_json

def team_scorers(tid):
    cursor = conn.cursor()
    query = f"""SELECT Pl.pid, T.name as Team, concat(Pl.fname," ", Pl.lname) as name, Count(*) as played_match, Sum(P.mins_played) as played_min, Sum(P.total_goals) as goals, Sum(P.assists) as assists , Sum(P.total_goals)/Count(*) as goals_per_match
    FROM plays_in as P , player as Pl, league as L, team as T
    WHERE P.pid = Pl.pid and Pl.tid = T.tid and T.lid= L.lid and T.tid = 50 
    group by P.pid
    order by goals DESC;"""
    cursor.execute(query)
    scorers_json = convert_to_json(cursor)
    query = f"""SELECT L.lid, L.name,T.tid, T.name as team
    FROM team as T, league as L
    WHERE T.lid = L.lid and T.tid={tid};"""
    cursor.execute(query)
    league_json = convert_to_json(cursor)
    final_json = league_json[:-2] + ", \"scorers\": " + scorers_json + "}]"
    return final_json

def team_assisters(tid):
    cursor = conn.cursor()
    query = f"""SELECT Pl.pid, T.name as team, concat(Pl.fname," ", Pl.lname) as name, Count(*) as played_match, Sum(P.mins_played) as played_min, Sum(P.total_goals) as goals, Sum(P.assists) as assists , Sum(P.assists)/Count(*) as assists_per_match
    FROM plays_in as P , player as Pl, league as L, team as T
    WHERE P.pid = Pl.pid and Pl.tid = T.tid and T.lid= L.lid and T.tid = 50 
    group by P.pid
    order by assists DESC;"""
    cursor.execute(query)
    assisters_json = convert_to_json(cursor)
    query = f"""SELECT L.lid, L.name,T.tid, T.name as team
    FROM team as T, league as L
    WHERE T.lid = L.lid and T.tid={tid};"""
    cursor.execute(query)
    league_json = convert_to_json(cursor)
    final_json = league_json[:-2] + ", \"assisters\": " + assisters_json + "}]"
    return final_json

def team_cards(tid):
    cursor = conn.cursor()
    cursor.execute("SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));")
    query = f"""SELECT red.pid, red.team, red.name, red.played_match, red.played_min, red.red_cards, yellow.yellow_cards, red_cards+yellow.yellow_cards as total_cards
    FROM
    (SELECT Pl.pid, T.name as team, concat(Pl.fname," ", Pl.lname) as name, Count(*) as played_match, Sum(P.mins_played) as played_min, Sum(P.red_cards) as red_cards
    FROM plays_in as P , player as Pl, league as L, team as T
    WHERE P.pid = Pl.pid and Pl.tid = T.tid and T.lid= L.lid and T.tid = 50
    group by P.pid
    order by red_cards DESC) as red,
    (SELECT Pl.pid, T.name as team, concat(Pl.fname," ", Pl.lname) as name, Count(*) as played_match, Sum(P.mins_played) as played_min, Sum(P.yellow_cards) as yellow_cards
    FROM plays_in as P , player as Pl, league as L, team as T
    WHERE P.pid = Pl.pid and Pl.tid = T.tid and T.lid= L.lid and T.tid = 50
    group by P.pid
    order by red_cards DESC) as yellow
    WHERE red.pid = yellow.pid
    order by total_cards desc;"""
    cursor.execute(query)
    cards_json = convert_to_json(cursor)
    query = f"""SELECT L.lid, L.name,T.tid, T.name as team
    FROM team as T, league as L
    WHERE T.lid = L.lid and T.tid={tid};"""
    cursor.execute(query)
    league_json = convert_to_json(cursor)
    final_json = league_json[:-2] + ", \"cards\": " + cards_json + "}]"
    return final_json

def player(pid):
    cursor = conn.cursor()
    query = f"""SELECT pid, concat(fname," ", lname) as name, nation, height, weight, birthdate, year(now()) - year(birthdate) as age
    FROM player 
    WHERE pid={pid};"""
    cursor.execute(query)
    player_json = convert_to_json(cursor)
    query = f"""SELECT L.lid, L.name,T.tid, T.name as team
    FROM team as T, league as L, player as P
    WHERE T.lid = L.lid and T.tid=P.tid and P.pid = {pid};"""
    cursor.execute(query)
    league_json = convert_to_json(cursor)
    final_json = league_json[:-2] + ", \"info\": " + player_json + "}]"
    return final_json

def funfacts1():
    cursor = conn.cursor()
    query = f"""
    (select p.pid, p.fname, p.lname, pin.position, t.name, round(avg(pin.rating), 2) as avg_rating, count(*) as played_match
    from team t, player p, plays_in pin, league l
    where t.lid = l.lid and l.country = 'England' and p.tid=t.tid and p.pid = pin.pid and pin.position like '%G%'
    group by p.pid
    having count(*) > 25
    order by avg_rating DESC
    limit 1)
    UNION
    (select p.pid, p.fname, p.lname, pin.position, t.name, round(avg(pin.rating), 2) as avg_rating, count(*) as played_match
    from team t, player p, plays_in pin, league l
    where t.lid = l.lid and l.country = 'England' and p.tid=t.tid and p.pid = pin.pid and pin.position like '%D%'
    group by p.pid
    having count(*) > 25
    order by avg_rating DESC
    limit 4)
    UNION
    (select p.pid, p.fname, p.lname, pin.position, t.name, round(avg(pin.rating), 2) as avg_rating, count(*) as played_match
    from team t, player p, plays_in pin, league l
    where t.lid = l.lid and l.country = 'England' and p.tid=t.tid and p.pid = pin.pid and pin.position like '%M%'
    group by p.pid
    having count(*) > 25
    order by avg_rating DESC
    limit 4)
    UNION
    (select p.pid, p.fname, p.lname, pin.position, t.name, round(avg(pin.rating), 2) as avg_rating, count(*) as played_match
    from team t, player p, plays_in pin, league l
    where t.lid = l.lid and l.country = 'England' and p.tid=t.tid and p.pid = pin.pid and pin.position like '%F%'
    group by p.pid
    having count(*) > 25
    order by avg_rating DESC
    limit 2);"""
    cursor.execute(query)
    funfacts1_json = convert_to_json(cursor)
    final_json = "{\"explanation\": \"Best line-up (in 4-4-2 format) in Premier League using average match ratings of the players. Only players with a minimum of 25 played matches are included\"" + ", \"result\": " + funfacts1_json + "}"
    return final_json

def funfacts2():
    cursor = conn.cursor()
    query = f"""
    select ref_table.referee, count(*) / ref_table.games as home_win_rate, ref_table.games
    from (select m.referee, count(*) as games
        from matches m, plays p, team t1, team t2, league l
        where m.mid = p.mid and t1.tid = p.home_tid and t2.tid = p.away_tid and t1.lid=l.lid and t2.lid=l.lid and l.country = 'England'
        group by m.referee
        having count(*) > 15) as ref_table,
        matches m, plays p, team t1, team t2
    where m.mid = p.mid and t1.tid = p.home_tid and t2.tid = p.away_tid and ref_table.referee = m.referee and m.home_goals > m.away_goals
    group by ref_table.referee
    order by home_win_rate DESC;"""
    cursor.execute(query)
    funfacts2_json = convert_to_json(cursor)
    final_json = "{\"explanation\": \"Winning percentage of the home team in the matches directed by the referees who took part in at least 15 matches in the Premier League\"" + ", \"result\": " + funfacts2_json + "}"
    return final_json

def funfacts3():
    cursor = conn.cursor()
    query = f"""
    Select *
    From
    (select p.fname, p.lname, avg_table.position as position, max_table.max_goals
    from (select T.position, max(T.goals) max_goals
            from (select p2.pid, pin2.position as position, count(*) as played_match, sum(pin2.total_goals) as goals
                                                    from team t2, player p2, plays_in pin2
                                                    where t2.lid = 140 and p2.tid=t2.tid and p2.pid = pin2.pid
                                                    group by p2.pid
                                                    having count(*) > 25) as T
            group by T.position) as max_table,
        (select p2.pid, pin2.position as position, count(*) as played_match, sum(pin2.total_goals) as goals
                                                    from team t2, player p2, plays_in pin2
                                                    where t2.lid = 140 and p2.tid=t2.tid and p2.pid = pin2.pid
                                                    group by p2.pid
                                                    having count(*) > 25) as avg_table,
            player p
    where max_table.max_goals = avg_table.goals and max_table.position=avg_table.position and p.pid = avg_table.pid) as final_table
    group by final_table.position"""
    cursor.execute(query)
    funfacts3_json = convert_to_json(cursor)
    final_json = "{\"explanation\": \"Top scorer and total goals for every position in La Liga\"" + ", \"result\": " + funfacts3_json + "}"
    return final_json

def funfacts4():
    cursor = conn.cursor()
    query = f"""
    SELECT L.name AS LeagueName, round(sum(A.Ave)/count(*), 2) AS AvgAge
    FROM league AS L, (SELECT T.lid, T.tid, T.name, avg(datediff(curdate(), P.birthdate))/365 AS Ave
                    FROM team AS T, player AS P
                    WHERE P.tid = T.tid
                    GROUP BY T.tid) AS A
    WHERE A.lid = L.lid
    GROUP BY L.lid
    ORDER BY AvgAge asc"""
    cursor.execute(query)
    funfacts4_json = convert_to_json(cursor)
    final_json = "{\"explanation\": \"The average age of players in every league in ascending order\"" + ", \"result\": " + funfacts4_json + "}"
    return final_json

def funfacts5():
    cursor = conn.cursor()
    query = f"""
    SELECT *
    FROM (SELECT l.name AS l_name, t.name AS t_name, p.fname, p.lname, round(sum(pi.rating)/count(*), 2) as avg_rating
        FROM plays_in AS pi, player AS p, team AS t, league AS l
        WHERE pi.pid = p.pid AND pi.is_captain = 1 AND p.tid = t.tid AND t.lid = l.lid
        GROUP BY p.pid
        ORDER BY avg_rating desc) AS Table1
    GROUP BY Table1.l_name"""
    cursor.execute(query)
    funfacts5_json = convert_to_json(cursor)
    final_json = "{\"explanation\": \"Team captains with best average rating from every league\"" + ", \"result\": " + funfacts5_json + "}"
    return final_json

def funfacts():
    final_json = "[" + funfacts1() + ", " + funfacts2() + ", " + funfacts3()+ ", " + funfacts4() + ", " + funfacts5() + "]" 
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