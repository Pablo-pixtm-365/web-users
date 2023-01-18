# Impport the neccesary libraries 
from flask import Flask, render_template, redirect, url_for, request, flash,  Blueprint
from sqlalchemy.engine import URL
from sqlalchemy import create_engine, engine
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask_login import LoginManager, login_user, logout_user, login_required
from models.entities.user import User
from models.modeluser import ModelUser
from flask_wtf.csrf import CSRFProtect

#auth = Blueprint('auth', __name__)
# Innit the aplication or server
app = Flask(__name__)


connection_string = ('Driver={SQL Server};'
                      'Server=YOUR SERVER;'
                      'Database=YOUR DATABASE;'
                      'UID=YOUR USER;'
                      'PWD=YOUR PASSWORD')

connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
app.config['SQLALCHEMY_DATABASE_URI'] = connection_url
#engine = create_engine(connection_url)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["SESSION_COOKIE_SECURE"] = True
app.secret_key = "18ff50fc6850b557eb431c4904621292"

csrf = CSRFProtect(app)
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
            flash("Usuario invalido...")
            return render_template('account.html')
            #user  = str(info["usuario"])
    
    return render_template("account.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/login/register', methods=['GET', 'POST'])
@login_required
def form():
    if request.method == "POST":
        if request.form["btn-send"] == "send-data":
            id_user = int(request.form["id_user"])
            name = request.form["fullname"]
            turno = request.form["turno"]
            enter_date = request.form["enter-date"]
            train_date = request.form["train-date"]
            department = request.form["select1"]
            sex = request.form["select2"]
            nivel = request.form["select3"]
            score = int(request.form["score"])
            query = ("INSERT INTO AsociadosEntrenamiento (ID_usuario, Nombre, Turno, Fecha_ingreso, Fecha_entrenamiento, Departamento, Sexo, Nivel, Puntaje)"
                    " VALUES (:val1, :val2, :val3, :val4, :val5, :val6, :val7, :val8, :val9)")
            vals = {"val1":id_user, "val2":name, "val3":turno, "val4":enter_date, "val5":train_date, "val6":department, "val7":sex, "val8":nivel, "val9":score}
            cursor = db.session.execute(query, vals)
            db.session.commit()
            if cursor:
                return redirect(url_for('form'))
            else:
                flash("Hay informacion faltante...")
        
        #elif request.form[]

        else:
            pass
    return render_template("index.html")


def statuts_401(error):
    return redirect(url_for('login'))


if __name__ == '__main__':
    csrf.init_app(app)
    app.register_error_handler(401, statuts_401)
    app.run(debug=True)