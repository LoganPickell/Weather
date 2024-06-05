from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def weather():
    city = 'London'
    api_key = '184b9613da0fb982cf38f6b3ec5f2eed'
    url = f"http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather = {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
    else:
        weather = {'error': 'Unable to fetch weather data'}

    return render_template('weather.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
