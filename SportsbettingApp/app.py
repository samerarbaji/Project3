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
def NFLRoute2():
    results1 = db.session.query(
    NFLRoute.Home_Win, 
    NFLRoute.Home_Team, 
    NFLRoute.Away_Team, 
    NFLRoute.Home_Odds, 
    NFLRoute.Away_odds).all()
    
    result_list1 = []
    
    for result in results1:
        NFLdata = {
            "Home Team":item[1],
            "Away Team":item[2],
            "Home Win":item[3],
            "Home Odds":item[4],
            "Away Odds":item[5]
        }

        result_list1.append(NFLdata)

    return jsonify(result_list1)


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
def NFLRoute():
    results1 = db.session.query(
    HorseRoute.Result, 
    HorseRoute.Horse, 
    HorseRoute.BetType, 
    HorseRoute.Track, 
    HorseRoute.Odds).all()
    
    result_list1 = []
    
    for result in results1:
        Horsedata = {
            "Track":item[1],
            "Horse":item[2],
            "Bet Type":item[3],
            "Odds":item[4],
            "Result":item[5]
        }

        result_list1.append(Horsedata)

    return jsonify(result_list1)

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
def UFCRoute2():
    results1 = db.session.query(
    NFLRoute.Winner1, 
    UFCRoute.Winner2, 
    UFCRoute.Red_Corner_Fighter1, 
    UFCRoute.Blue_Corner_Fighter1, 
    UFCRoute.Red_Fighter_odds1,
    UFCRoute.Blue_Fighter_odds1,
    UFCRoute.Red_Corner_Fighter2, 
    UFCRoute.Blue_Corner_Fighter2, 
    UFCRoute.Red_Fighter_odds2,
    UFCRoute.Blue_Fighter_odds2).all()
    
    result_list1 = []
    
    for result in results1:
        UFCdata = {
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

        result_list1.append(UFCdata)

    return jsonify(result_list1)

if __name__ == "__main__":
    app.run(debug=True)
