from flask import Flask, render_template, request, url_for,redirect,session
from reservations.reservation_dao import ReservationDao
from utilisateurs.utilisateur_dao import UtilisateurDao
from paies.paie_dao import PaieDao

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
        message = None
        insertion = None
        if request.method == "POST": 
            nom_event = request.form.get('film')
            nom_util = request.form.get('nom_util')
            place = request.form.get('place')
            if  not nom_event or not nom_util or not place:
                message = "error"
            else:
                #employe = employe(nom_event, nom_util, placeD)
                ajouter = ReservationDao()
                insertion = ajouter.ajouter_reservation(nom_event, nom_util, place)
                message = "succes"
               # print(message)
        return render_template("form.html", message=message, insertion =insertion)


@app.route("/ajouter_reservation_concert", methods=['POST', 'GET'])
def ajouter_reservation_concert():
        message = None
        insertion = None
        if request.method == "POST": 
            nom_event = request.form.get('film')
            nom_util = request.form.get('nom_util')
            place = request.form.get('place')
            if  not nom_event or not nom_util or not place:
                message = "error"
            else:
                #employe = employe(nom_event, nom_util, placeD)
                ajouter = ReservationDao()
                insertion = ajouter.ajouter_reservation(nom_event, nom_util, place)
                message = "succes"
               # print(message)
        return render_template("formulaire_con.html", message=message, insertion =insertion)

@app.route("/ajouter_reservation_diner", methods=['POST', 'GET'])
def ajouter_reservation_diner():
        message = None
        insertion = None
        if request.method == "POST": 
            nom_event = request.form.get('film')
            nom_util = request.form.get('nom_util')
            place = request.form.get('place')
            if  not nom_event or not nom_util or not place:
                message = "error"
            else:
                #employe = employe(nom_event, nom_util, placeD)
                ajouter = ReservationDao()
                insertion = ajouter.ajouter_reservation(nom_event, nom_util, place)
                message = "succes"
               # print(message)
        return render_template("formulaire_diner.html", message=message, insertion =insertion)

@app.route("/ajouter_utilisateur", methods=['POST', 'GET'])
def ajouter_utilisateur():
        message = None
        insertion = None
        if request.method == "POST": 
            nom = request.form.get('Nom')
            prenom = request.form.get('Prenom')
            age = request.form.get('age')
            email = request.form.get('Email')
            password = request.form.get('Password')
            role = request.form.get('role')
            if  not nom or not prenom or not age or not email or not password or not role:
                message = "error"
            else:
                ajouter = UtilisateurDao()
                insertion = ajouter.add_utilisateur(nom, prenom, age, email, password, role)
                message = "succes"
    
        return render_template("formulaire_enreg.html", message=message, insertion =insertion)

@app.route("/paiement", methods=['POST', 'GET'])
def payer_evenement():
        message = None
        add=None
        if request.method == "POST":  
            Nomprenom = request.form.get('nom')
            Numerocarte = request.form.get('Numero')
            dateexp= request.form.get('date')
            cvv = request.form.get('CVV')
           
            if  not Nomprenom or not Numerocarte or not dateexp or not cvv:
                message = "error"
            else:  

                ajouter = PaieDao()
                add = ajouter.payer_evenement(Nomprenom, Numerocarte, dateexp, cvv)
                message = "succes"
        return render_template("paie.html", message=message, add=add)
    
@app.route("/login", methods=['POST','GET'])
def login():
    message = None
    if request.method == "POST":
        email=request.form.get()
        password = request.form.get()
        if not email or not password:
              message='error'
        else:
            user = UtilisateurDao()
            utilisateur = user.get_one(email, password)
            message ='success'

          
    return render_template("login.html")

@app.route('/enregistrement')
def enregistrement():
    return render_template("formulaire_enreg.html")

@app.route('/paiement')
def paiement():
    return render_template("paie.html")
