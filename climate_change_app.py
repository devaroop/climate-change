from flask import Flask, render_template, request
from flask_json import FlaskJSON, json_response

app = Flask(__name__)
FlaskJSON(app)

@app.route('/')
def dashboard():    
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    import pdb;pdb.set_trace()
    given_date = request.args.get('date')
    date, month, year = given_date.split('/')
    result = fetch_data_for(day, month, year)
    return json_response(result)
