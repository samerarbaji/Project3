# import necessary libraries
from models import create_classes
import os
from flask import (
    Flask,
    render_template,
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
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get "sqlite:///db.sportsbetting.sqlite"

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

sportsbetting = create_classes(db)

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


# Query the database and send the jsonified results
@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        UFC_Red_Fighter1 = request.form["Red_Corner_Fighter1"]
        UFC_Blue_Fighter1 = request.form["Blue_Corner_Fighter1"]
        UFC_Winner1 = request.form["Winner1"]
        UFC_Red_Fighter_odds1 = request.form["Red_Fighter_odds1"]
        UFC_Blue_Fighter_odds1 = request.form["Blue_Fighter_odds1"]
        UFC_Red_Fighter2 = request.form["Red_Corner_Fighter2"]
        UFC_Blue_Fighter2 = request.form["Blue_Corner_Fighter2"]
        UFC_Winner2 = request.form["Winner2"]
        UFC_Red_Fighter_odds2 = request.form["Red_Fighter_odds2"]
        UFC_Blue_Fighter_odds2 = request.form["Blue_Fighter_odds2"]

        sportsbetting = Sportsbetting(UFC_Red_Fighter1=Red_Corner_Fighter1, 
                                      UFC_Blue_Fighter1=Blue_Corner_Fighter1,
                                      UFC_Winner1=Winner1,
                                      UFC_Red_Fighter_odds1=Red_Fighter_odds1,
                                      UFC_Blue_Fighter_odds1=Blue_Fighter_odds1,
                                      UFC_Red_Fighter2=Red_Corner_Fighter2, 
                                      UFC_Blue_Fighter2=Blue_Corner_Fighter2,
                                      UFC_Winner2=Winner2,
                                      UFC_Red_Fighter_odds2=Red_Fighter_odds2,
                                      UFC_Blue_Fighter_odds2=Blue_Fighter_odds2
                                      )
        db.session.add(sportsbetting)
        db.session.commit()
        return redirect("/", code=302)

    return render_template("form.html")

@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        Soccer_Match = request.form["Matchup_US_P"]
        Visitor_Odd = request.form["Visitor_Odd"]
        Draw_Odd = request.form["Draw_Odd"]
        Home_Odd = request.form["Home_Odd"]
        Soccer_Match_Result = request.form["True_Result"]

        sportsbetting = Sportsbetting(Soccer_Match=Matchup_US_P, 
                                      Soccer_Visitor_Odd=Visitor_Odd,
                                      Soccer_Draw_Odd=Draw_Odd,
                                      Soccer_Home_Odd=Home_Odd,
                                      Soccer_Match_Result=True_Result
                                      )
        db.session.add(sportsbetting)
        db.session.commit()
        return redirect("/", code=302)

    return render_template("form.html")

@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        Horse = request.form["Horse"]
        Horse_Odds = request.form["Odds"]
        Horse_Bet_Type = request.form["Bet Type"]
        Horse_Result = request.form["Result"]

        sportsbetting = Sportsbetting(Horse=Horse, 
                                      Horse_Odds=Odds,
                                      Horse_Bet_Type=Bet Type,
                                      Horse_Result=Result
                                      )
        db.session.add(sportsbetting)
        db.session.commit()
        return redirect("/", code=302)

    return render_template("form.html")

@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        Football_Home_Team = request.form["Home Team"]
        Football_Away_Team = request.form["Away Team"]
        Football_Home_Odds = request.form["Home Odds Open"]
        Football_Away_Odds = request.form["Away Odds Open"]
        Football_Home_Win = request.form["Home Win"]

        sportsbetting = Sportsbetting(Football_Home_Team=Home Team, 
                                      Football_Away_Team=Away Team,
                                      Football_Home_Odds=Home Odds Open,
                                      Football_Away_Odds=Away Odds Open,
                                      Football_Home_Win=Home Win
                                      )
        db.session.add(sportsbetting)
        db.session.commit()
        return redirect("/", code=302)

    return render_template("form.html")




    return jsonify(pet_data)


if __name__ == "__main__":
    app.run()
