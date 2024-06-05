from flask import Flask, render_template, request
import requests

app = Flask(__name__)
api_key = '184b9613da0fb982cf38f6b3ec5f2eed'

def kelvin_to_fahrenheit(kelvin_temp):
    return round((kelvin_temp - 273.15) * 9/5 + 32, 2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET', 'POST'])
def weather_info():
    location = request.form['location']
    if location.isdigit():
        url = f"http://api.openweathermap.org/data/2.5/weather?zip={location}&appid={api_key}"
    else:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    weather = {
        'city': data['name'],
        'temperature': kelvin_to_fahrenheit(data['main']['temp']),
        'min_temperature': kelvin_to_fahrenheit(data['main']['temp_min']),
        'max_temperature': kelvin_to_fahrenheit(data['main']['temp_max']),
        'description': data['weather'][0]['description'].capitalize(),
        'icon': data['weather'][0]['icon'],
    }

    return render_template('weather.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)