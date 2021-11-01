#from outscraper import ApiClient
from flask import Flask, jsonify, request
import os
import googlemaps

app = Flask(__name__)

#place_name = 'Mcdonalds Burwood'
#length = 2
@app.route('/', methods=['GET'])
def reviews():
    gmaps = googlemaps.Client(key='AIzaSyDj7clChH8kmGTe5uga8JUz21Q0AAm_9iA')
    place_name = 'Mcdonalds Burwood'
    places_result = gmaps.places(place_name)
    place_id = places_result['results'][0]['place_id']  # grab place id

    place = gmaps.place(place_id=place_id)  # use sigular form 'place'
    reviews = []  # empty list which will hold dictionaries of reviews
    while len(reviews) <= 1:
        for i in range(len(place['result']['reviews'])):
            text = place['result']['reviews'][i]['text']
            rating = place['result']['reviews'][i]['rating']
            if rating >= 5:  # retrieve 5 star reviews only
                reviews.append({'rating': rating,
                            'text': text})
    return jsonify(reviews)

# Listener
if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host="flip3.engr.oregonstate.edu", port=33133)
    #port = int(os.environ.get('PORT', 33133))
    #app.run(port=port, debug=True) # Use 'python app.py' or 'flask run' to run in terminal
