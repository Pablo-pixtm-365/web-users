# Impport the neccesary libraries 
from flask import Flask, render_template, redirect, session, url_for, request, session, flash,  Blueprint
from sqlalchemy.engine import URL
from sqlalchemy import create_engine, engine
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask_login import LoginManager, login_user, logout_user, login_required
from models.entities.user import User
from models.modeluser import ModelUser

#auth = Blueprint('auth', __name__)
# Innit the aplication or server
app = Flask(__name__)


connection_string = ""


connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
app.config['SQLALCHEMY_DATABASE_URI'] = connection_url
#engine = create_engine(connection_url)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = "18ff50fc6850b557eb431c4904621292"


db = SQLAlchemy(app)
login_manager_app = LoginManager(app)
#login_manager_app.init_app(app)


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)

@app.route('/')
def index():
    return redirect(url_for('login'))




@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        #if "username" in request.form and "password" in request.form:
        username = request.form["username"]
        password2 = request.form["password"]
        #query = text("SELECT usuario, Contra FROM usuario where usuario = {} AND Contra = '{}'".format(username, password))
        #cursor = engine.execute(query)
        user = User(0, username, password2)
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password == password2 and logged_user.username == username:
                login_user(logged_user)
                return redirect(url_for('form'))
            else:
                flash("Contraseña incorrecta...")
                return render_template('account.html')

        else:
            flash("Usuario no encontrado...")
            return render_template('account.html')
            #user  = str(info["usuario"])
    
    return render_template("account.html")

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/login/register', methods=['GET', 'POST'])
def form():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)