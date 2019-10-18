from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL, MySQLdb
from flask_bcrypt import bcrypt


goliatApp = Flask(__name__)
goliatApp.config['MYSQL_HOST'] = 'localhost'
goliatApp.config['MYSQL_USER'] = 'root'
goliatApp.config['MYSQL_PASSWORD'] = 'mysql'
goliatApp.config['MYSQL_DB'] = 'goliat'
goliatApp.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(goliatApp)


@goliatApp.route('/')
def index():
    return render_template("login.html")


@goliatApp.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        nombres = request.form['nombresE']
        apellidos = request.form['apellidosE']
        fechaNacimiento = request.form['fechaNacimientoE']
        puestoEmpleado = request.form['puestoE']
        tituloUniversitario = request.form['tituloE']
        pais = request.form['paisE']
        estado = request.form['estadoE']
        ciudad = request.form['ciudadE']
        usuario = request.form['usuarioE']
        email = request.form['email']
        clave = request.form['contraUsuario'].encode('utf-8')
        claveCifrada = bcrypt.hashpw(clave, bcrypt.gensalt())
        empleados = mysql.connection.cursor()
        empleados.execute("INSERT INTO empleado (nombresE, apellidosE, fechaNacimientoE,  puestoE, tituloE, paisE, estadoE, ciudadE,  usuarioE, email, contraUsuario) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                          (nombres.upper(), apellidos.upper(), fechaNacimiento, puestoEmpleado, tituloUniversitario, pais, estado, ciudad, usuario, email, claveCifrada,))
        mysql.connection.commit()
        return redirect(url_for('login'))


@goliatApp.route('/login', methods=["GET", "POST"])
def login():
    if request == 'POST':
        usuario = request.form['usuarioN']
        clave = request.form['contraUsuario'].encode('utf-8')
        selUsuario = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        selUsuario.execute(
            "SELECT * FROM empleado WHERE usuarioN = %s", (usuario,))
        u = selUsuario.fetchone()
        if u is not None:
            if bcrypt.hashpw(clave, u["contraUsuario"].encode('utf-8')) == u["contraUsuario"].encode('utf-8'):
                session["nomE"] = u["nomE"]
                return render_template('home.html')
            else:
                return 'Error: clave incorrecta'
        else:
            return 'Error: usuario no existe'
    else:
        return render_template("login.html")


if __name__ == '__main__':
    goliatApp.run(port=3000, debug=True)
