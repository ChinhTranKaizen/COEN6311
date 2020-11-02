
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

db = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123',
    db='user',
    charset='utf8'
)

cursor = db.cursor()


@app.route('/')
def index():
    return render_template("index.html")



@app.route('/loginprocess',methods=["GET","POST"])
def login():
    username = str(request.form.get("username"))
    password = str(request.form.get("password"))
    select_sql = 'select * from customer where username="%s" and password="%s";' % (username, password)
    try:
        cursor.execute(select_sql)
        results = cursor.fetchall()
        print(len(results))
        if len(results) == 1:
            session['username'] = username
            session.permanent = True
            return render_template("loginprocess.html")
        else:
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


@app.route('/addcustomer', methods=["POST"])
def registerprocess():

    username = str(request.form.get("username"))
    password = str(request.form.get("password"))
    firstname = str(request.form.get("firstname"))
    lastname = str(request.form.get("lastname"))
    email = str(request.form.get("email"))
    phone = str(request.form.get("phone"))
    address = str(request.form.get("address"))
    postal = str(request.form.get("postal"))

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


@app.route('/register', methods=["GET", "POST"])
def register():
    return render_template("user-register.html")

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
