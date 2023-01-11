from flask import Flask, render_template, redirect, session, url_for, request, session, flash
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text


app = Flask(__name__)


connection_string = ("")


connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
app.config['SQLALCHEMY_DATABASE_URI'] = connection_url
#engine = create_engine(connection_url)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)

@app.route('/login', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        if "username" in request.form and "password" in request.form:
            username = request.form["username"]
            password = request.form["password"]
            cursor = db.session.execute("SELECT usuario, Contra FROM usuario WHERE usuario=:val1 AND Contra=:val2", {'val1': username, 'val2':password})
            info = cursor.fetchone()
            
            #print(username)
            #print(password)
            #print(info)
            if info is not None:
                if str(info["usuario"]) == username and info["Contra"] == password:
                    return redirect(url_for("form"))
            else:
                flash('Wrong email or password')
                return render_template("account.html")

    return render_template("account.html")



@app.route('/login/register', methods=['GET', 'POST'])
def form():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)