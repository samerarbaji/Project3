# import necessary libraries
import os
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine, func)
from flask import (
    Flask,
    render_template,
    url_for,
    json,
    jsonify,
    request,
    redirect)




#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres:samer123@localhost:5432/project2_db"

# Remove tracking modifications
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")



    
   

@app.route("/api/NFLRoute")
#returns data of all odds from a requested team jsonified
def NFLRoute():
    
    results1 = session.query(
    NFLRoute.Home_Win, 
    NFLRoute.Home_Team, 
    NFLRoute.Away_Team, 
    NFLRoute.Home_Odds, 
    NFLRoute.Away_odds).all()
    
    result_list1 = []
    
    for result1 in results1:
        NFLdata = {
            "Home Team": result1[1],
            "Away Team": result1[2],
            "Home Win": result1[3],
            "Home Odds": result1[4],
            "Away Odds": result1[5]
        }

        result_list1.append(NFLdata)

    return jsonify(result_list1)



    
    

@app.route("/api/HorseRoute")
#returns horse betting jsonified data
def HorseRoute():
    
    results2 = session.query(
    HorseRoute.Result, 
    HorseRoute.Horse, 
    HorseRoute.BetType, 
    HorseRoute.Track, 
    HorseRoute.Odds).all()
    
    result_list2 = []
    
    for result2 in results2:
        Horsedata = {
            "Track": result2[1],
            "Horse": result2[2],
            "Bet Type": result2[3],
            "Odds": result2[4],
            "Result": result2[5]
        }

        result_list2.append(Horsedata)

    return jsonify(result_list2)


    
    

@app.route("/api/UFCRoute")
#returns UFC fight data jsonified
def UFCRoute():
   
    results3 = session.query(
    UFCRoute.Winner1, 
    UFCRoute.Winner2, 
    UFCRoute.Red_Corner_Fighter1, 
    UFCRoute.Blue_Corner_Fighter1, 
    UFCRoute.Red_Fighter_odds1,
    UFCRoute.Blue_Fighter_odds1,
    UFCRoute.Red_Corner_Fighter2, 
    UFCRoute.Blue_Corner_Fighter2, 
    UFCRoute.Red_Fighter_odds2,
    UFCRoute.Blue_Fighter_odds2).all()
    
    result_list3 = []
    
    for result3 in results3:
        UFCdata = {
            "Red Corner Fighter 1": result3[1],
            "Blue Corner Fighter 1": result3[2],
            "Red Fighter 1 Odds": result3[3],
            "Blue Fighter 1 Odds": result3[4],
            "Winner of Fight 1": result3[5],
            "Red Corner Fighter 2": result3[6],
            "Blue Corner Fighter 2": result3[7],
            "Red Fighter 2 Odds": result3[8],
            "Blue Fighter 2 Odds": result3[9],
            "Winner of Fight 2": result3[10]
        }

        result_list3.append(UFCdata)

    return jsonify(result_list3)

if __name__ == "__main__":
    app.run(debug=True)
