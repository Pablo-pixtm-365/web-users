from flask import Flask, render_template, redirect, session, url_for, request, session
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text


app = Flask(__name__)


connection_string = ('Driver={SQL Server};'
                      'Server=kukulcan\sqlserver;'
                      'Database=ENTRENAMIENTO_PRUEBAS;'
                      'UID=pduarte;'
                      'PWD=Eduardo_3290')


connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
app.config['SQLALCHEMY_DATABASE_URI'] = connection_url
#engine = create_engine(connection_url)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        if "username" in request.form and "password" in request.form:
            username = request.form["username"]
            password = request.form["password"]
            cursor = db.engine.execute("SELECT * FROM usuario WHERE usuario=? AND Contra=?", (username, password))
            info = cursor.fetchone()
            

            if info["usuario"] == username and info["Contra"] == password:
                return "LOGIN SUCCESSFULL"
            else:
                return "ERROR WITH THE LOGING"

    return render_template("account.html")

#@app.route('/register')


if __name__ == '__main__':
    app.run(debug=True)