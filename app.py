from flask import Flask, render_template, json
import os
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

# Pages for each star sign
@app.route("/signs/<signs>")
def signs(signs):
    """Render signs.html with wiki info using microservice"""
    # retrieve Wiki info using Wiki scraper microservice
    response = requests.get("http://flip1.engr.oregonstate.edu:4753/" + signs + " (astrology)")
    wiki = json.loads(response.text)    
    # star sign symbols to display
    symbol = {
            "Aquarius": "♒︎",
            "Aries": "♈︎",
            "Cancer": "♋︎",
            "Capricorn": "♑︎",
            "Gemini": "♊︎",
            "Leo": "♌︎", 
            "Libra": "♎︎", 
            "Pisces": "♓︎", 
            "Sagittarius": "♐︎", 
            "Scorpio": "♏︎",
            "Taurus": "♉︎",
            "Virgo": "♍︎"
            }
    return render_template("signs.html", wiki=wiki, signs=signs, symbol=symbol[signs])

# Compatibility
@app.route("/compatibility/<sign>")
def compatibility(sign):
    """Render compatibility.html with online imgs about compatibility pulled for selected <sign>"""
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
    """Renders horoscope.html and gets daily horoscope using Aztro API"""
    url = "https://sameer-kumar-aztro-v1.p.rapidapi.com/"
    querystring = {
        "sign":sign, 
        "day":"yesterday"
        }
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
    """Renders travel.html with wiki page info using microservice for selected <sign>"""
    # variable to store travel locations and the corresponding place_id for each sign
    # find place_id at https://developers.google.com/places/place-id
    where = {
            "Aquarius": { "location": "Zakynthos", "place_id": "ChIJeWd9-9M7ZxMRN32bkyGz-GI" },
            "Aries": { "location": "Bondi Beach", "place_id": "ChIJn5qtqpytEmsRn2juKNy2hjQ" },
            "Cancer": { "location": "New Orleans", "place_id": "ChIJaS5FoBGmIIYRj77fFz8J_94" },
            "Capricorn": { "location": "Amalfi Coast", "place_id": "ChIJoXFMw62VOxMR3ExPyRTP6Ew" },
            "Gemini": { "location": "Lamma Island", "place_id": "ChIJNYBP5yVVATQREm7zX3gXth4" },
            "Leo": { "location": "Miami", "place_id": "ChIJrz_-m5q02YgR3MjgN6ttEfc" }, 
            "Libra": { "location": "Chefchaouen", "place_id": "ChIJO5BjVs0nCw0Rn_4Koj0Ssw0" },
            "Pisces": { "location": "Prague", "place_id": "ChIJw7ckbB6VC0cRnyUSr4g8zyo" },
            "Sagittarius": { "location": "Maldives", "place_id": "ChIJ57m5WKivEmsRVm0F9Unhr5s" },
            "Scorpio": { "location": "Hawaiʻi Volcanoes National Park", "place_id": "ChIJscm5wLZhUXkRJq6EPCZ7Wz4" },
            "Taurus": { "location": "Costa Rica", "place_id": "ChIJS_Wpm5xxoY8Rhkpczjlh5pU" }, 
            "Virgo": { "location": "Singapore", "place_id": "ChIJ6SvldwoR2jERHyZaM5NvIm4" }
            }

    # retrieve Wiki info for travel locations using Wiki scraper microservice
    response = requests.get("http://flip1.engr.oregonstate.edu:4753/" + where[sign]['location'])
    response_json = json.loads(response.text)
    if "History" in response_json:
        wiki_result = response_json["History"]
    else:
        wiki_result = response_json["Main"]

    # retrieve Google reviews for travel locations using Google review microservice
    response_rating = requests.get("http://flip3.engr.oregonstate.edu:33233/" + where[sign]['place_id'])
    response_json_rating = json.loads(response_rating.text)
    rating_result = []

    # get star rating and review text
    for i in range(len(response_json_rating)):
        rating_result.append((response_json_rating[i]["rating"], response_json_rating[i]["text"]))

    # Add star images based on rating result
    star_dict = {
        5:"⭐⭐⭐⭐⭐",
        4:"⭐⭐⭐⭐",
        3:"⭐⭐⭐",
        2:"⭐⭐",
        1:"⭐"
        }
    star_image = []
    for i in range(len(rating_result)):
        star_image.append(star_dict[rating_result[i][0]])
   
    # pull online imgs for travel locations for all signs
    img = {
            "Aquarius": "https://images.unsplash.com/photo-1570015329194-675ae0cf2516?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80",
            "Aries": "https://images.unsplash.com/photo-1557528263-efac13096ad1?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=764&q=80",
            "Cancer": "https://images.unsplash.com/photo-1626224336689-56a914fcb5b1?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=688&q=80",
            "Capricorn": "https://images.unsplash.com/photo-1610574138412-7bf28ade0222?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=735&q=80",
            "Gemini": "https://images.unsplash.com/photo-1597240890437-6d9c2d4c16aa?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=687&q=80",
            "Leo": "https://images.unsplash.com/photo-1530071291164-537d481750f4?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80", 
            "Libra": "https://images.unsplash.com/photo-1593350054764-2ea4054328ba?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=735&q=80", 
            "Pisces": "https://images.unsplash.com/photo-1600623471616-8c1966c91ff6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80", 
            "Sagittarius": "https://images.unsplash.com/photo-1590523277543-a94d2e4eb00b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1632&q=80", 
            "Scorpio": "https://images.unsplash.com/photo-1517508138376-d2ca9d34a908?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1173&q=80",
            "Taurus": "https://images.unsplash.com/photo-1620658927695-c33df6fb8130?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=735&q=80",
            "Virgo": "https://images.unsplash.com/photo-1516496636080-14fb876e029d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=688&q=80"
            }
    return render_template("travel.html", wiki_result=wiki_result, where=where[sign]['location'], sign=sign, img=img[sign], rating=rating_result, star_image=star_image)

# Listener
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 17995))
    app.run(host='0.0.0.0', port=port)
