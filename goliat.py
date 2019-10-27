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
        trabajo = request.form['trabajoUsua']
        tituloUniversitario = request.form['gradoUniUsua']
        pais = request.form['paisOrigenUsua']
        estado = request.form['estadoOrigenUsua']
        ciudad = request.form['ciudadOrigenUsua']
        usuario = request.form['usuario']
        email = request.form['emailUsua']
        clave = request.form['contraUsua'].encode('utf-8')
        claveCifrada = bcrypt.hashpw(clave, bcrypt.gensalt())
        empleados = mysql.connection.cursor()
        empleados.execute("INSERT INTO usuario (nombresUsua, apellidosUsua, fechaNaciUsua, numeroCelUsua, trabajoUsua, gradoUniUsua, paisOrigenUsua, estadoOrigenUsua, ciudadOrigenUsua,  usuario, emailUsua, contraUsua) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                          (nombres.upper(), apellidos.upper(), fechaNacimiento, numeroCel, trabajo, tituloUniversitario, pais, estado, ciudad, usuario, email,  claveCifrada,))
        mysql.connection.commit()
        empleados.close()
        return redirect(url_for('login'))


@goliatApp.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        clave = request.form['contraUsua'].encode('utf-8')
        selUsuario = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        selUsuario.execute(
            "SELECT * FROM usuario WHERE usuario = %s", (usuario,))
        u = selUsuario.fetchone()
        selUsuario.close()
        if u is not None:
            if bcrypt.hashpw(clave, u["contraUsua"].encode('utf-8')) == u["contraUsua"].encode('utf-8'):
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

@goliatApp.route('/perfil')
def perfil():
    return render_template('perfil.html')

@goliatApp.route('/actividades')
def actividades():
    return render_template('actividades.html')

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
    trabajo = request.form['trabajoUsua']
    tituloUniversitario = request.form['gradoUniUsua']
    pais = request.form['paisOrigenUsua']
    estado = request.form['estadoOrigenUsua']
    ciudad = request.form['ciudadOrigenUsua']
    usuario = request.form['usuario']
    email = request.form['emailUsua']
    clave = request.form['contraUsua'].encode('utf-8')
    claveCifrada = bcrypt.hashpw(clave, bcrypt.gensalt())
    empleado = mysql.connection.cursor()
    empleado.execute("INSERT INTO usuario (nombresUsua, apellidosUsua, fechaNaciUsua,  trabajoUsua, gradoUniUsua, paisOrigenUsua, estadoOrigenUsua, ciudadOrigenUsua,  usuario, emailUsua, contraUsua) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                     (nombres.upper(), apellidos.upper(), fechaNacimiento, trabajo, tituloUniversitario, pais, estado, ciudad, usuario, email, claveCifrada,))
    mysql.connection.commit()
    empleado.close()
    return redirect(url_for('sPerfil'))


@goliatApp.route('/uPerfil', methods=["POST"])
def uPerfil():
    idUsuario = request.form['idUsuario']
    nombres = request.form['nombresUsua']
    apellidos = request.form['apellidosUsua']
    fechaNacimiento = request.form['fechaNaciUsua']
    trabajo = request.form['trabajoUsua']
    tituloUniversitario = request.form['gradoUniUsua']
    pais = request.form['paisOrigenUsua']
    estado = request.form['estadoOrigenUsua']
    ciudad = request.form['ciudadOrigenUsua']
    usuario = request.form['usuario']
    email = request.form['emailUsua']
    clave = request.form['contraUsua'].encode('utf-8')
    claveCifrada = bcrypt.hashpw(clave, bcrypt.gensalt())
    empleado = mysql.connection.cursor()
    empleado.execute("UPDATE usuario SET (nombresUsua = %s, apellidosUsua = %s, fechaNaciUsua = %s,  trabajoUsua = %s, gradoUniUsua = %s, paisOrigenUsua = %s, estadoOrigenUsua = %s, ciudadOrigenUsua = %s,  usuario = %s, emailUsua = %s, contraUsua= %s) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                     (nombres.upper(), apellidos.upper(), fechaNacimiento, trabajo, tituloUniversitario, pais, estado, ciudad, usuario, email, claveCifrada,idUsuario))
    mysql.connection.commit()
    empleado.close()
    return redirect(url_for('sPerfil'))
    
@goliatApp.route('/dCliente/<string:idUsuario>', methods = ['GET'])
def dPerfil(idUsuario):
    delUsuario = mysql.connection.cursor()
    delUsuario.execute("DELETE FROM usuario WHERE idUsuario = %s", (idUsuario))
    mysql.connection.commit()
    delUsuario.close()
    return redirect(url_for('sPerfil'))

if __name__ == '__main__':
    goliatApp.secret_key = 'goliatGana'
    goliatApp.run(port=3000, debug=True)
