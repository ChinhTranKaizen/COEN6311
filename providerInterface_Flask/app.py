from flask import Flask, redirect, url_for, render_template, request
# To start server :
# First: C:\Users\OS\COEN6311\car-rental-all-class
# Then: ./mvnw spring-boot:run
# Please execute: "$env:FLASK_RUN_PORT = 5001" to change your port
from datetime import date

import requests, uuid, json

app = Flask(__name__)

#The first page when starting provider interface: return the log_in page
@app.route("/")
def index():
    # This should return the login page if login successfully, return the index.html page
    return render_template("log_in.html")

#This is a in-between route that processes log-in information
@app.route("/login", methods =["POST"])
def login():
    #Set up the parameters for getting all employees from the database to process log-in information
    url = "http://localhost:3001/employees"
    r = requests.request("GET",url).json()
    username = str(request.form.get("username"))
    password = str(request.form.get("password"))
    login_token = False
    #Check for every responses in the response message, if there is a match, change the token to True
    for response in r:
        if response["name"] == username and response["password"]==password:
            login_token = True
    if login_token:
        return render_template("index.html") #log in sucessfully
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
        params = {'id': str(request.form.get("CarID")),
            'entrydate': str(request.form.get("EntryDate")),
            'kmdriven': str(request.form.get("KmDriven")),
            'releaseyear': str(request.form.get("ReleaseYear")),
            'condition': str(request.form.get("CarCondition")),
            'pricekm': str(request.form.get("PriceKm"))
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
    deleteID = str(request.form.get("DeleteID"))
    entryDate = str(request.form.get("DeleteEntrydate"))
    kmDriven = str(request.form.get("DeleteKmdriven"))
    releaseYear = str(request.form.get("DeleteReleaseyear"))
    condition = str(request.form.get("DeleteCondition"))
    priceKm = str(request.form.get("DeletePricekm"))
    return render_template("delete_confirmation.html", deleteID = deleteID, entryDate = entryDate, kmDriven = kmDriven, releaseYear = releaseYear, condition = condition, priceKm = priceKm)

#This is an in-between route to process delete requests based on ID.
@app.route("/delete", methods=["POST"])
def delete():
    url = 'http://localhost:3001/cars/' + str(request.form.get("DeleteID"))
    delete_r = requests.request('DELETE',url)
    return redirect(url_for("car_list"))

#Sprint 2: edit details of a car

@app.route("/edit_car",methods=["POST"])
def edit_car():
    editID = str(request.form.get("EditID"))
    editEntryDate = str(request.form.get("EditEntrydate"))
    editKmdriven = str(request.form.get("EditKmdriven"))
    editReleaseYear = str(request.form.get("EditReleaseyear"))
    editCondition = str(request.form.get("EditCondition"))
    editPricekm = str(request.form.get("EditPricekm"))
    today = datetime.date.today()
    d1 = today.strftime("%Y-%m-%d")

    return render_template("edit_car.html",today = d1, editID=editID,editEntryDate=editEntryDate,editKmdriven=editKmdriven,editReleaseYear=editReleaseYear,editCondition=editCondition,editPricekm=editPricekm)

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

    url = "http://localhost:3001/cars" + "/" + PutID
    params = {'id': PutID,
            'entrydate': PutEntryDate,
            'kmdriven': PutKmDriven,
            'releaseyear': PutReleaseYear,
            'condition': PutCarCondition,
            'pricekm': PutPriceKm
            }

    headers = {'content-type': 'application/json'}
    r = requests.request('PUT',url, data = json.dumps(params), headers=headers)

    return redirect(url_for("car_list"))

#Sprint 2: filter car with a form
@app.route("/filter_form")
def filter_form():
    today = datetime.date.today()
    d1 = today.strftime("%Y-%m-%d")
    return render_template("filter_form.html",today=d1)

@app.route("/filter_carlist", methods = ["POST"])
def filter_carlist():

    #Get the response from the server
    url = "http://localhost:3001/cars"
    r = requests.request("GET",url).json()

    #Get the responses from the html filter_form


    #Applied the filtering function:
    filtered_response = ""

    return render_template("carlist.html",responses = filtered_response)


if __name__ == '__main__':
    app.run(port=5001)