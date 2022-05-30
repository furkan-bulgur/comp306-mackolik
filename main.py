from flask import Flask
import mysql.connector
import json
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
conn = mysql.connector.connect(user=os.environ.get("DB_USER"), 
                                password=os.environ.get("PASSWORD"),
                                host=os.environ.get("HOST"),
                                database=os.environ.get("DATABASE"))


@app.route('/')
def premier_league_teams():
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM team WHERE lid=39")
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    result = cursor.fetchall()
    json_data=[]
    for result in result:
            json_data.append(dict(zip(row_headers,result)))
    return json.dumps(json_data)

if __name__ == "__main__":
    app.run(host='localhost', port=5001)