from flask import Flask, render_template, request
from weather import current_weather
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    if not bool(city.strip()):
        city = "Kolkata"
    
    weather_details = current_weather(city)
    
    # if city not found by API
    if weather_details['cod'] != 200:
        return render_template('city-not-found.html')
    
    return render_template(
        "weather.html",
        title = weather_details["name"],
        status = weather_details['weather'][0]['description'].capitalize(),
        temp=f'{weather_details["main"]["temp"]:.1f}',
        feels_like=f'{weather_details["main"]["feels_like"]:.1f}')


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)