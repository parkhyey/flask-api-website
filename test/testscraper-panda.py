import googlemaps
import pandas as pd

gmaps = googlemaps.Client(key='AIzaSyDj7clChH8kmGTe5uga8JUz21Q0AAm_9iA')
place_name = 'Mcdonalds Burwood'
places_result = gmaps.places(place_name)
place_id = places_result['results'][0]['place_id']

place = gmaps.place(place_id=place_id)  # use sigular form 'place'
reviews = []  # empty list which will hold dictionaries of reviews

for i in range(len(place['result']['reviews'])):
    text = place['result']['reviews'][i]['text']
    rating = place['result']['reviews'][i]['rating']

    reviews.append({'rating': rating,
                   'text': text
                    }
                   )

df = pd.DataFrame(reviews)
print(df)
