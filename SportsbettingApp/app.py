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
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgres:postgres@localhost:5432/project3"
# Remove tracking modifications
from sqlalchemy import create_engine
engine = create_engine('postgres://bwxormoq:eKtYIkVXGTjFJYwGePZHd1aSVOFZtjkP@ziggy.db.elephantsql.com:5432/bwxormoq')

Base = automap_base()
Base.prepare(engine, reflect=True)
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#db = SQLAlchemy(app)

NFL_Route=Base.classes.NFL
Horse_Route=Base.classes.Horseracing
UFC_Route=Base.classes.UFC1

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/NFL")
#returns data of all odds from a requested team jsonified
def NFLRoute():
    session = Session(engine)
    results1 = session.query( 
    NFL_Route.Home_Team, 
    NFL_Route.Away_Team,
    NFL_Route.Winner_Home, 
    NFL_Route.Odds_Home, 
    NFL_Route.Odds_Away).all()

    session.close()

    result_list1 = []
    
    for Home_Team, Away_Team, Winner_Home, Odds_Home, Odds_Away in results1:
        NFL = {}
        NFL["Home_Team"] = Home_Team
        NFL["Away_Team"] = Away_Team
        NFL["Winner_Home"] = Winner_Home
        NFL["Odds_Home"] = Odds_Home
        NFL["Odds_Away"] = Odds_Away
        result_list1.append(NFL)

    return jsonify(result_list1)


@app.route("/api/Horseracing")
#returns horse betting jsonified data
def HorseRoute():
    session = Session(engine)
    results2 = session.query(
    Horse_Route.Track, 
    Horse_Route.Horse, 
    Horse_Route.BetType, 
    Horse_Route.Odds, 
    Horse_Route.Winner).all()

    session.close()
    
    result_list2 = []
    
    for Track, Horse, BetType, Odds, Winner in results2:
        Horseracing = {}
        Horseracing["Track"] = Track
        Horseracing["Horse"] = Horse
        Horseracing["BetType"] = BetType
        Horseracing["Odds"] = Odds
        Horseracing["Winner"] = Winner
        result_list2.append(Horseracing)

    return jsonify(result_list2)


@app.route("/api/UFC1")
#returns UFC fight data jsonified
def UFCRoute():
    session = Session(engine)
    results3 = session.query(     
    UFC_Route.Red_Corner_Fighter, 
    UFC_Route.Blue_Corner_Fighter, 
    UFC_Route.Odds_Red_Fighter,
    UFC_Route.Odds_Blue_Fighter,
    UFC_Route.Winner,
    UFC_Route.index).all()

    session.close()
    
    result_list3 = []
    
    for Red_Corner_Fighter, Blue_Corner_Fighter, Odds_Red_Fighter, Odds_Blue_Fighter, Winner, index in results3:
        UFC1 = {}
        UFC1["index"] = index
        UFC1["Red_Corner_Fighter"] = Red_Corner_Fighter
        UFC1["Blue_Corner_Fighter"] = Blue_Corner_Fighter
        UFC1["Odds_Red_Fighter"] = Odds_Red_Fighter
        UFC1["Odds_Blue_Fighter"] = Odds_Blue_Fighter
        UFC1["Winner"] = Winner
        result_list3.append(UFC1)

    return jsonify(result_list3)


if __name__ == "__main__":
    app.run(debug=True)
