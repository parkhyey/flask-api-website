# Dependencies
from flask import Flask, render_template, json, url_for, request, redirect
import os
import database.db_connector as db
from markupsafe import escape
import json
import requests
import datetime


# Configuration
app = Flask(__name__)
app.permanent_session_lifetime = datetime.timedelta(days=365)

# Routes
# Home


@app.route("/")
def root():
    """Render index.html as home page"""
    return render_template("index.html")


@app.route("/index.html")
def index():
    """Render index.html as home page"""
    return render_template("index.html")

# Compatibility
@app.route("/compatibility/<sign>")
def compatibility(sign):
    """Render compatibility.html"""
    return render_template("compatibility.html", sign=sign)

@app.route("/horoscope/<sign>")
def horoscope(sign):
    """Render horoscope.html"""
    return render_template("horoscope.html", sign=sign)

# Travel
@app.route("/travel/<sign>", methods=['POST', 'GET'])
def travel(sign):
    """Render travel.html"""
    # select location based on <sign>
    where = {"Aquarius": "Zakynthos", "Aries": "Bondi Beach", "Cancer": "New Orleans", "Capricorn": "Amalfi Coast", "Gemini": "Lamma Island",
             "Leo": "Miami", "Libra": "Chefchaouen", "Pisces": "Raja Ampat", "Sagittarius": "Cumbemayo", "Scorpio": "Hawaiʻi Volcanoes National Park", "Taurus": "Costa Rica", "Virgo": "Singapore"}
    # img = "<img src='../static/img/Zakinthos, Greece-unsplash.jpg/'>"
    response = requests.get(
        "http://flip1.engr.oregonstate.edu:4753/" + where[sign])
    todos = json.loads(response.text)
    wiki_result = todos["History"]
    return render_template("travel.html", wiki_result=wiki_result, where=where[sign], sign=sign)

# All Star Signs
@app.route("/signs/Aquarius.html")
def Aquarius():
    """Render Aquarius.html"""
    return render_template("signs/Aquarius.html")


@app.route("/signs/Aries")
def Aries():
    """Render Aries.html"""
    return render_template("signs/Aries.html")


@app.route("/signs/Cancer")
def Cancer():
    """Render Cancer.html"""
    return render_template("signs/Cancer.html")


@app.route("/signs/Capricorn")
def Capricorn():
    """Render Capricorn.html"""
    return render_template("signs/Capricorn.html")


@app.route("/signs/Gemini")
def Gemini():
    """Render Gemini.html"""
    return render_template("signs/Gemini.html")


@app.route("/signs/Leo")
def Leo():
    """Render Leo.html"""
    return render_template("signs/Leo.html")


@app.route("/signs/Libra")
def Libra():
    """Render Libra.html"""
    return render_template("signs/Libra.html")


@app.route("/signs/Pisces")
def Pisces():
    """Render Pisces.html"""
    return render_template("signs/Pisces.html")


@app.route("/signs/Sagittarius")
def Sagittarius():
    """Render Sagittarius.html"""
    return render_template("signs/Sagittarius.html")


@app.route("/signs/Scorpio")
def Scorpio():
    """Render Scorpio.html"""
    return render_template("signs/Scorpio.html")


@app.route("/signs/Taurus")
def Taurus():
    """Render Taurus.html"""
    return render_template("signs/Taurus.html")


@app.route("/signs/Virgo")
def Virgo():
    """Render Virgo.html"""
    return render_template("signs/Virgo.html")


# Listener
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 33233))    
    app.run(port=port, debug=True)
    # Use 'python app.py' or 'flask run' to run in terminal
