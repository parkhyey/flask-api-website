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

# Listener
if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host="flip3.engr.oregonstate.edu", port=33133)
    #port = int(os.environ.get('PORT', 33133))
    #app.run(port=port, debug=True) # Use 'python app.py' or 'flask run' to run in terminal
