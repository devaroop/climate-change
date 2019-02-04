from flask import Flask, render_template, request
from flask import jsonify
import time, datetime
from AllReport import get_populated_map
import json

app = Flask(__name__)


def fetch_current_weather(date):
    # Enter your API key here 
    api_key = "0c6527e1e073a790890aa665fb699de3"
    lat_n_long = "18.5204,73.8567"

    # base_url variable to store url 
    base_url = "https://api.darksky.net/forecast/"

    # Give city name 
    city_name = "Pune"

    complete_url = base_url + api_key + "/" + lat_n_long
    response = requests.get(complete_url) 

    #x = json.dumps(json.loads(response.text), indent=4, ensure_ascii=False)
    print(json.loads(response.text))
    

@app.route('/')
def dashboard():    
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    #    import pdb;pdb.set_trace()
    given_date = request.args.get('date')
    date, month, year = given_date.split('/')
    result = get_populated_map(date, month, year)
    return json.dumps(result)
