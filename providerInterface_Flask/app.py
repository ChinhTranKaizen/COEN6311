from flask import Flask, redirect, url_for, render_template, request
# To start server : 
# First: C:\Users\OS\COEN6311\car-rental-all-class
# Then: ./mvnw spring-boot:run
# Please execute: "$env:FLASK_RUN_PORT = 5001" to change your port
from datetime import date

import requests, uuid, json

app = Flask(__name__)

    # Cars data structure:
    # Integer id;
	# String entrydate;
	# Integer kmdriven;
	# Integer releaseyear;
	# String condition;
	# Integer pricekm;
@app.route("/")
def index():
    # This should return the login page if login successfully, return the index.html page
    return render_template("log_in.html")

@app.route("/login", methods =["POST"])
def login():
    url = "http://localhost:3001/employees"
    r = requests.request("GET",url).json()
    username = str(request.form.get("username"))
    password = str(request.form.get("password"))
    login_token = False
    for response in r:
        if response["name"] == username and response["password"]==password:
            login_token = True
    if login_token:
        return render_template("index.html")
    else:
        return render_template("bad_log_in.html")

@app.route("/register_form")
def register_form():
    return render_template("register.html")

@app.route("/register", methods = ["POST"])
def register():
    url = 'http://localhost:3001/employees'
    params = {'id': str(request.form.get("id")),
        'name' : str(request.form.get("fullname")),
        'password' : str(request.form.get("password")),
        'position' : str(request.form.get("position")),
        'email' : str(request.form.get("email"))
        }

    headers = {'content-type': 'application/json'}
    r = requests.request("POST", url, data = json.dumps(params),headers = headers)
    return render_template("log_in.html", response_status = r.status_code)

@app.route("/car_list", methods=["GET","POST"])
def car_list():
    if request.method == "POST":
        url = "http://localhost:3001/cars"
        params = {'id': str(request.form.get("CarID")),
            'entrydate': str(request.form.get("EntryDate")),
            'kmdriven': str(request.form.get("KmDriven")),
            'releaseyear': str(request.form.get("ReleaseYear")),
            'condition': str(request.form.get("CarCondition")),
            'pricekm': str(request.form.get("PriceKm"))
            }
        headers = {'content-type': 'application/json'}
        r = requests.request('POST',url, data = json.dumps(params), headers=headers)
        
    
    url = "http://localhost:3001/cars"
    r = requests.request("GET",url).json()

    return render_template("car_list.html",responses = r)

@app.route("/add_car_form")
def add_car_form():
    
    today = date.today()
    d1 = today.strftime("%Y-%m-%d")

    return render_template("add_car_form.html",today = d1)

@app.route("/delete_confirmation", methods=["POST"])
def delete_confirmation():
    deleteID = str(request.form.get("DeleteID"))
    entryDate = str(request.form.get("DeleteEntrydate"))
    kmDriven = str(request.form.get("DeleteKmdriven"))
    releaseYear = str(request.form.get("DeleteReleaseyear")) 
    condition = str(request.form.get("DeleteCondition"))
    priceKm = str(request.form.get("DeletePricekm"))
    return render_template("delete_confirmation.html", deleteID = deleteID, entryDate = entryDate, kmDriven = kmDriven, releaseYear = releaseYear, condition = condition, priceKm = priceKm)

@app.route("/delete", methods=["POST"])
def delete():
    url = 'http://localhost:3001/cars/' + str(request.form.get("DeleteID"))
    delete_r = requests.request('DELETE',url)
    return redirect(url_for("car_list"))

if __name__ == '__main__':
    app.run(port=5001)