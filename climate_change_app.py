from flask import Flask, render_template, request
from flask import jsonify
import time, datetime
from AllReport import get_populated_map
import json, requests

app = Flask(__name__)

def fetch_current_weather():
    # Enter your API key here 
    api_key = "0c6527e1e073a790890aa665fb699de3"
    lat_n_long = "18.5204,73.8567"

    # base_url variable to store url 
    base_url = "https://api.darksky.net/forecast/"

    # Give city name 
    city_name = "Pune"

    complete_url = base_url + api_key + "/" + lat_n_long
    response = requests.get(complete_url) 

    result = json.loads(response.text)
    extracted_data = dict()
    extracted_data["temp"] = "{0:.2f}".format((result["currently"]["temperature"] - 32) / 1.8)
    extracted_data["humidity"] = "{0:.2f}".format(result["currently"]["humidity"] * 100)
    extracted_data["rainProbability"] = result["currently"]["precipProbability"]
    extracted_data["ozone"] = result["currently"]["ozone"]
    
    return extracted_data
    

@app.route('/')
def dashboard():    
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    given_date = request.args.get('date')
    date, month, year = given_date.split('/')
    result = get_populated_map(date, month, year)
    if(request.args.get('current') == 'true'):
        result["current"] = fetch_current_weather()
    return json.dumps(result)
