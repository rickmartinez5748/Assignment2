from flask import Flask, render_template

app=Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/experience')
def experience():
    return render_template("experience.html")

if __name__=='__main__':
    app.run(host='127.0.0.1', debug=True)