from flask import Flask, render_template, request, url_for,redirect,session
from reservations.reservation_dao import ReservationDao

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

@app.route('/formulaire')
def formulaire():
    return render_template("form.html")
@app.route('/add_reservation' , methods=['GET', 'POST'])
def add_reservation():
    if request.method == 'POST':
        event_name = request.form['event_name']
        user_name = request.form['user_name']
        num_tickets = request.form['num_tickets']

@app.route('/formulaire_Diner')
def formulaire_Diner():
    return render_template("formulaire_diner.html")

@app.route('/formulaire_Con')
def formulaire_Con():
    return render_template("formulaire_con.html")


@app.route("/ajouter_reservation", methods=['POST', 'GET'])
def ajouter_reservation():
        req = request.form
        print(req)
        message = None
        employe = None
        print("Methode.utilisee:" , request.method)
        if request.method == "POST": 
            nom_event = req['film']
            nom_util = req['nom_util']
            placeD = req['place']
            if nom_event == 'Selectionnez Votre Films' or nom_util == '' or placeD == '':
                message = "error"
            else:
                #employe = employe(nom_event, nom_util, placeD)
                ajouter = ReservationDao()
                message = ajouter.ajouter_reservation(nom_event, nom_util, placeD)
                print(message)
        return render_template("form.html", message=message, employe=employe)
    
@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/enregistrement')
def enregistrement():
    return render_template("ajout_util.html")

@app.route('/paiement')
def paiement():
    return render_template("paie.html")
