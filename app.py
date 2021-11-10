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


@app.route("/index")
def index():
    """Render index.html as home page"""
    return render_template("index.html")


# Compatibility
@app.route("/compatibility/<sign>")
def compatibility(sign):
    """Render compatibility.html"""
    img = {
            "Aquarius": "https://numerologysign.com/wp-content/uploads/2020/09/Aquarius-Compatibility-Chart-Zodiac-Sign-Percentages-768x819.png.webp",
            "Aries": "https://numerologysign.com/wp-content/uploads/2020/09/Aries-Compatibility-Chart-Zodiac-Sign-Percentages-768x819.png.webp",
            "Cancer": "https://numerologysign.com/wp-content/uploads/2020/09/Cancer-Compatibility-Chart-Zodiac-Sign-Percentages-768x819.png.webp",
            "Capricorn": "https://numerologysign.com/wp-content/uploads/2020/09/Capricorn-Compatibility-Chart-and-Zodiac-Sign-Percentages-768x819.png.webp",
            "Gemini": "https://numerologysign.com/wp-content/uploads/2020/09/Gemini-Compatibility-Chart-and-Zodiac-Sign-Percentages-768x819.png.webp",
            "Leo": "https://numerologysign.com/wp-content/uploads/2020/09/Leo-Compatibility-Chart-and-Zodiac-Sign-Percentages-768x819.png.webp", 
            "Libra": "https://numerologysign.com/wp-content/uploads/2020/09/Libra-Compatibility-Chart-Zodiac-Sign-Percentages-768x819.png.webp", 
            "Pisces": "https://numerologysign.com/wp-content/uploads/2020/09/Pisces-Compatibility-Chart-Zodiac-Sign-Percentages-768x819.png.webp", 
            "Sagittarius": "https://numerologysign.com/wp-content/uploads/2020/09/Sagittarius-Compatibility-Chart-and-Zodiac-Sign-Percentages-768x819.png.webp", 
            "Scorpio": "https://numerologysign.com/wp-content/uploads/2020/09/Scorpio-Compatibility-Chart-and-Zodiac-Sign-Percentages-768x819.png.webp",
            "Taurus": "https://numerologysign.com/wp-content/uploads/2020/09/Taurus-Compatibility-Chart-and-Zodiac-Sign-Percentages-768x819.png.webp",
            "Virgo": "https://numerologysign.com/wp-content/uploads/2020/09/Virgo-Compatibility-Chart-and-Zodiac-Sign-Percentages-768x819.png.webp"
            }
    return render_template("compatibility.html", sign=sign, img=img[sign])


# Horoscope
@app.route("/horoscope/<sign>", methods=['POST', 'GET'])
def horoscope(sign):
    """Gets daily horoscope from Aztro API"""
    url = "https://sameer-kumar-aztro-v1.p.rapidapi.com/"
    querystring = {"sign":sign, "day":"yesterday"}
    headers = {
        'x-rapidapi-host': "sameer-kumar-aztro-v1.p.rapidapi.com",
        'x-rapidapi-key': "c232a67fd7msh5d9690a65c5ee5ep19f6a0jsn958fd5326d04"
        }
    response = requests.request("POST", url, headers=headers, params=querystring)
    horoscope = json.loads(response.text)
    img = {
            "Aquarius": "../static/img/aquarius.jpg",
            "Aries": "../static/img/aries.jpg",
            "Cancer": "../static/img/cancer.jpg",
            "Capricorn": "../static/img/capricorn.jpg",
            "Gemini": "../static/img/gemini.jpg",
            "Leo": "../static/img/leo.jpg", 
            "Libra": "../static/img/libra.jpg", 
            "Pisces": "../static/img/pisces.jpg", 
            "Sagittarius": "../static/img/sagittarius.jpg", 
            "Scorpio": "../static/img/scorpio.jpg",
            "Taurus": "../static/img/taurus.jpg",
            "Virgo": "../static/img/virgo.jpg"
            }
    return render_template("horoscope.html", sign=sign, horoscope=horoscope, img=img[sign])


# Travel
@app.route("/travel/<sign>", methods=['POST', 'GET'])
def travel(sign):
    """Scrapes and returns wiki page history section for the places assigned for each sign"""
    # locations for each sign
    where = {
            "Aquarius": { "location": "Zakynthos", "place_id": "ChIJW69I7FhZwokR61IbDPnsqTo" },
            "Aries": { "location": "Bondi Beach", "place_id": "ChIJW69I7FhZwokR61IbDPnsqTo" },
            "Cancer": { "location": "New Orleans", "place_id": "ChIJW69I7FhZwokR61IbDPnsqTo" },
            "Capricorn": { "location": "Amalfi Coast", "place_id": "ChIJW69I7FhZwokR61IbDPnsqTo" },
            "Gemini": { "location": "Lamma Island", "place_id": "ChIJW69I7FhZwokR61IbDPnsqTo" },
            "Leo": { "location": "Miami", "place_id": "ChIJW69I7FhZwokR61IbDPnsqTo" }, 
            "Libra": { "location": "Chefchaouen", "place_id": "ChIJW69I7FhZwokR61IbDPnsqTo" },
            "Pisces": { "location": "ZakRaja Ampatynthos", "place_id": "ChIJW69I7FhZwokR61IbDPnsqTo" }, 
            "Sagittarius": { "location": "Himalaya", "place_id": "ChIJW69I7FhZwokR61IbDPnsqTo" },
            "Scorpio": { "location": "Hawaiʻi Volcanoes National Park", "place_id": "ChIJW69I7FhZwokR61IbDPnsqTo" },
            "Taurus": { "location": "Costa Rica", "place_id": "ChIJW69I7FhZwokR61IbDPnsqTo" },
            "Virgo": { "location": "Singapore", "place_id": "ChIJW69I7FhZwokR61IbDPnsqTo" }
            }

    # Wiki service
    response = requests.get("http://flip1.engr.oregonstate.edu:4753/" + where[sign]['location'])
    response_json = json.loads(response.text)
    wiki_result = response_json["History"]

    # Google rating service
    response_rating = requests.get("http://flip3.engr.oregonstate.edu:33133/" + where[sign]['place_id'])
    response_json2 = json.loads(response_rating.text)
    print(response_json2)
    rating_result = []
    # rating_result = [response_json2[0]["text"],response_json2[1]["text"]]
    for i in range(len(response_json2)):
        rating_result.append(response_json2[i]["text"])
    # pull imgs online for each sign
    img = {
            "Aquarius": "https://images.unsplash.com/photo-1570015329194-675ae0cf2516?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80",
            "Aries": "https://images.unsplash.com/photo-1557528263-efac13096ad1?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=764&q=80",
            "Cancer": "https://images.unsplash.com/photo-1626224336689-56a914fcb5b1?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=688&q=80",
            "Capricorn": "https://images.unsplash.com/photo-1610574138412-7bf28ade0222?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=735&q=80",
            "Gemini": "https://images.unsplash.com/photo-1597240890437-6d9c2d4c16aa?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=687&q=80",
            "Leo": "https://images.unsplash.com/photo-1530071291164-537d481750f4?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80", 
            "Libra": "https://images.unsplash.com/photo-1593350054764-2ea4054328ba?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=735&q=80", 
            "Pisces": "https://images.unsplash.com/photo-1601844075967-c1376c021732?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=687&q=80", 
            "Sagittarius": "https://images.unsplash.com/photo-1623127557678-7546ee28656f?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=687&q=80", 
            "Scorpio": "https://images.unsplash.com/photo-1517508138376-d2ca9d34a908?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1173&q=80",
            "Taurus": "https://images.unsplash.com/photo-1620658927695-c33df6fb8130?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=735&q=80",
            "Virgo": "https://images.unsplash.com/photo-1516496636080-14fb876e029d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=688&q=80"
            }

    return render_template("travel.html", wiki_result=wiki_result, where=where[sign]['location'], sign=sign, img=img[sign], rating=rating_result)


# All Star Signs
@app.route("/signs/Aquarius")
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
    app.run(host="localhost", port=7777)
    # port = int(os.environ.get('PORT', 33233))
    # app.run(port=port, debug=True)
    # Use 'python app.py' or 'flask run' to run in terminal
