from flask import Flask, jsonify
import requests

app = Flask(__name__)

API_KEY = 'd23cc393ef4def35ffa330cea1ba3239'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/weather/<city>', methods=['GET'])
def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return jsonify({
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        })
    else:
        return jsonify({'error': 'City not found'}), 404

if __name__ == 'main':
    app.run(host='0.0.0.0', port=5000)
