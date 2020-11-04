
import pymysql
from flask import Flask
from flask import render_template
from flask import request
from flask import session
import traceback
import pymysql.cursors



app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '123'

app.secret_key = '123'
app.config.update(SECRET_KEY='123')
#Declare a connection with userdatabase which stores customer information
db = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123',
    db='user',
    charset='utf8'
)

#Points to the database for further connect
cursor = db.cursor()

#Routes to login page on start up
@app.route('/')
def index():
    return render_template("index.html")


#The form on login page will send a post requests to this route to check if there is an entry in the database for such customer
@app.route('/loginprocess',methods=["GET","POST"])
def login():
    #Get data back from the form
    username = str(request.form.get("username"))
    password = str(request.form.get("password"))
    #Build a sql to go through customer database
    select_sql = 'select * from customer where username="%s" and password="%s";' % (username, password)
    try:
        cursor.execute(select_sql)
        results = cursor.fetchall()
        print(len(results))
        #If there is a result in the query then returns login success page
        if len(results) == 1:
            session['username'] = username
            session.permanent = True
            return render_template("loginprocess.html")
        else:
            #else return log in error page.
            return render_template("loginerr.html")
            db.commit()
    except:
        traceback.print_exc()
        db.rollback()
    return render_template("index.html")

@app.context_processor
def my_context_processor():
    user = session.get('username')
    if user:
        return {'loginuser': user}
    return {}

#This is a processor to add data to the database based on the data from the submitted form
@app.route('/addcustomer', methods=["POST"])
def registerprocess():
    #Get data from the form using post method
    username = str(request.form.get("username"))
    password = str(request.form.get("password"))
    firstname = str(request.form.get("firstname"))
    lastname = str(request.form.get("lastname"))
    email = str(request.form.get("email"))
    phone = str(request.form.get("phone"))
    address = str(request.form.get("address"))
    postal = str(request.form.get("postal"))

    #Insert a new customer into post request
    insert_user_sql = 'INSERT INTO customer(username, password,firstname,lastname,email,phone,address,postal) ' \
                      'VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\");' % (
                      username, password, firstname, lastname, email, phone, address, postal)
    try:
        cursor.execute(insert_user_sql)
        db.commit()
        return render_template('user.html')
    except:

        traceback.print_exc()

        db.rollback()
    return render_template("registererr.html")

#When this route is called, return the registration page.
@app.route('/register', methods=["GET", "POST"])
def register():
    return render_template("user-register.html")

#This is an inbetween route that process the modifying profile process, if the appending to the data base is successful then returns
#modify sucess else return modify error
@app.route('/modifyprofile', methods=["POST"])
def modify():
    currentuser = str(session.get('username'))
    password = str(request.form.get("password"))
    firstname = str(request.form.get("firstname"))
    lastname = str(request.form.get("lastname"))
    email = str(request.form.get("email"))
    phone = str(request.form.get("phone"))
    address = str(request.form.get("address"))
    postal = str(request.form.get("postal"))
    newinfo = 'update customer set password="%s",firstname="%s",lastname="%s",email = "%s",' \
              'phone="%s", address = "%s", postal="%s" where username="%s"' % (
              password, firstname, lastname, email, phone, address, postal, currentuser)
    try:
        cursor.execute(newinfo)
        db.commit()
        return render_template('modify.html')
    except:

        traceback.print_exc()
        db.rollback()
        return render_template("modifyerr.html")

#This route is to route to modify profile html page.
@app.route('/userprofile', methods=["GET","POST"])
def modifyprofile():

    currentuser = str(session.get('username'))
    select_sql = 'select * from customer where username= "%s" ;' % (currentuser)
    cursor.execute(select_sql)
    row = cursor.fetchall()

    return render_template("modifyprofile.html", row=row)

@app.route('/search')
def search():
    return render_template("search.html")


if __name__ == "__main__":
    app.run(port='5000', host="127.0.0.1", debug=True)
