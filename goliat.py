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
        nombres = request.form['nombresUsua']
        apellidos = request.form['apellidosUsua']
        fechaNacimiento = request.form['fechaNaciUsua']
        numeroCel = request.form['numeroCelUsua']
        puestosmpleado = request.form['trabajoUsua']
        tituloUniversitario = request.form['gradoUniUsua']
        pais = request.form['paisOrigenUsua']
        estado = request.form['estadoOrigenUsua']
        ciudad = request.form['ciudadOrigenUsua']
        usuario = request.form['usuario']
        email = request.form['emailUsua']
        clave = request.form['contraUsuario'].encode('utf-8')
        claveCifrada = bcrypt.hashpw(clave, bcrypt.gensalt())
        empleados = mysql.connection.cursor()
        empleados.execute("INSERT INTO empleado (nombresUsua, apellidosUsua, fechaNaciUsua, numeroCelUsua, trabajoUsua, gradoUniUsua, paisOrigenUsua, estadoOrigenUsua, ciudadOrigenUsua,  usuario, emailUsua, contraUsuario) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                          (nombres.upper(), apellidos.upper(), fechaNacimiento, numeroCel, puestosmpleado, tituloUniversitario, pais, estado, ciudad, email, usuario,  claveCifrada,))
        mysql.connection.commit()
        empleados.close()
        return redirect(url_for('login'))


@goliatApp.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        clave = request.form['contraUsuario'].encode('utf-8')
        selUsuario = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        selUsuario.execute(
            "SELECT * FROM empleado WHERE usuario = %s", (usuario,))
        u = selUsuario.fetchone()
        selUsuario.close()
        if u is not None:
            if bcrypt.hashpw(clave, u["contraUsuario"].encode('utf-8')) == u["contraUsuario"].encode('utf-8'):
                session["nombresUsua"] = u["nombresUsua"]
                session["appellidosE"] = u["apellidosUsua"]
                return render_template('home.html')
            else:
                return 'Error: clave incorrecta'
        else:
            return 'Error: usuario no existe'
    else:
        return render_template("login.html")


@goliatApp.route('/logout')
def logout():
    session.clear()
    return render_template('login.html')


@goliatApp.route('/home')
def home():
    return render_template('home.html')

# - - - - -  - - - - - - - - - - - - - - - - Empleados- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
@goliatApp.route('/sPerfil', methods=["GET", "POST"])
def sPerfil():
    selEmpleado = mysql.connection.cursor()
    selEmpleado.execute("SELECT * FROM jugadores")
    empleado = selEmpleado.fetchall()
    selEmpleado.close()
    return render_template('perfil.html', perfil=empleado)


@goliatApp.route('/iPerfil', methods=["POST"])
def iPerfil():
    nombres = request.form['nombresUsua']
    apellidos = request.form['apellidosUsua']
    fechaNacimiento = request.form['fechaNaciUsua']
    puestosmpleado = request.form['trabajoUsua']
    tituloUniversitario = request.form['gradoUniUsua']
    pais = request.form['paisOrigenUsua']
    estado = request.form['estadoOrigenUsua']
    ciudad = request.form['ciudadOrigenUsua']
    usuario = request.form['usuario']
    email = request.form['emailUsua']
    clave = request.form['contraUsuario'].encode('utf-8')
    claveCifrada = bcrypt.hashpw(clave, bcrypt.gensalt())
    empleado = mysql.connection.cursor()
    empleado.execute("INSERT INTO empleado (nombresUsua, apellidosUsua, fechaNaciUsua,  trabajoUsua, gradoUniUsua, paisOrigenUsua, estadoOrigenUsua, ciudadOrigenUsua,  usuario, emailUsua, contraUsuario) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                     (nombres.upper(), apellidos.upper(), fechaNacimiento, puestosmpleado, tituloUniversitario, pais, estado, ciudad, usuario, email, claveCifrada,))
    mysql.connection.commit()
    empleado.close()
    return redirect(url_for('sPerfil'))



if __name__ == '__main__':
    goliatApp.secret_key = 'goliatGana'
    goliatApp.run(port=3000, debug=True)
