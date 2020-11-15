from flask import Flask, redirect, url_for, render_template, request, session, abort, make_response
# To start server :
# First: C:\Users\OS\COEN6311\car-rental-all-class
# Then: ./mvnw spring-boot:run
# Please execute: "$env:FLASK_RUN_PORT = 5001" to change your port
from datetime import date, datetime
import requests, uuid, json

import checkemail

app = Flask(__name__)
app.secret_key = "coen6311"
#The first page when starting provider interface: return the log_in page
@app.route("/")
def index():
    # This should return the login page if login successfully, return the index.html page
    if session.get('username') is not None:
        return render_template("index.html", username = session.get('username'), position = session.get('position'))
    else:
        return render_template("log_in.html")

#This is a in-between route that processes log-in information
@app.route("/login", methods =["POST"])
def login():
    #Set up the parameters for getting all employees from the database to process log-in information
    url = "http://localhost:3001/employees"
    r = requests.request("GET",url).json()
    username = str(request.form.get("username"))
    password = str(request.form.get("password"))

    #Check for every responses in the response message, if there is a match, change the token to username
    for response in r:
        if response["name"] == username and response["password"]==password:
            if response["activation"] == False:
                return abort(make_response({'message': 'Your account is not activated. Please contact the manager.'},400))
            else:
                session['username'] = response['name']
                session['position'] = response['position']
                break
    if session.get('username') is not None:
        return render_template("index.html", username = session.get('username'), position = session.get('position')) #log in sucessfully
    else:
        return render_template("bad_log_in.html") #log in fails

#A route to open registration form html page
@app.route("/register_form", methods = ["GET", "POST"])
def register_form():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        #Preparing the parameters to send the Java spring boot server
        if len(str(request.form.get("password"))) < 8:
            abort(make_response({'message': 'Password needs to be at least 8 characters'},400))
        elif str(request.form.get("position")) != "Staff" and str(request.form.get("position")) != "Finance":
            abort(make_response({'message': 'New employees can only be Staff or Finance'},400))
        elif not checkemail.check(str(request.form.get("email"))):
            abort(make_response({'message': 'Email entered is invalid'},400))
        elif str(request.form.get('activation')) != "false":
            abort(make_response({'message': 'New user must await activation from manager'},400))
        else:
            url = 'http://localhost:3001/employees'
            r1 = requests.get(url).json()
            for response1 in r1:
                if response1['name'] == str(request.form.get("fullname")):
                    abort(make_response({'message': 'Name already exists.'},400))
                elif response1['email'] == str(request.form.get("email")):
                    abort(make_response({'message': 'Email already exists.'},400))

            params = {'id': str(request.form.get("id")),
                'name' : str(request.form.get("fullname")),
                'password' : str(request.form.get("password")),
                'position' : str(request.form.get("position")),
                'email' : str(request.form.get("email")),
                'activation' : str(request.form.get('activation'))
                }

            headers = {'content-type': 'application/json'}
            #make the requests
            r = requests.request("POST", url, data = json.dumps(params),headers = headers)
            #Depends on if the registration is successful or not, return it to display in log_in html
            return render_template("log_in.html", response_status = r.status_code)

@app.route("/logout")
def logout():
    session.pop('username', None)
    session.pop('position', None)
    return redirect(url_for('index'))

@app.route('/manage_accounts',methods = ["GET", "POST"])
def manage_accounts():
    url = "http://localhost:3001/employees"
    r = requests.request("GET",url).json()
    if request.method == "GET":
        employees = []
        for user in r:
            if user['activation'] == False:
                user.pop('password', None)
                employees.append(user)

        return render_template('manage_accounts.html',employees=employees)
    if request.method == "POST":
        employee_id = request.form.get('id')
        put_employee = {}
        for employee in r:
            if employee['id'] == int(employee_id):
                put_employee = employee
                put_employee['activation'] = True
        headers = {'content-type': 'application/json'}
        url = 'http://localhost:3001/employees/'+str(employee_id)
        r = requests.put(url, data =json.dumps(put_employee),headers=headers)
        return redirect(url_for('manage_accounts'))

#An html page that displays the car list, whose content is fetched from the server
#This also acts as an in-between page to process adding cars to the fleet requests from add_car_form below
@app.route("/car_list", methods=["GET","POST"])
def car_list():
    #When a form sends post request to this route then the code below prep the parameters to send to the server.
    if request.method == "POST":
        #checks that every field must be filled:
        if str(request.form.get("CarID")) == "":
            abort(make_response({'message': 'id must be filled'},400))
        elif str(request.form.get("EntryDate")) == "":
            abort(make_response({'message': 'entrydate must be filled'},400))
        elif str(request.form.get("KmDriven")) == "":
            abort(make_response({'message': 'kmdriven must be filled'},400))
        elif str(request.form.get("ReleaseYear")) == "":
            abort(make_response({'message': 'releaseyear must be filled'},400))
        elif str(request.form.get("CarCondition")) == "":
            abort(make_response({'message': 'condition must be filled'},400))
        elif str(request.form.get("PriceKm")) == "":
            abort(make_response({'message': 'pricekm must be filled'},400))
        elif str(request.form.get("CarState")) == "":
            abort(make_response({'message': 'state must be filled'},400))
        elif str(request.form.get("Brand")) == "":
            abort(make_response({'message': 'brand must be filled'},400))
        elif str(request.form.get("Type")) == "":
            abort(make_response({'message': 'type must be filled'},400))
        elif str(request.form.get("PriceDay")) == "":
            abort(make_response({'message': 'priceday must be filled'},400))

        url = "http://localhost:3001/cars"
        date1 = str(request.form.get("EntryDate"))
        date2 = str(request.form.get("ReleaseYear"))
        if int(date1[0:4])<int(date2):
            return abort(make_response({'message': "The entry year cannot be smaller than the release year."},400))
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

    return render_template("car_list.html",responses = r,username = session.get('username'), position = session.get('position'))

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
    today = date.today()
    d1 = today.strftime("%Y-%m-%d")
    return render_template("edit_car.html",today = d1, editcar = editcar, position = session.get('position'))

@app.route("/wrapup_edit",methods=["POST"])
def wrapup_edit():
    if str(request.form.get("oldID")) or str(request.form.get("oldID")) is None:
        abort(make_response({'message': 'Must contain ID'},400))

    if str(request.form.get("oldEntryDate")) == "" or request.form.get("oldEntryDate") is None:
        abort(make_response({'message': 'Must oldEntryDate'},400))

    if str(request.form.get("oldKmDriven")) == "" or request.form.get("oldKmDriven") is None:
        abort(make_response({'message': 'Must contain oldKmDriven'},400))

    if str(request.form.get("oldReleaseYear")) == "" or request.form.get("oldReleaseYear") is None:
        abort(make_response({'message': 'Must contain oldReleaseYear'},400))

    if str(request.form.get("oldCarCondition")) == "" or request.form.get("oldCarCondition") is None:
        abort(make_response({'message': 'Must contain oldCarCondition'},400))

    if str(request.form.get("oldPriceKm")) == "" or request.form.get("oldPriceKm") is None:
        abort(make_response({'message': 'Must contain oldPriceKm'},400))

    if str(request.form.get("oldPriceDay")) == "" or request.form.get("oldPriceDay") is None:
        abort(make_response({'message': 'Must contain oldPriceDay'},400))

    if str(request.form.get("oldBrand")) == "" or request.form.get("oldBrand") is None:
        abort(make_response({'message': 'Must contain oldBrand'},400))

    if str(request.form.get("oldType")) == "" or request.form.get("oldType") is None:
        abort(make_response({'message': 'Must contain oldType'},400))

    if str(request.form.get("oldState")) == "" or request.form.get("oldState") is None:
        abort(make_response({'message': 'Must contain oldState'},400))

    PutID = str(request.form.get("oldID"))

    if str(request.form.get("EntryDate")) == "" or request.form.get("EntryDate") is None:
        PutEntryDate = str(request.form.get("oldEntrydate"))
    else:
        PutEntryDate = str(request.form.get("EntryDate"))

    if str(request.form.get("KmDriven")) == "" or request.form.get("KmDriven") is None:
        PutKmDriven = str(request.form.get("oldKmdriven"))
    else:
        PutKmDriven = str(request.form.get("KmDriven"))

    if str(request.form.get("ReleaseYear")) == "" or request.form.get("ReleaseYear") is None:
        PutReleaseYear = str(request.form.get("oldReleaseyear"))
    else:
        PutReleaseYear = str(request.form.get("ReleaseYear"))

    if str(request.form.get("CarCondition")) == "" or request.form.get("CarCondition") is None:
        PutCarCondition = str(request.form.get("oldCondition"))
    else:
        PutCarCondition = str(request.form.get("CarCondition"))

    if str(request.form.get("PriceKm")) == "" or request.form.get("PriceKm") is None:
        PutPriceKm = str(request.form.get("oldPricekm"))
    else:
        PutPriceKm = str(request.form.get("PriceKm"))

    if str(request.form.get("PriceDay")) == "" or request.form.get("PriceDay") is None:
        PutPriceDay = str(request.form.get("oldPriceday"))
    else:
        PutPriceDay = str(request.form.get("PriceDay"))

    if str(request.form.get("Brand")) == "" or request.form.get("Brand") is None:
        PutBrand = str(request.form.get("oldBrand"))
    else:
        PutBrand = str(request.form.get("Brand"))

    if str(request.form.get("Type")) == "" or request.form.get("Type") is None:
        PutType = str(request.form.get("oldType"))
    else:
        PutType = str(request.form.get("Type"))

    if str(request.form.get("State")) == "" or request.form.get("State") is None:
        PutState = str(request.form.get("oldState"))
    else:
        PutState = str(request.form.get("State"))

    date1 = PutEntryDate
    date2 = PutReleaseYear
    if int(date1[0:4])<int(date2):
        return abort(make_response({'message': "The entry year cannot be smaller than the release year."},400))
    else:
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
                cars_for_removal = []
                for car in r:
                    c = car['entrydate'].split("-")
                    date_c = date(int(c[0]),int(c[1]),int(c[2]))
                    if date_c>date_a:
                        cars_for_removal.append(car)
                for car in cars_for_removal:
                    r.remove(car)
            if EntryDateMin != "":
                b = EntryDateMin.split("-")
                date_b = date(int(b[0]),int(b[1]),int(b[2]))
                cars_for_removal = []
                for car in r:
                    c = car['entrydate'].split("-")
                    date_c = date(int(c[0]),int(c[1]),int(c[2]))
                    if date_c < date_b:
                        cars_for_removal.append(car)
                for car in cars_for_removal:
                    r.remove(car)
            if EntryDateMin !="" and EntryDateMax !="":
                if date_a < date_b:
                    return abort(make_response({'message': "The max entry year cannot be smaller than the min entry year."},400))
        #Processing Km Driven data
        KmDrivenMax = request.form.get('KmDrivenMax')
        KmDrivenMin = request.form.get('KmDrivenMin')
        if KmDrivenMax != "" or KmDrivenMin != "":
            if KmDrivenMax != "":
                cars_for_removal = []
                for car in r:
                    c = int(car['kmdriven'])
                    if c>int(KmDrivenMax):
                        cars_for_removal.append(car)
                for car in cars_for_removal:
                    r.remove(car)
            if KmDrivenMin != "":
                cars_for_removal = []
                for car in r:
                    c = int(car['kmdriven'])
                    if c<int(KmDrivenMin):
                        cars_for_removal.append(car)
                for car in cars_for_removal:
                    r.remove(car)
            if (KmDrivenMax != "" and KmDrivenMin != "") and (int(KmDrivenMax) < int(KmDrivenMin)):
                return abort(make_response({'message': "The max km driven cannot be smaller than the min km driven."},400))

        #Processing release year
        ReleaseYearMax = request.form.get('ReleaseYearMax')
        ReleaseYearMin = request.form.get('ReleaseYearMin')
        if ReleaseYearMax != "" or ReleaseYearMin != "":
            if ReleaseYearMax != "":
                cars_for_removal = []
                for car in r:
                    c = int(car['releaseyear'])
                    if c>int(ReleaseYearMax):
                        cars_for_removal.append(car)
                for car in cars_for_removal:
                    r.remove(car)
            if ReleaseYearMin != "":
                cars_for_removal = []
                for car in r:
                    c = int(car['releaseyear'])
                    if c<int(ReleaseYearMin):
                        cars_for_removal.append(car)
                for car in cars_for_removal:
                    r.remove(car)
            if (ReleaseYearMax != "" and ReleaseYearMin != "") and (int(ReleaseYearMax) < int(ReleaseYearMin)):
                return abort(make_response({'message': "The max release year cannot be smaller than the min release year."},400))

        #Procesing CarCondition
        CarCondition = request.form.get('CarCondition')
        if CarCondition != "":
            cars_for_removal = []
            for car in r:
                if car['condition']!=CarCondition:
                    cars_for_removal.append(car)
            for car in cars_for_removal:
                r.remove(car)

        #Processing Car brands
        Brand = request.form.get('Brand')
        if Brand != "":
            cars_for_removal = []
            for car in r:
                if car['brand']!=Brand:
                    cars_for_removal.append(car)
            for car in cars_for_removal:
                r.remove(car)

        #Processing Car types
        Type = request.form.get('Type')
        if Type != "":
            cars_for_removal = []
            for car in r:
                if car['type']!=Type:
                    cars_for_removal.append(car)
            for car in cars_for_removal:
                r.remove(car)

        #Processing Car states
        CarState = request.form.get('CarState')
        if CarState != "":
            cars_for_removal = []
            for car in r:
                if car['state']!=CarState:
                    cars_for_removal.append(car)
            for car in cars_for_removal:
                r.remove(car)

        #Processing price per km
        PriceKmMin = request.form.get('PriceKmMin')
        PriceKmMax = request.form.get('PriceKmMax')
        if PriceKmMax != "" or PriceKmMin != "":
            if PriceKmMax != "":
                cars_for_removal = []
                for car in r:
                    c = int(car['pricekm'])
                    if c>int(PriceKmMax):
                        cars_for_removal.append(car)
                for car in cars_for_removal:
                    r.remove(car)
            if PriceKmMin != "":
                cars_for_removal = []
                for car in r:
                    c = int(car['pricekm'])
                    if c<int(PriceKmMin):
                        cars_for_removal.append(car)
                for car in cars_for_removal:
                    r.remove(car)
            if (PriceKmMax != "" and PriceKmMin != "") and (int(PriceKmMax) < int(PriceKmMin)):
                return abort(make_response({'message': "The max price per km cannot be smaller than the min price per km."},400))

        #Processing price per day
        PriceDayMax = request.form.get('PriceDayMax')
        PriceDayMin = request.form.get('PriceDayMin')
        if PriceDayMax != "" or PriceDayMin != "":
            if PriceDayMax != "":
                cars_for_removal = []
                for car in r:
                    c = int(car['priceday'])
                    if c>int(PriceDayMax):
                        cars_for_removal.append(car)
                for car in cars_for_removal:
                    r.remove(car)
            if PriceDayMin != "":
                cars_for_removal = []
                for car in r:
                    c = int(car['priceday'])
                    if c<int(PriceDayMin):
                        cars_for_removal.append(car)
                for car in cars_for_removal:
                    r.remove(car)
            if (PriceDayMax != "" and PriceDayMin != "") and (int(PriceDayMax) < int(PriceDayMin)):
                return abort(make_response({'message': "The max price per day cannot be smaller than the min price per day."},400))

        filtered_response = r

        return render_template("car_list.html", responses = filtered_response, username = session.get('username'), position = session.get('position'))

    elif request.method == "GET":
        today = date.today()
        d1 = today.strftime("%Y-%m-%d")
        return render_template("filter_form.html",today=d1)

if __name__ == '__main__':
    app.run(port=5001)