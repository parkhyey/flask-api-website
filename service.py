# Google review scraper
# Takes place_id and respond JSON data of reviews and ratings of the place
# Request format = url/ + place_id

from flask import Flask, jsonify
import googlemaps
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# service landing page with instruction
@app.route('/', methods=['GET'])
def home():
    text = "To use, add '/place_ID' after the above url. You can find place ID at https://developers.google.com/places/place-id. \
        For example, try '/ChIJW69I7FhZwokR61IbDPnsqTo'"
    return text

@app.route('/<place_id>', methods=['GET'])
def reviews(place_id):
    gmaps = googlemaps.Client(key='AIzaSyDj7clChH8kmGTe5uga8JUz21Q0AAm_9iA')  # personal google API key
    
    # find place_id at https://developers.google.com/places/place-id
    place = gmaps.place(place_id=place_id)  
    # empty list to hold dictionaries of reviews
    reviews = []  

    # pull only review texts and star ratings
    for i in range(len(place['result']['reviews'])):
        text = place['result']['reviews'][i]['text']
        rating = place['result']['reviews'][i]['rating']
        
        # customize response
        # set number of star ratings
        if rating >= 4:  
            reviews.append({'rating': rating,
                            'text': text})
        # set number of reviews to retrieve
        if len(reviews) == 10:  
            break
    response = jsonify(reviews)
    # fix CORS policy error
    response.headers.add('Access-Control-Allow-Origin', '*')  
    return response

# Listener
if __name__ == "__main__":
    app.run(host="flip3.engr.oregonstate.edu", port=33233)
