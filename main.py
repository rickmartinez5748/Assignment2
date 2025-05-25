from flask import Flask, render_template, request
from bmi import calculate_bmi 
import requests
import json

app=Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/weather')
def weather():
    city="sudbury"
    key="884db306856a765ed4d4ecd3f01a7e3b"
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
    response=requests.get(url)
    data=response.json()
    temperature=round(data["main"]["temp"]-273.15,2)
    description=data["weather"][0]["description"]
    return render_template("weather.html", temperature=temperature, description=description)

@app.route("/bmi", methods=["GET", "POST"])
def bmi_page():
    bmi_result = None
    if request.method == "POST":
        weight = request.form.get("weight")
        height = request.form.get("height")
        bmi_result = calculate_bmi(weight, height) 
    return render_template("bmi.html", bmi=bmi_result)

if __name__=='__main__':
    app.run(host='127.0.0.1', debug=True)