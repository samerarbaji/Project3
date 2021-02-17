# import necessary libraries
import os
from flask.globals import session
from flask_sqlalchemy import SQLAlchemy

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from sqlalchemy import create_engine, engine
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session






#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres:postgres@localhost:5432/project3"
# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")



    
   

@app.route("/api/NFLRoute")
#returns data of all odds from a requested team jsonified
def NFLRoute():
    session = Session(engine)
    results1 = session.query( 
    NFLRoute.Home_Team, 
    NFLRoute.Away_Team,
    NFLRoute.Winner_Home, 
    NFLRoute.Odds_Home, 
    NFLRoute.Odds_Away).all()
    
    result_list1 = []
    
    for result1 in results1:
        NFLdata = {
            "Home_Team": result1[1],
            "Away_Team": result1[2],
            "Winner_Home": result1[3],
            "Odds_Home": result1[4],
            "Odds_Away": result1[5]
        }

        result_list1.append(NFLdata)

    return jsonify(result_list1)



    
    

@app.route("/api/HorseRoute")
#returns horse betting jsonified data
def HorseRoute():
    session = Session(engine)
    results2 = session.query(
    HorseRoute.Track, 
    HorseRoute.Horse, 
    HorseRoute.BetType, 
    HorseRoute.Odds, 
    HorseRoute.Winner).all()
    
    result_list2 = []
    
    for result2 in results2:
        Horsedata = {
            "Track": result2[1],
            "Horse": result2[2],
            "BetType": result2[3],
            "Odds": result2[4],
            "Winner": result2[5]
        }

        result_list2.append(Horsedata)

    return jsonify(result_list2)


    
    

@app.route("/api/UFCRoute")
#returns UFC fight data jsonified
def UFCRoute():
    session = Session(engine)
    results3 = session.query( 
    UFCRoute.Red_Corner_Fighter, 
    UFCRoute.Blue_Corner_Fighter, 
    UFCRoute.Odds_Red_Fighter,
    UFCRoute.Odds_Blue_Fighter,
    UFCRoute.Winner).all()
    
    result_list3 = []
    
    for result3 in results3:
        UFCdata = {
            "Red_Corner_Fighter ": result3[1],
            "Blue_Corner_Fighter ": result3[2],
            "Odds_Red_Fighter": result3[3],
            "Odds_Blue_Fighter": result3[4],
            "Winner": result3[5]
        }

        result_list3.append(UFCdata)

    return jsonify(result_list3)

if __name__ == "__main__":
    app.run(debug=True)
