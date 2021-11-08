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
@app.route("/compatibility.html")
def compatibility():
    """Render compatibility.html"""
    return render_template("compatibility.html")

# Horoscope
@app.route("/horoscope.html")
def horoscope():
    """Render horoscope.html"""
    return render_template("horoscope.html")

# Travel
@app.route("/travel.html")
def travel():
    """Render travel.html"""
    return render_template("travel.html")

# All Star Signs
@app.route("/signs/Aquarius.html")
def Aquarius():
    """Render Aquarius.html"""
    return render_template("signs/Aquarius.html")

@app.route("/signs/Aries.html")
def Aries():
    """Render Aries.html"""
    return render_template("signs/Aries.html")

@app.route("/signs/Cancer.html")
def Cancer():
    """Render Cancer.html"""
    return render_template("signs/Cancer.html")

@app.route("/signs/Capricorn.html")
def Capricorn():
    """Render Capricorn.html"""
    return render_template("signs/Capricorn.html")

@app.route("/signs/Gemini.html")
def Gemini():
    """Render Gemini.html"""
    return render_template("signs/Gemini.html")

@app.route("/signs/Leo.html")
def Leo():
    """Render Leo.html"""
    return render_template("signs/Leo.html")

@app.route("/signs/Libra.html")
def Libra():
    """Render Libra.html"""
    return render_template("signs/Libra.html")

@app.route("/signs/Pisces.html")
def Pisces():
    """Render Pisces.html"""
    return render_template("signs/Pisces.html")

@app.route("/signs/Sagittarius.html")
def Sagittarius():
    """Render Sagittarius.html"""
    return render_template("signs/Sagittarius.html")

@app.route("/signs/Scorpio.html")
def Scorpio():
    """Render Scorpio.html"""
    return render_template("signs/Scorpio.html")

@app.route("/signs/Taurus.html")
def Taurus():
    """Render Taurus.html"""
    return render_template("signs/Taurus.html")

@app.route("/signs/Virgo.html")
def Virgo():
    """Render Virgo.html"""
    return render_template("signs/Virgo.html")

@app.route("/reviews.html")
def reviews():
    """Render reviews.html"""
    return render_template("reviews.html")

@app.route('/this',methods = ['POST', 'GET'])
def result():
   data = "Zakynthos"
   response = requests.get("http://flip1.engr.oregonstate.edu:4753/"+data)
   todos = json.loads(response.text)
   return str(todos)

@app.route("/testing.html")
def testing():
    return render_template("testing.html")

@app.route("/testing2.html", methods = ['POST', 'GET'])
def testing2():
    user = request.args.get('nm')
    return redirect(url_for('success',name = user))
    #return render_template("testing2.html")

# Listener
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 33233))
    app.run(port=port, debug=True) # Use 'python app.py' or 'flask run' to run in terminal
