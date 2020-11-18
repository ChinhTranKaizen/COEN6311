
import requests ,json
from flask import Flask, redirect, url_for, render_template, request, session, abort, jsonify



app = Flask(__name__)

app.secret_key = "123"


# Routes to login page on start up
@app.route('/')
def index():

    return render_template("index.html")

@app.context_processor
def my_context_processor():
    user = session.get('username')
    if user:
        return {'loginuser': user}
    return {}

# The form on login page will send a post requests to this route to check if there is an entry in the database for such customer
@app.route('/loginprocess' ,methods=["POST"])
def login():

    # Set up the parameters for getting all customers from the database to process log-in information
    url = "http://localhost:3001/customers"
    r = requests.request("GET", url).json()
    username = str(request.form.get("username"))
    password = str(request.form.get("password"))

    # Check for every responses in the response message, if there is a match, change the token to username
    for response in r:
        if response["username"] == username and response["password"] == password:
            session['username'] = response['username']
            break
    if session.get('username') is not None:
        return render_template("loginprocess.html", username=session.get('username'))  # log in sucessfully
    else:
        return render_template("loginerr.html")  # log in fails

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


# This is a processor to add customer to the database based on the data from the submitted form
@app.route('/addcustomer', methods=["POST"])
def registerprocess():
    if request.method == "POST":
        # Preparing the parameters to send the Java spring boot server
        url = 'http://localhost:3001/customers'
        params = {
            'username' : str(request.form.get("username")),
            'password' : str(request.form.get("password")),
            'firstname' : str(request.form.get("firstname")),
            'lastname': str(request.form.get("lastname")),
            'phone': str(request.form.get("phone")),
            'email' : str(request.form.get("email")),
            'country': str(request.form.get("country")),
            'city': str(request.form.get("city")),
            'province': str(request.form.get("province")),
            'postal': str(request.form.get("postal")),
            'activation': str(True)
            }

        headers = {'content-type': 'application/json'}
        r = requests.request('POST', url, data=json.dumps(params), headers=headers)

        return render_template("user.html", response=r)

    else:
        return render_template("registererr.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    return render_template("user-register.html")


# This is an inbetween route that process the modifying profile process
# modify sucess else return modify error
@app.route('/modifyprofile', methods=["GET","POST"])
def modify():
    modifyid = str(request.form.get("customerid"))
    url = "http://localhost:3001/customers" + "/" + modifyid
    modify = {
        'customerid': modifyid,
        'username': str(request.form.get("username")),
        'password': str(request.form.get("password")),
        'firstname': str(request.form.get("firstname")),
        'lastname': str(request.form.get("lastname")),
        'phone': str(request.form.get("phone")),
        'email': str(request.form.get("email")),
        'country': str(request.form.get("country")),
        'city': str(request.form.get("city")),
        'province': str(request.form.get("province")),
        'postal': str(request.form.get("postal")),
        'activation': True
    }
    print(modify)
    print(url)
    headers = {'content-type': 'application/json'}
    r = requests.request('PUT', url, data=json.dumps(modify), headers=headers)
    return render_template("modify.html",response = r)

#This route is to route to get customer's profile.
@app.route('/userprofile', methods=["GET","POST"])
def profile():
    url = 'http://localhost:3001/customers'
    r = requests.request("GET", url).json()
    username = session.get('username')
    if username != "":
        for customer in r:
            if customer["username"] == username:
                print(customer)
                return render_template("modifyprofile.html", customer=customer, username = session.get('username'))
    else:
        return render_template("modifyerr.html")


# sprint 2 filter of cars in database
# This is a processor to show cars the database which customer wants to rent
@app.route('/search', methods=["GET" ,"POST"])
def search():
    url = "http://localhost:3001/cars"
    r = requests.request("GET" ,url).json()
    return render_template("search.html" ,responses = r ,username = session.get('username'))

#filter car with a form
@app.route("/filter_form", methods=["POST", "GET"])
def filter_form():
    if request.method == "POST":
        url = "http://localhost:3001/cars"
        r = requests.request("GET", url).json()

        # Processing Km Driven data
        KmDrivenMax = request.form.get('KmDrivenMax')
        KmDrivenMin = request.form.get('KmDrivenMin')
        if KmDrivenMax != "" or KmDrivenMin != "":
            if KmDrivenMax != "":
                cars_for_removal = []
                for car in r:
                    c = int(car['kmdriven'])
                    if c > int(KmDrivenMax):
                        cars_for_removal.append(car)
                for car in cars_for_removal:
                    r.remove(car)
            if KmDrivenMin != "":
                cars_for_removal = []
                for car in r:
                    c = int(car['kmdriven'])
                    if c < int(KmDrivenMin):
                        cars_for_removal.append(car)
                for car in cars_for_removal:
                    r.remove(car)
            if (KmDrivenMax != "" and KmDrivenMin != "") and (int(KmDrivenMax) < int(KmDrivenMin)):
                return abort(
                    make_response({'message': "The max km driven cannot be smaller than the min km driven."}, 400))

        # Procesing CarCondition
        conditions = ["good", "very good"]
        CarCondition = request.form.get('CarCondition')
        if CarCondition != "":
            if CarCondition not in conditions:
                abort(make_response({'message': "Invalid car condition given"}, 400))
            cars_for_removal = []
            for car in r:
                if car['condi'] != CarCondition:
                    cars_for_removal.append(car)
            for car in cars_for_removal:
                r.remove(car)

        # Processing Car Brand
        brands = ["Ford", "Renault", "BMW", "Peugeot", "Citroen"]
        Brand = request.form.get('Brand')
        if Brand != "":
            if Brand not in brands:
                abort(make_response({'message': "Invalid car brand given"}, 400))
            cars_for_removal = []
            for car in r:
                if car['brand'] != Brand:
                    cars_for_removal.append(car)
            for car in cars_for_removal:
                r.remove(car)

        # Processing Car Style
        styles = ["fullsize", "standard", "standardsuv", "premiumsuv", "minivan"]
        Style = request.form.get('Style')
        if Style != "":
            if Style not in styles:
                abort(make_response({'message': "Invalid car type given"}, 400))
            cars_for_removal = []
            for car in r:
                if car['style'] != Style:
                    cars_for_removal.append(car)
            for car in cars_for_removal:
                r.remove(car)


        # Processing price per day
        PriceDayMax = request.form.get('PriceDayMax')
        PriceDayMin = request.form.get('PriceDayMin')
        if PriceDayMax != "" or PriceDayMin != "":
            if PriceDayMax != "":
                cars_for_removal = []
                for car in r:
                    c = int(car['priceday'])
                    if c > int(PriceDayMax):
                        cars_for_removal.append(car)
                for car in cars_for_removal:
                    r.remove(car)
            if PriceDayMin != "":
                cars_for_removal = []
                for car in r:
                    c = int(car['priceday'])
                    if c < int(PriceDayMin):
                        cars_for_removal.append(car)
                for car in cars_for_removal:
                    r.remove(car)
            if (PriceDayMax != "" and PriceDayMin != "") and (int(PriceDayMax) < int(PriceDayMin)):
                return abort(
                    make_response({'message': "The max price per day cannot be smaller than the min price per day."},
                                  400))
        filtered_response = r
        print(filtered_response)
        return render_template("carlist.html", responses=filtered_response, username=session.get('username'))


@app.route('/confirm_order', methods=["GET" ,"POST"])
def confirm_order():

    return render_template("confirm_order.html" ,username = session.get('username'))


if __name__ == "__main__":
    app.run(port='5000', host="127.0.0.1", debug=True)
