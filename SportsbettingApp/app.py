# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect,
    url_for)
from flask_sqlalchemy import SQLAlchemy





#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sportsbetting.db"

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


class NFLRoute(db.Model):
    __tablename__ = 'NFL betting'

    Home_Win = db.Column(db.String(64), primary_key=True)
    Home_Team = db.Column(db.String(64))
    Away_Team = db.Column(db.String(64))
    Away_Odds = db.Column(db.String(64))
    Home_Odds = db.Column(db.String(64))
    
    def __repr__(self):
        return '<tStats %r>' % (self.name)

@app.route("/api/NFLRoute")
#returns data of all odds from a requested team jsonified
def NFLRoute(TeamName):
    #creates a tuple of NFL records of the team name requested
    TeamData = db.session.query(NFL_Opening_Odds2).filter(Home_Team == TeamName or Away_Team == TeamName).all()
    
    TeamOutput = []
    #loop through values in NFLData and put it in correct format jsonify
    for item in TeamData:
        output = {
            "Home Team":item[2],
            "Away Team":item[3],
            "Home Win":item[4],
            "Home Odds":item[5],
            "Away Odds":item[6]
        }
        TeamOutput.append(output)

    return jsonify(TeamOutput)

class HorseRoute(db.Model):
    __tablename__ = 'Horse betting'

    Result = db.Column(db.String(64), primary_key=True)
    Horse = db.Column(db.String(64))
    BetType = db.Column(db.String(64))
    Track= db.Column(db.String(64))
    Odds = db.Column(db.String(64))
    
    def __repr__(self):
        return '<tStats %r>' % (self.name)

@app.route("/api/HorseRoute")
#returns horse betting jsonified data
def HorseRoute():
    HorseData = db.session.query(tips2).all()

    HorseOutput = []

    for item in HorseData:
        output ={
            "Track":item[4],
            "Horse":item[5],
            "Bet Type":item[6],
            "Odds":item[7],
            "Result":item[8]
        }
        HorseOutput.append(output)
     
    return jsonify(HorseOutput)

class UFCRoute(db.Model):
    __tablename__ = 'UFC betting'

    Winner1 = db.Column(db.String(64), primary_key=True)
    Winner2 = db.Column(db.String(64), primary_key=True)
    Red_Corner_Fighter1 = db.Column(db.String(64))
    Blue_Corner_Fighter1 = db.Column(db.String(64))
    Red_Fighter_odds1 = db.Column(db.String(64))
    Blue_Fighter_odds1 = db.Column(db.String(64))
    Red_Corner_Fighter2 = db.Column(db.String(64))
    Blue_Corner_Fighter2 = db.Column(db.String(64))
    Red_Fighter_odds2 = db.Column(db.String(64))
    Blue_Fighter_odds2 = db.Column(db.String(64))
    
    def __repr__(self):
        return '<tStats %r>' % (self.name)

@app.route("/api/UFCRoute")
#returns UFC fight data jsonified
def UFCRoute():
    UFCData = db.session.query(ufcfinal_df2).all()

    UFCOutput = []

    for item in UFCData:
        output ={
            "Red Corner Fighter 1":item[1],
            "Blue Corner Fighter 1":item[2],
            "Red Fighter 1 Odds":item[3],
            "Blue Fighter 1 Odds":item[4],
            "Winner of Fight 1":item[5],
            "Red Corner Fighter 2":item[6],
            "Blue Corner Fighter 2":item[7],
            "Red Fighter 2 Odds":item[8],
            "Blue Fighter 2 Odds":item[9],
            "Winner of Fight 2":item[10]
        }
        UFCOutput.append(output)
     
    return jsonify(UFCOutput)

if __name__ == "__main__":
    app.run()
