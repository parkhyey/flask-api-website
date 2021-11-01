from outscraper import ApiClient
from flask import Flask, jsonify, request
import os

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({'you': some_json}), 201
    else:
        return jsonify({'about':'Hellow world!'})
    
@app.route('/multi/<int:num>', methods=['GET'])
def get_multiply10(num):
    return jsonify({'result': num*10})

@app.route('/test', methods=['GET'])
def test():
    api_cliet = ApiClient(api_key='AIzaSyDj7clChH8kmGTe5uga8JUz21Q0AAm_9iA')
    response = api_cliet.google_maps_reviews(
    'https://www.google.com/maps/place/Do+or+Dive+Bar/@40.6867831,-73.9570104,17z/data=!3m2!4b1!5s0x89c25b96a0b10eb9:0xfe4f81ff249e280d!4m5!3m4!1s0x89c25b96a0b30001:0x643d0464b3138078!8m2!3d40.6867791!4d-73.9548217',
    language='en',
    limit=10)
    maps_result = api_cliet.google_maps_search('restaurants brooklyn usa')
    return response, maps_result

#api_cliet = ApiClient(api_key='AIzaSyDj7clChH8kmGTe5uga8JUz21Q0AAm_9iA')
#response = api_cliet.google_maps_reviews(
#    'https://www.google.com/maps/place/Do+or+Dive+Bar/@40.6867831,-73.9570104,17z/data=!3m2!4b1!5s0x89c25b96a0b10eb9:0xfe4f81ff249e280d!4m5!3m4!1s0x89c25b96a0b30001:0x643d0464b3138078!8m2!3d40.6867791!4d-73.9548217',
#    language='en',
#    limit=100
#)


# Listener
if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host="flip3.engr.oregonstate.edu", port=33133)
    #port = int(os.environ.get('PORT', 33133))
    #app.run(port=port, debug=True) # Use 'python app.py' or 'flask run' to run in terminal
