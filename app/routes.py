import os
import requests
from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            api_key = os.getenv('WEATHER_API_KEY')
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
            response = requests.get(url)
            if response.status_code == 200:
                weather_data = response.json()
            else:
                weather_data = {'error': 'City not found!'}
    return render_template('index.html', weather=weather_data)

