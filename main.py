from flask import Flask, render_template

app=Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/weather')
def weather():
    return render_template("weather.html")

@app.route('/bmi')
def bmi():
    return render_template("bmi.html")

if __name__=='__main__':
    app.run(host='127.0.0.1', debug=True)