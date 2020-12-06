from flask import Flask, redirect, url_for, render_template, request, session, abort, make_response
# To start server :
# First: C:\Users\OS\COEN6311\car-rental-all-class
# Then: ./mvnw spring-boot:run
# Please execute: "$env:FLASK_RUN_PORT = 5001" to change your port
# Set Flask to debug mode :$env:FLASK_ENV = "development"
from datetime import date, datetime
import requests, uuid, json, os

import checkemail

app = Flask(__name__)

app.secret_key = "coen6311"

#This is the index endpoint.
@app.route("/")
def index():
    # This should return the login page if login successfully, return the index.html page
    # Checking session value for "username" attribute
    if session.get('username') is not None:
        #Pass on the user's username and position for display in the html page
        return render_template("index.html", username = session.get('username'), position = session.get('position'))
    else:
        return render_template("log_in.html")

#This is a in-between route that processes log-in information
@app.route("/login", methods =["POST"])
def login():
    #Check if the user is logged in by accessing the session variable
    if session.get('username') is not None:
        return redirect(url_for('index'))
    #Set up the parameters for getting all employees from the database to process log-in information
    url = "http://localhost:3001/employees"
    r = requests.request("GET",url).json()
    #Get the data from html form POST request with name "username" and "password"
    username = str(request.form.get("username"))
    password = str(request.form.get("password"))

    #Check for every responses in the response message, if there is a match, make changes to the session variable
    for response in r:
        if response["name"] == username and response["password"]==password:
            #In case the user account is not activated, return an error:
            if response["activation"] == False:
                return abort(make_response({'message': 'Your account is not activated. Please contact the manager.'},400))
            else: #just change the session variable to store the user's username and position (for service access restriction)
                session['username'] = response['name']
                session['position'] = response['position']
                break
    #Checks if the user logs in successfully by accessing session variable
    if session.get('username') is not None:
        #passing "username" and "position" to display in index html
        return render_template("index.html", username = session.get('username'), position = session.get('position')) #log in sucessfully
    else:
        #returns bad_log_in html when session variable does not contain username
        return render_template("bad_log_in.html") #log in fails

#A route to open registration form html page
@app.route("/register_form", methods = ["GET", "POST"])
def register_form():
    #If access via GET -> return the registration form
    if request.method == "GET":
        return render_template("register.html")
    #if access via POST (usually from html form) -> processing registration data
    elif request.method == "POST":
        #Preparing the parameters to send the Java spring boot server
        #Checks for length of password
        if len(str(request.form.get("password"))) < 8:
            abort(make_response({'message': 'Password needs to be at least 8 characters'},400))
        #Checks for Position: only Staff and Finance people are allowed to register
        elif str(request.form.get("position")) != "Staff" and str(request.form.get("position")) != "Finance":
            abort(make_response({'message': 'New employees can only be Staff or Finance'},400))
        #Check for if the entered email is valid using "checkemail" module
        elif not checkemail.check(str(request.form.get("email"))):
            abort(make_response({'message': 'Email entered is invalid'},400))
        #Check the default activation: new users must have it at "false" so that manager can later activate their accounts
        elif str(request.form.get('activation')) != "false":
            abort(make_response({'message': 'New user must await activation from manager'},400))
        else: #The input passes every test above:
            #Prepare endpoint for making requests to Springboot server
            url = 'http://localhost:3001/employees'
            #Get the list of employees from the backend to check for existing name or email
            r1 = requests.get(url).json()
            for response1 in r1:
                if response1['name'] == str(request.form.get("fullname")):
                    abort(make_response({'message': 'Name already exists.'},400))
                elif response1['email'] == str(request.form.get("email")):
                    abort(make_response({'message': 'Email already exists.'},400))
            #Preparing the body for making POST request to create new employee
            params = {'employeeid': str(request.form.get("id")),
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

#Remove session variable when the user logs out
@app.route("/logout")
def logout():
    session.pop('username', None)
    session.pop('position', None)
    #Then return them to log in page
    return redirect(url_for('index'))

# This is for activitating inactivated employees or remove employee accounts and not managing every aspect of employees account
@app.route('/manage_accounts', methods = ["GET", "POST"])
def manage_accounts():
    #Check for log in status and access privileges
    if session.get('username') is None:
        return redirect(url_for("index"))
    elif session.get('position') == "Staff" or session.get('position') == "Finance":
        abort(make_response({'message': 'Not enough authorization'},403))

    #Prep endpoint to get the list of employees
    url = "http://localhost:3001/employees"
    r = requests.request("GET",url).json()

    #Get request endpoint to display list of employees
    if request.method == "GET":
        employees = []
        for user in r:
            #remove passwords because of "reasons"
            user.pop('password', None)
            #Managers should not be included in the list
            if user['position'] == "Manager":
                continue
            employees.append(user)
        #Pass in employees variable to be displayed in html
        return render_template('manage_accounts.html',employees=employees)

    #Post request from html form to finalize the activation
    if request.method == "POST":
        #Get the activated employee from html form from confirm_activate_accounts.html
        employee_id = request.form.get('id')
        #Prepare the Put request body to be send
        put_employee = {}
        for employee in r:
            if employee['employeeid'] == int(employee_id):
                put_employee = employee
                #Set the employee account activation status to True
                put_employee['activation'] = True
        #Prepare the put request headers and url
        headers = {'content-type': 'application/json'}
        url = 'http://localhost:3001/employees/'+str(employee_id)
        #Make the request
        r = requests.put(url, data =json.dumps(put_employee),headers=headers)
        #return to employee list
        return redirect(url_for('manage_accounts'))

#This endpoint allow displaying the confirmation page for employee activation
@app.route('/confirm_activate_accounts',methods = ['POST'])
def confirm_activate_accounts():
    #Check for login status and access privileges
    if session.get('username') is None:
        return redirect(url_for("index"))
    elif session.get('position') == "Staff" or session.get('position') == "Finance":
        abort(make_response({'message': 'Not enough authorization'},403))

    #Get the employee with the submitted id from html form (from manage_accounts.html) to display in confirm page
    url = "http://localhost:3001/employees/" + str(request.form.get('id'))
    r = requests.request("GET",url).json()

    return render_template("confirm_activation.html", employee_confirm = r)

#Remove account endpoint
@app.route('/remove_account',methods = ['POST'])
def remove_account():

    employee_id = request.form.get('id')
    url = 'http://localhost:3001/employees/'+str(employee_id)
    requests.delete(url)
    return redirect(url_for('manage_accounts'))

@app.route('/confirm_remove_accounts',methods = ['POST'])
def confirm_remove_accounts():
    if session.get('username') is None:
        return redirect(url_for("index"))
    elif session.get('position') == "Staff" or session.get('position') == "Finance":
        abort(make_response({'message': 'Not enough authorization'},403))

    url = "http://localhost:3001/employees/" + str(request.form.get('id'))
    r = requests.request("GET",url).json()

    return render_template("confirm_account_deletion.html", employee_confirm = r)

#An html page that displays the car list, whose content is fetched from the server
#This also acts as an in-between page to process adding cars to the fleet requests from add_car_form below
@app.route("/car_list", methods=["GET","POST"])
def car_list():
    if session.get('username') is None:
        return redirect(url_for("index"))
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
            params = {'carid': str(request.form.get("CarID")),
                'entrydate': str(request.form.get("EntryDate")),
                'kmdriven': str(request.form.get("KmDriven")),
                'releaseyear': str(request.form.get("ReleaseYear")),
                'condi': str(request.form.get("CarCondition")),
                'pricekm': str(request.form.get("PriceKm")),
                "state": str(request.form.get("CarState")),
                "brand": str(request.form.get("Brand")),
                "model": "",
                "style": str(request.form.get("Type")),
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
    if session.get('username') is None:
        return redirect(url_for("index"))
    elif session.get('position') == "Staff":
        abort(make_response({'message': 'Not enough authorization'},404))
    today = date.today()
    d1 = today.strftime("%Y-%m-%d")

    return render_template("add_car_form.html",today = d1)

#This is an route the directs to the confirmation for delete page with all the information of the targeted car
@app.route("/delete_confirmation", methods=["POST"])
def delete_confirmation():
    if session.get('position') == "Staff":
        abort(make_response({'message': 'Not enough authorization'},404))
    r = requests.get('http://localhost:3001/cars/'+ str(request.form.get("DeleteID"))).json()
    deletecar = {
        'deleteID' : r['carid'],
        'entryDate' : r["entrydate"],
        'kmDriven' : r["kmdriven"],
        'releaseYear' : r["releaseyear"],
        'condition' : r["condi"],
        'priceKm' : r["pricekm"] ,
        'brand': r["brand"] ,
        'type' : r["style"],
        'state' : r["state"] ,
        'priceday' : r["priceday"]
    }
    return render_template("delete_confirmation.html", deletecar = deletecar)

#This is an in-between route to process delete requests based on ID.
@app.route("/delete", methods=["POST"])
def delete():
    if session.get('position') == "Staff":
        abort(make_response({'message': 'Not enough authorization'},404))
    url = 'http://localhost:3001/cars/' + str(request.form.get("DeleteID"))
    delete_r = requests.request('DELETE',url)
    return redirect(url_for("car_list"))

#Sprint 2: edit details of a car

@app.route("/edit_car",methods=["POST"])
def edit_car():
    r = requests.get('http://localhost:3001/cars/'+ str(request.form.get("EditID"))).json()
    editcar = {
        'editID' : r['carid'],
        'editEntryDate' : r["entrydate"],
        'editKmdriven' : r["kmdriven"],
        'editReleaseYear' : r["releaseyear"],
        'editCondition' : r["condi"],
        'editPricekm' : r["pricekm"] ,
        'editBrand': r["brand"] ,
        'editType' : r["style"],
        'editState' : r["state"] ,
        'editPriceday' : r["priceday"]
    }
    today = date.today()
    d1 = today.strftime("%Y-%m-%d")
    return render_template("edit_car.html",today = d1, editcar = editcar, position = session.get('position'))

@app.route("/wrapup_edit",methods=["POST"])
def wrapup_edit():
    if str(request.form.get("oldID")) == "" or str(request.form.get("oldID")) is None:
        abort(make_response({'message': 'Must contain ID'},400))

    if str(request.form.get("oldEntrydate")) == "" or request.form.get("oldEntrydate") is None:
        abort(make_response({'message': 'Must contain oldEntryDate'},400))

    if str(request.form.get("oldKmdriven")) == "" or request.form.get("oldKmdriven") is None:
        abort(make_response({'message': 'Must contain oldKmDriven'},400))

    if str(request.form.get("oldReleaseyear")) == "" or request.form.get("oldReleaseyear") is None:
        abort(make_response({'message': 'Must contain oldReleaseYear'},400))

    if str(request.form.get("oldCondition")) == "" or request.form.get("oldCondition") is None:
        abort(make_response({'message': 'Must contain oldCarCondition'},400))

    if str(request.form.get("oldPricekm")) == "" or request.form.get("oldPricekm") is None:
        abort(make_response({'message': 'Must contain oldPriceKm'},400))

    if str(request.form.get("oldPriceday")) == "" or request.form.get("oldPriceday") is None:
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
        #THERE IS A BUG HERE
        # if session.get('position') == "Staff" and (str(request.form.get("EntryDate")) != "" or request.form.get("EntryDate") is not None):
        #     abort(make_response({'message': 'Not enough authorization'},403))
        PutEntryDate = str(request.form.get("EntryDate"))

    if str(request.form.get("KmDriven")) == "" or request.form.get("KmDriven") is None:
        PutKmDriven = str(request.form.get("oldKmdriven"))
    else:
        # if session.get('position') == "Staff" and (str(request.form.get("KmDriven")) != "" or request.form.get("KmDriven") is not None):
        #     abort(make_response({'message': 'Not enough authorization'},403))
        PutKmDriven = str(request.form.get("KmDriven"))

    if str(request.form.get("ReleaseYear")) == "" or request.form.get("ReleaseYear") is None:
        PutReleaseYear = str(request.form.get("oldReleaseyear"))
    else:
        # if session.get('position') == "Staff" and (str(request.form.get("ReleaseYear")) != "" or request.form.get("ReleaseYear") is not None):
        #     abort(make_response({'message': 'Not enough authorization'},403))
        PutReleaseYear = str(request.form.get("ReleaseYear"))

    if str(request.form.get("CarCondition")) == "" or request.form.get("CarCondition") is None:
        PutCarCondition = str(request.form.get("oldCondition"))
    else:
        PutCarCondition = str(request.form.get("CarCondition"))

    if str(request.form.get("PriceKm")) == "" or request.form.get("PriceKm") is None:
        PutPriceKm = str(request.form.get("oldPricekm"))
    else:
        # if session.get('position') == "Staff" and (str(request.form.get("PriceKm")) != "" or request.form.get("PriceKm") is not None):
        #     abort(make_response({'message': 'Not enough authorization'},403))
        PutPriceKm = str(request.form.get("PriceKm"))

    if str(request.form.get("PriceDay")) == "" or request.form.get("PriceDay") is None:
        PutPriceDay = str(request.form.get("oldPriceday"))
    else:
        # if session.get('position') == "Staff" and (str(request.form.get("PriceDay")) != "" or request.form.get("PriceDay") is not None):
        #     abort(make_response({'message': 'Not enough authorization'},403))
        PutPriceDay = str(request.form.get("PriceDay"))

    if str(request.form.get("Brand")) == "" or request.form.get("Brand") is None:
        PutBrand = str(request.form.get("oldBrand"))
    else:
        # if session.get('position') == "Staff" and (str(request.form.get("Brand")) != "" or request.form.get("Brand") is not None):
        #     abort(make_response({'message': 'Not enough authorization'},403))
        PutBrand = str(request.form.get("Brand"))

    if str(request.form.get("Type")) == "" or request.form.get("Type") is None:
        PutType = str(request.form.get("oldType"))
    else:
        # if session.get('position') == "Staff" and (str(request.form.get("Type")) != "" or request.form.get("Type") is not None):
        #     abort(make_response({'message': 'Not enough authorization'},404))
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

        put_params = {'carid': PutID,
                'entrydate': PutEntryDate,
                'kmdriven': PutKmDriven,
                'releaseyear': PutReleaseYear,
                'condi': PutCarCondition,
                'pricekm': PutPriceKm,
                "state": PutState,
                "brand": PutBrand,
                "model": "",
                "style": PutType,
                "priceday": PutPriceDay
                }
        old_params = {'carid': PutID,
                'entrydate': str(request.form.get("oldEntrydate")),
                'kmdriven': str(request.form.get("oldKmDriven")),
                'releaseyear': str(request.form.get("oldReleaseyear")),
                'condi': str(request.form.get("oldCondition")),
                'pricekm': str(request.form.get("oldPricekm")),
                "state": str(request.form.get("oldState")),
                "brand": str(request.form.get("oldBrand")),
                "model": "",
                "style": str(request.form.get("oldType")),
                "priceday": str(request.form.get("oldPriceday"))
                }

        # headers = {'content-type': 'application/json'}
        # r = requests.request('PUT',url, data = json.dumps(put_params), headers=headers)

        # return redirect(url_for("car_list"))
        return render_template("confirm_edit.html",put_params = put_params, old_params = old_params, position = session.get('position'))

@app.route("/confirm_edit", methods = ["POST"])
def confirm_edit():
    url = "http://localhost:3001/cars" + "/" + str(request.form.get("putID"))
    put_params = {'carid': str(request.form.get("putID")),
                'entrydate': str(request.form.get("putEntrydate")),
                'kmdriven': str(request.form.get("putKmdriven")),
                'releaseyear': str(request.form.get("putReleaseyear")),
                'condi': str(request.form.get("putCondition")),
                'pricekm': str(request.form.get("putPricekm")),
                "state": str(request.form.get("putState")),
                "brand": str(request.form.get("putBrand")),
                "model": "",
                "style": str(request.form.get("putType")),
                "priceday": str(request.form.get("putPriceday"))
                }
    print(put_params)
    headers = {'content-type': 'application/json'}
    r = requests.request('PUT',url, data = json.dumps(put_params), headers=headers)

    return redirect(url_for("car_list"))

#Sprint 2: filter car with a form
@app.route("/filter_form", methods = ["POST", "GET"])
def filter_form():
    if session.get('username') is None:
        return redirect(url_for("index"))

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
        conditions = ["new","slightly used","used","old"]
        CarCondition = request.form.get('CarCondition')
        if CarCondition != "":
            if CarCondition not in conditions:
                abort(make_response({'message': "Invalid car condition given"},400))
            cars_for_removal = []
            for car in r:
                if car['condi']!=CarCondition:
                    cars_for_removal.append(car)
            for car in cars_for_removal:
                r.remove(car)

        #Processing Car brands
        brands = ["Toyota","Honda","Mazda","Nissan","Subaru"]
        Brand = request.form.get('Brand')
        if Brand != "":
            if Brand not in brands:
                abort(make_response({'message': "Invalid car brand given"},400))
            cars_for_removal = []
            for car in r:
                if car['brand']!=Brand:
                    cars_for_removal.append(car)
            for car in cars_for_removal:
                r.remove(car)

        #Processing Car types
        types = ["Sedan","SUV","Minivan","Crossover","Wagon"]
        Type = request.form.get('Type')
        if Type != "":
            if Type not in types:
                abort(make_response({'message': "Invalid car type given"},400))
            cars_for_removal = []
            for car in r:
                if car['style']!=Type:
                    cars_for_removal.append(car)
            for car in cars_for_removal:
                r.remove(car)

        #Processing Car states
        states = ["True", "False"]
        CarState = request.form.get('CarState')
        if CarState != "":
            if CarState not in states:
                abort(make_response({'message': "Invalid car state given"},400))
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

#Sprint3: For Managers: manage employees account, managers can read report, finance people can generate reports

@app.route('/generate_financial_report', methods =['POST', 'GET'])
def generate_financial_report():
    if session.get('position') != 'Finance':
        abort(make_response({'message': "Not enough authorization."},403))

    today = date.today()
    d1 = today.strftime("%Y-%m-%d")

    url = 'http://localhost:3001/bills'
    r = requests.get(url).json()

    if request.method == "GET":
        return render_template('generate_financial_report.html', today=d1)
    elif request.method == "POST":
        url = 'http://localhost:3001/bills'
        r = requests.get(url).json()
        lowerlimit = request.form.get('lowerlimit')
        upperlimit = request.form.get('upperlimit')
        if upperlimit != "" and lowerlimit != "":
            a = upperlimit.split("-")
            date_a = date(int(a[0]),int(a[1]),int(a[2]))
            b = lowerlimit.split("-")
            date_b = date(int(b[0]),int(b[1]),int(b[2]))
            if date_a < date_b:
                return abort(make_response({'message': "The max year cannot be smaller than the min year."},400))
            bills_for_removal = []
            for bill in r:
                c = bill['startdate'].split("-")
                date_c = date(int(c[0]),int(c[1]),int(c[2]))
                if date_c>date_a or date_c < date_b:
                    bills_for_removal.append(bill)
            for bill in bills_for_removal:
                r.remove(bill)
        else:
            return abort(make_response({'message': "both lower and upper limits are required"},400))

        duration = str(date_a - date_b).split(',')
        report_duration = duration[0]
        report_date = d1
        report_revenue = 0
        for bill in r:
            report_revenue += int(bill['carbill'])

        url = 'http://localhost:3001/reports'
        headers = {'content-type': 'application/json'}
        params = {
            'reportdate': report_date,
            'revenue': report_revenue,
            'durationreported': report_duration
        }
        r = requests.post(url, data=json.dumps(params),headers=headers)
        return render_template('success_financial_report.html', params = params)

@app.route('/get_bills', methods = ['POST'])
def get_bills():

    lowerlimit = request.form.get('DateMin')
    upperlimit = request.form.get('DateMax')

    url = 'http://localhost:3001/bills'
    r = requests.get(url).json()

    #Only filters based on start date
    if upperlimit != "" and lowerlimit != "":
        a = upperlimit.split("-")
        date_a = date(int(a[0]),int(a[1]),int(a[2]))
        b = lowerlimit.split("-")
        date_b = date(int(b[0]),int(b[1]),int(b[2]))
        if date_a < date_b:
            return abort(make_response({'message': "The max year cannot be smaller than the min year."},400))
        bills_for_removal = []
        for bill in r:
            c = bill['startdate'].split("-")
            date_c = date(int(c[0]),int(c[1]),int(c[2]))
            if date_c>date_a or date_c < date_b:
                bills_for_removal.append(bill)
        for bill in bills_for_removal:
            r.remove(bill)
    else:
        return abort(make_response({'message': "both lower and upper limits are required"},400))

    bills = r

    today = date.today()
    d1 = today.strftime("%Y-%m-%d")

    return render_template('generate_financial_report.html', today = d1, bills = bills, upperlimit=upperlimit, lowerlimit=lowerlimit)

@app.route('/financial_report', methods = ['GET'])
def financial_report():
    if session.get('position') != 'Manager':
        abort(make_response({'message': "invalid authorization"},403))
    url = 'http://localhost:3001/reports'
    r = requests.get(url).json()
    return render_template('financial_report.html', reports = r)

if __name__ == '__main__':
    os.environ['FLASK_ENV']= "development"
    app.run(port=5001)