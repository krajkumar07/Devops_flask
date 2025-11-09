from flask import Flask , request , render_template, jsonify
from datetime import datetime
import json
app=Flask(__name__)

@app.route('/')
def home():
    day_of_week = datetime.today().strftime('%A')
    return render_template('index.html', day_of_week=day_of_week)

@app.route('/name')
def fun():
    name=request.values.get('name')
    age=request.values.get('age')
    restult={
        'name': name,
        'age':age
    }
    return restult

@app.route('/api', methods=['GET'])
def get_data():
    with open('data.json', 'r') as f:
        data = json.load(f)   
    return jsonify(data)      


if __name__=='__main__':
    app.run(debug=True)