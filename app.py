from flask import Flask, render_template, request, url_for

app= Flask(__name__)
app.secret_key= "cle secret"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/evenements')
def evenements():
    return render_template("evenements.html")

@app.route('/form_events')
def form_events():
    return render_template("form_events.html")