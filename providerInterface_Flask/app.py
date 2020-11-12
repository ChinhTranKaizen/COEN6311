from flask import Flask, redirect, url_for, render_template, request, session, abort, jsonify
# To start server :
# First: C:\Users\OS\COEN6311\car-rental-all-class
# Then: ./mvnw spring-boot:run
# Please execute: "$env:FLASK_RUN_PORT = 5001" to change your port
from datetime import date, datetime

import requests, uuid, json

app = Flask(__name__)
app.secret_key = "coen6311"
#The first page when starting provider interface: return the log_in page
@app.route("/")
def index():
    # This should return the login page if login successfully, return the index.html page
    return render_template("log_in.html",login_token = session.get('token'))

#This is a in-between route that processes log-in information
@app.route("/login", methods =["POST"])
def login():
    #Set up the parameters for getting all employees from the database to process log-in information
    url = "http://localhost:3001/employees"
    r = requests.request("GET",url).json()
    username = str(request.form.get("username"))
    password = str(request.form.get("password"))

    #Check for every responses in the response message, if there is a match, change the token to True
    for response in r:
        if response["name"] == username and response["password"]==password:
            session['token'] = True
            break
    if session.get('token') is not None:
        return render_template("index.html", log_in = session.get('token')) #log in sucessfully
    else:
        return render_template("bad_log_in.html") #log in fails

#A route to open registration form html page
@app.route("/register_form")
def register_form():
    return render_template("register.html")

#An in-between route that processes registration data and send to Java Spring boot
@app.route("/register", methods = ["POST"])
def register():
    #Preparing the parameters to send the Java spring boot server
    url = 'http://localhost:3001/employees'
    params = {'id': str(request.form.get("id")),
        'name' : str(request.form.get("fullname")),
        'password' : str(request.form.get("password")),
        'position' : str(request.form.get("position")),
        'email' : str(request.form.get("email"))
        }

    headers = {'content-type': 'application/json'}
    #make the requests
    r = requests.request("POST", url, data = json.dumps(params),headers = headers)
    #Depends on if the registration is successful or not, return it to display in log_in html
    return render_template("log_in.html", response_status = r.status_code)

#An html page that displays the car list, whose content is fetched from the server
#This also acts as an in-between page to process adding cars to the fleet requests from add_car_form below
@app.route("/car_list", methods=["GET","POST"])
def car_list():
    #When a form sends post request to this route then the code below prep the parameters to send to the server.
    if request.method == "POST":
        url = "http://localhost:3001/cars"
        date1 = str(request.form.get("EntryDate"))
        date2 = str(request.form.get("ReleaseYear"))
        date3 = datetime.now().strftime("%Y-%m-%d")
        if int(date1[0:4])<int(date2):
            return abort(jsonify(message = "The entry year cannot be smaller than the release year."),400)
        else:
            params = {'id': str(request.form.get("CarID")),
                'entrydate': str(request.form.get("EntryDate")),
                'kmdriven': str(request.form.get("KmDriven")),
                'releaseyear': str(request.form.get("ReleaseYear")),
                'condition': str(request.form.get("CarCondition")),
                'pricekm': str(request.form.get("PriceKm")),
                "state": str(request.form.get("CarState")),
                "brand": str(request.form.get("Brand")),
                "model": "",
                "type": str(request.form.get("Type")),
                "priceday": str(request.form.get("PriceDay"))
                }
            headers = {'content-type': 'application/json'}
            r = requests.request('POST',url, data = json.dumps(params), headers=headers)

    #Prep the parameters to send GET requests to the car
    url = "http://localhost:3001/cars"
    r = requests.request("GET",url).json()

    return render_template("car_list.html",responses = r)

#This redirects to a add_car_form page where you can fill in the form. upon submission the data is directed to car_list
@app.route("/add_car_form")
def add_car_form():

    today = date.today()
    d1 = today.strftime("%Y-%m-%d")

    return render_template("add_car_form.html",today = d1)

#This is an route the directs to the confirmation for delete page with all the information of the targeted car
@app.route("/delete_confirmation", methods=["POST"])
def delete_confirmation():
    deletecar = {
        'deleteID' : str(request.form.get("DeleteID")),
        'entryDate' : str(request.form.get("DeleteEntrydate")),
        'kmDriven' : str(request.form.get("DeleteKmdriven")),
        'releaseYear' : str(request.form.get("DeleteReleaseyear")),
        'condition' : str(request.form.get("DeleteCondition")),
        'priceKm' : str(request.form.get("DeletePricekm")),
        'brand': str(request.form.get("DeleteBrand")),
        'type' : str(request.form.get("DeleteType")),
        'state' : str(request.form.get("DeleteState")),
        'priceday' : str(request.form.get("DeletePriceday"))
    }

    return render_template("delete_confirmation.html", deletecar = deletecar)

#This is an in-between route to process delete requests based on ID.
@app.route("/delete", methods=["POST"])
def delete():
    url = 'http://localhost:3001/cars/' + str(request.form.get("DeleteID"))
    delete_r = requests.request('DELETE',url)
    return redirect(url_for("car_list"))

#Sprint 2: edit details of a car

@app.route("/edit_car",methods=["POST"])
def edit_car():
    editcar = {
        'editID' : str(request.form.get("EditID")),
        'editEntryDate' : str(request.form.get("EditEntrydate")),
        'editKmdriven' : str(request.form.get("EditKmdriven")),
        'editReleaseYear' : str(request.form.get("EditReleaseyear")),
        'editCondition' : str(request.form.get("EditCondition")),
        'editPricekm' : str(request.form.get("EditPricekm")),
        'editBrand': str(request.form.get("EditBrand")),
        'editType' : str(request.form.get("EditType")),
        'editState' : str(request.form.get("EditState")),
        'editPriceday' : str(request.form.get("EditPriceday"))
    }
    today = datetime.date.today()
    d1 = today.strftime("%Y-%m-%d")

    return render_template("edit_car.html",today = d1, editcar = editcar)

@app.route("/wrapup_edit",methods=["POST"])
def wrapup_edit():
    PutID = str(request.form.get("oldID"))

    if str(request.form.get("EntryDate")) == "":
        PutEntryDate = str(request.form.get("oldEntrydate"))
    else:
        PutEntryDate = str(request.form.get("EntryDate"))

    if str(request.form.get("KmDriven")) == "":
        PutKmDriven = str(request.form.get("oldKmdriven"))
    else:
        PutKmDriven = str(request.form.get("KmDriven"))

    if str(request.form.get("ReleaseYear")) == "":
        PutReleaseYear = str(request.form.get("oldReleaseyear"))
    else:
        PutReleaseYear = str(request.form.get("ReleaseYear"))

    if str(request.form.get("CarCondition")) == "":
        PutCarCondition = str(request.form.get("oldCondition"))
    else:
        PutCarCondition = str(request.form.get("CarCondition"))

    if str(request.form.get("PriceKm")) == "":
        PutPriceKm = str(request.form.get("oldPricekm"))
    else:
        PutPriceKm = str(request.form.get("PriceKm"))

    if str(request.form.get("PriceDay")) == "":
        PutPriceDay = str(request.form.get("oldPriceday"))
    else:
        PutPriceDay = str(request.form.get("PriceDay"))

    if str(request.form.get("Brand")) == "":
        PutBrand = str(request.form.get("oldBrand"))
    else:
        PutBrand = str(request.form.get("Brand"))

    if str(request.form.get("Type")) == "":
        PutType = str(request.form.get("oldType"))
    else:
        PutType = str(request.form.get("Type"))

    if str(request.form.get("State")) == "":
        PutState = str(request.form.get("oldState"))
    else:
        PutState = str(request.form.get("State"))

    url = "http://localhost:3001/cars" + "/" + PutID
    params = {'id': PutID,
            'entrydate': PutEntryDate,
            'kmdriven': PutKmDriven,
            'releaseyear': PutReleaseYear,
            'condition': PutCarCondition,
            'pricekm': PutPriceKm,
            "state": PutState,
            "brand": PutBrand,
            "model": "",
            "type": PutType,
            "priceday": PutPriceDay
            }

    headers = {'content-type': 'application/json'}
    r = requests.request('PUT',url, data = json.dumps(params), headers=headers)

    return redirect(url_for("car_list"))

#Sprint 2: filter car with a form
@app.route("/filter_form", methods = ["POST", "GET"])
def filter_form():
    if request.method == "POST":
        url = "http://localhost:3001/cars"
        r = requests.request("GET",url).json()
        #Processing entry date filter data
        EntryDateMax = request.form.get('EntryDateMax')
        EntryDateMin = request.form.get('EntryDateMin')
        if EntryDateMax != "" or EntryDateMin != "":
            if EntryDateMax != "":
                a = EntryDateMax.split("-")
                date_a = date(int(a[0]),int(a[1]),int(a[2]))
                for car in r:
                    c = car['entrydate'].split("-")
                    date_c = date(int(c[0]),int(c[1]),int(c[2]))
                    if date_c>date_a:
                        r.remove(car)
            if EntryDateMin != "":
                b = EntryDateMin.split("-")
                date_b = date(int(b[0]),int(b[1]),int(b[2]))
                for car in r:
                    c = car['entrydate'].split("-")
                    date_c = date(int(c[0]),int(c[1]),int(c[2]))
                    if date_c < date_b:
                        r.remove(car)
            if EntryDateMin !="" and EntryDateMax !="":
                if date_a < date_b:
                    return abort(jsonify(message = "The max entry year cannot be smaller than the min entry year."),400)

        #Processing Km Driven data
        KmDrivenMax = request.form.get('KmDrivenMax')
        KmDrivenMin = request.form.get('KmDrivenMin')
        if KmDrivenMax != "" or KmDrivenMin != "":
            if KmDrivenMax != "":
                for car in r:
                    c = int(car['kmdriven'])
                    if c>int(KmDrivenMax):
                        r.remove(car)
            if KmDrivenMin != "":
                for car in r:
                    c = int(car['kmdriven'])
                    if c<int(KmDrivenMin):
                        r.remove(car)
            if (KmDrivenMax != "" and KmDrivenMin != "") and (int(KmDrivenMax) < int(KmDrivenMin)):
                return abort(jsonify(message = "The max km driven cannot be smaller than the min km driven."),400)

        #Processing release year
        ReleaseYearMax = request.form.get('ReleaseYearMax')
        ReleaseYearMin = request.form.get('ReleaseYearMin')
        if ReleaseYearMax != "" or ReleaseYearMin != "":
            if ReleaseYearMax != "":
                for car in r:
                    c = int(car['releaseyear'])
                    if c>int(ReleaseYearMax):
                        r.remove(car)
            if ReleaseYearMin != "":
                for car in r:
                    c = int(car['releaseyear'])
                    if c<int(ReleaseYearMin):
                        r.remove(car)
            if (ReleaseYearMax != "" and ReleaseYearMin != "") and (int(ReleaseYearMax) < int(ReleaseYearMin)):
                return abort(jsonify(message = "The max release year cannot be smaller than the min release year."),400)

        #Procesing CarCondition
        CarCondition = request.form.get('CarCondition')
        if CarCondition != "":
            for car in r:
                if car['condition']!=CarCondition:
                    r.remove(car)

        #Processing Car brands
        Brand = request.form.get('Brand')
        if Brand != "":
            for car in r:
                if car['brand']!=Brand:
                    r.remove(car)

        #Processing Car types
        Type = request.form.get('Type')
        if Type != "":
            for car in r:
                if car['type']!=Type:
                    r.remove(car)

        #Processing Car states
        CarState = request.form.get('CarState')
        if CarState != "":
            for car in r:
                if car['state']!=CarState:
                    r.remove(car)

        #Processing price per km
        PriceKmMin = request.form.get('PriceKmMin')
        PriceKmMax = request.form.get('PriceKmMax')
        if PriceKmMax != "" or PriceKmMin != "":
            if PriceKmMax != "":
                for car in r:
                    c = int(car['pricekm'])
                    if c>int(PriceKmMax):
                        r.remove(car)
            if PriceKmMin != "":
                for car in r:
                    c = int(car['pricekm'])
                    if c<int(PriceKmMin):
                        r.remove(car)
            if (PriceKmMax != "" and PriceKmMin != "") and (int(PriceKmMax) < int(PriceKmMin)):
                return abort(jsonify(message = "The max price per km cannot be smaller than the min price per km."),400)

        #Processing price per day
        PriceDayMax = request.form.get('PriceDayMax')
        PriceDayMin = request.form.get('PriceDayMin')
        if PriceDayMax != "" or PriceDayMin != "":
            if PriceDayMax != "":
                for car in r:
                    c = int(car['priceday'])
                    if c>int(PriceDayMax):
                        r.remove(car)
            if PriceDayMin != "":
                for car in r:
                    c = int(car['priceday'])
                    if c<int(PriceDayMin):
                        r.remove(car)
            if (PriceDayMax != "" and PriceDayMin != "") and (int(PriceDayMax) < int(PriceDayMin)):
                return abort(jsonify(message = "The max price per day cannot be smaller than the min price per day."),400)

        filtered_response = r
        print(filtered_response)
        return render_template("car_list.html", responses = filtered_response)

    elif request.method == "GET":
        today = date.today()
        d1 = today.strftime("%Y-%m-%d")
        return render_template("filter_form.html",today=d1)


if __name__ == '__main__':
    app.run(port=5001)