from flask import Flask, render_template, request, url_for,redirect,session
from reservations.reservation import Reservation
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

@app.route("/add_reservation", methods=['POST', 'GET'])
def add_reservation():
    if 'username' not in session:
        return redirect(url_for('login'))
    req = request.form 
    print(req)
    message= None
    employe= None
    print("Methode HTTP utilisee :", request.method)
    if request.method == "POST":
        nom = req['nom']
        prenom = req['prenom']
        matricule = req['matricule']
        fonction = req['fonction']
        departement = req['departement']
    if nom =='' or prenom =='' or matricule =='' or fonction =='' or departement =='':
            message="error"
    else:
            employe = employe(nom, prenom, matricule, fonction, departement)
            #print(employe.nom, employe.prenom, employe.matricule, employe.fonction, employe.departement)
            message = ajou
            print(message)
return render_template("add_employe.html", message=message, employe=employe)