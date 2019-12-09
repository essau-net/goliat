from flask import Flask, render_template, request, jsonify, make_response, redirect, url_for, session, flash
from flask_mysqldb import MySQL, MySQLdb
from flask_bcrypt import bcrypt
from PIL import Image
import time, datetime, json
import numpy as np
import cgi
import cgitb


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
        claveConfirm = request.form['contraUsua1'].encode('utf-8')
        if clave == claveConfirm:
            claveCifrada = bcrypt.hashpw(clave, bcrypt.gensalt())
            empleados = mysql.connection.cursor()
            empleados.execute("INSERT INTO usuario (nombresUsua, apellidosUsua, fechaNaciUsua, numeroCelUsua, trabajoUsua, gradoUniUsua, paisOrigenUsua, estadoOrigenUsua, ciudadOrigenUsua,  usuario, emailUsua, contraUsua) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                              (nombres.upper(), apellidos.upper(), fechaNacimiento, numeroCel, trabajo, tituloUniversitario, pais, estado, ciudad, usuario, email,  claveCifrada,))
            mysql.connection.commit()
            empleados.close()
            return redirect(url_for('login'))
        else:
            return 'Contraseña incorrecta'


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
                session["idUsuario"] = u["idUsuario"]
                print("\n\n\n\n",type(u))

                return redirect(url_for('sProyecto'))
            else:
                flash('Error: clave incorrecta')
                return redirect(request.url)
        else:
            flash('Error: usuario no existe')
            return redirect(request.url)
    else:
        return render_template("login.html")
@goliatApp.route('/logout')
def logout():
    session.clear()
    return render_template('login.html')


@goliatApp.route('/home')
def home():
    return render_template('home.html')
# - - - - -  - - - - - - - - - - - - - - - - Perfil- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
#-------------------------------------------        Selecion del Perfil          ------------------------------------------------#
@goliatApp.route('/sPerfil', methods=["POST", "GET"])
def sPerfil():
    selUsuario = mysql.connection.cursor()
    selUsuario.execute(
        "SELECT * FROM usuario WHERE idUsuario = %s", (session["idUsuario"],))
    usuario = selUsuario.fetchone()
    selUsuario.close()
    return render_template('perfil.html', perfil=usuario)

#------------------------------------------         Actualizacion de Perfil          ----------------------------------------------#
@goliatApp.route('/uPerfil', methods=["POST"])
def uPerfil():
    idUsuario = request.form['idUsuario']
    nombres = request.form['nombresUsua']
    apellidos = request.form['apellidosUsua']
    fechaNacimiento = request.form['fechaNaciUsua']
    trabajo = request.form['trabajoUsua']
    celular = request.form['numeroCelUsua']
    tituloUniversitario = request.form['gradoUniUsua']
    pais = request.form['paisOrigenUsua']
    estado = request.form['estadoOrigenUsua']
    ciudad = request.form['ciudadOrigenUsua']
    usuario = request.form['usuario']
    email = request.form['emailUsua']
    clave = request.form['contraUsua'].encode('utf-8')
    claveCifrada = bcrypt.hashpw(clave, bcrypt.gensalt())
    empleado = mysql.connection.cursor()
    empleado.execute("UPDATE usuario SET nombresUsua = %s, apellidosUsua = %s, fechaNaciUsua = %s,  trabajoUsua = %s, numeroCelUsua = %s, gradoUniUsua = %s, paisOrigenUsua = %s, estadoOrigenUsua = %s, ciudadOrigenUsua = %s,  usuario = %s, emailUsua = %s, contraUsua= %s WHERE idUsuario = %s",
                     (nombres.upper(), apellidos.upper(), fechaNacimiento, trabajo, celular, tituloUniversitario, pais, estado, ciudad, usuario, email, claveCifrada, idUsuario))
    mysql.connection.commit()
    empleado.close()
    return redirect(url_for('sPerfil'))

#----------------------------------------------------        Eliminar cuenta        ------------------------------#
@goliatApp.route('/dPerfil', methods=['POST'])
def dPerfil():
    delUsuario = mysql.connection.cursor()
    delUsuario.execute(
        "DELETE FROM usuario WHERE idUsuario = %s", (session["idUsuario"],))
    mysql.connection.commit()
    delUsuario.close()
    return redirect(url_for('logout'))

#*************************************************    Actividades       *****************************************#
#------------------------------------------------       Selecionar actividades          ------------------------#
@goliatApp.route('/sActividad', methods=["POST", "GET"])
def sActividad():
    selAct = mysql.connection.cursor()
    selAct.execute(
        "SELECT * FROM actividad INNER JOIN permiso  ON actividad.idAct = permiso.idAct  INNER JOIN cronograma ON permiso.idCronograma = cronograma.idCronograma WHERE permiso.idUsuario = %s  GROUP BY permiso.idAct", (session["idUsuario"],))
    act = selAct.fetchall()
    selAct.close()

    selCronogramas = mysql.connection.cursor()
    selCronogramas.execute(
        "SELECT * FROM cronograma"
    )
    cronogramas = selCronogramas.fetchall()
    selCronogramas.close()

    return render_template('actividades.html', actividad=act, cronogramas = cronogramas)

#------------------------------------------------       Crear nueva Actividad           --------------------------#
@goliatApp.route('/iActividad', methods=["POST"])
def iActividad():
    titulo = request.form['tituloAct']
    proyecto = request.form['idProyecto']
    proposito = request.form['propositoAct']
    fechaPrevistaFin = request.form['fechaPrevistaFin']
    fechaInicioAct = datetime.datetime.now()
    actividad = mysql.connection.cursor()
    valor = request.form.get('actFinalizada')
    if valor:
        finalizada = 'y'
        progresoAct = 100
        fechaFinAct = datetime.datetime.now()
        actividad.execute(
            "INSERT INTO actividad (tituloAct, propositoAct, progresoAct, actFinalizada, fechaIniAct, fechaPrevistaFin, fechaFinAct) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (titulo, proposito, progresoAct, finalizada, fechaInicioAct, fechaPrevistaFin, fechaFinAct))
    else:
        finalizada = 'n'
        progresoAct = 0
        actividad.execute(
            "INSERT INTO actividad (tituloAct, propositoAct, progresoAct, actFinalizada, fechaIniAct, fechaPrevistaFin) VALUES (%s, %s, %s, %s, %s, %s)",
            (titulo, proposito, progresoAct, finalizada, fechaInicioAct, fechaPrevistaFin)
        )
    mysql.connection.commit()
    actividad.execute(
        "SELECT idAct FROM actividad WHERE idAct = (SELECT MAX(idAct) FROM actividad)"
    )
    idAct = actividad.fetchone()
    actividad.close()


    permiso = mysql.connection.cursor()
    permiso.execute(
        "INSERT INTO permiso (idCronograma, idAct, idUsuario) VALUES (%s, %s, %s)",
        (proyecto, idAct["idAct"], session["idUsuario"])
    )
    mysql.connection.commit()
    permiso.close()
    return redirect(url_for('sActividad'))
#------------------------------------------     Editar Actividad        ----------------------------------------------#
@goliatApp.route('/uActividad', methods=["POST"])
def uActividad():
    idProyecto = request.form['idProyecto']
    idPermiso = request.form['idPermiso']
    idAct = request.form['idAct']
    titulo = request.form['tituloAct']
    proposito = request.form['propositoAct']
    fechaPrevistaFin = request.form['fechaPrevistaFin']
    actividad = mysql.connection.cursor()
    valor = request.form.get('actFinalizada')
    if valor:
        finalizada = 'y'
        progresoAct = 100
        fechaFinAct = datetime.datetime.now()
        actividad.execute(
            "UPDATE actividad SET  tituloAct = %s, propositoAct = %s, progresoAct = %s, actFinalizada = %s, fechaPrevistaFin = %s, fechaFinAct = %s WHERE idAct = %s",
            (titulo, proposito, progresoAct, finalizada, fechaPrevistaFin, fechaFinAct, idAct)
        )
    else:
        finalizada = 'n'
        progresoAct = 0
        actividad.execute(
            "UPDATE actividad SET tituloAct = %s, propositoAct = %s, progresoAct = %s, actFinalizada = %s, fechaPrevistaFin = %s WHERE idAct = %s",
            (titulo, proposito, progresoAct, finalizada, fechaPrevistaFin, idAct)
        )
    mysql.connection.commit()
    actividad.close()

    permiso = mysql.connection.cursor()
    permiso.execute(
        "UPDATE permiso SET idCronograma = %s WHERE idPermiso = %s",
        (idProyecto, idPermiso)
    )
    mysql.connection.commit()
    permiso.close()
    return redirect(url_for('sActividad'))

#------------------------------------------     Eliminar Actividad      ----------------------------------------------#
@goliatApp.route('/dActividad<string:idAct>', methods=['GET'])
def dActividad(idAct):
    delAct = mysql.connection.cursor()
    delAct.execute(
        "DELETE FROM actividad WHERE idAct = %s", (idAct,))
    mysql.connection.commit()
    delAct.close()
    return redirect(url_for('sActividad'))

#**************************************************************         SubActividad        *****************************************************#
# --------------------------------------------------------------         SeleccionarActividades      --------------------------------------------#@goliatApp.route('/sActividad', methods=["POST", "GET"])
@goliatApp.route('/sSubAll', methods=["GET", "POST"])
def sSubAll():
    selSub = mysql.connection.cursor()
    selSub.execute(
        "SELECT * FROM sub_actividad INNER JOIN permiso ON  permiso.idSub = sub_actividad.idSub  INNER JOIN actividad ON permiso.idAct = actividad.idAct WHERE permiso.idUsuario = %s", (
            session["idUsuario"],)
    )
    subs = selSub.fetchall()
    selSub.close()

    selAct = mysql.connection.cursor()
    selAct.execute(
        "SELECT * FROM actividad INNER JOIN permiso ON actividad.idAct = permiso.idAct WHERE permiso.idUsuario = %s GROUP BY permiso.idAct", (
            session["idUsuario"],)
    )
    act = selAct.fetchall()
    selAct.close()
    return render_template('sub.html', subActs=subs, actividad=act)

#------------------------------------------------       Crear nueva Subactividad           --------------------------#
@goliatApp.route('/iSubActividad', methods=["POST"])
def iSubActividad():
    idPermiso = request.form['idPermiso']
    obtenerValores = mysql.connection.cursor()
    obtenerValores.execute(
        "SELECT * FROM permiso WHERE idPermiso=%s",
        (idPermiso,)
    )
    valores = obtenerValores.fetchone()
    obtenerValores.close()

    idProyecto = valores["idCronograma"]
    idAct = valores["idAct"]
    titulo = request.form['tituloSub']
    proposito = request.form['propositoSub']
    fechaLimite = request.form['fechaPrevistaFinSub']
    fechaInicioSub = datetime.datetime.now()
    subActividad = mysql.connection.cursor()
    valor = request.form.get('subFinalizada')
    if valor:
        finalizada = 'y'
        progresoSub = 100
        fechaFinSub = datetime.datetime.now()
        subActividad.execute(
            "INSERT INTO sub_actividad (tituloSub, propositoSub, progresoSub, subFinalizada, fechaIniSub, fechaPrevistaFinSub, fechaFinSub) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (titulo, proposito, progresoSub, finalizada, fechaInicioSub, fechaLimite, fechaFinSub)
        )
    else:
        finalizada = 'n'
        progresoSub = request.form["progresoSub"]
        subActividad.execute(
            "INSERT INTO sub_actividad (tituloSub, propositoSub, progresoSub, subFinalizada, fechaIniSub, fechaPrevistaFinSub) VALUES (%s, %s, %s, %s, %s, %s)",
            (titulo, proposito, progresoSub, finalizada, fechaInicioSub, fechaLimite))
    mysql.connection.commit()
    subActividad.close()

    idSub = mysql.connection.cursor()
    idSub.execute(
        "SELECT idSub FROM sub_actividad WHERE idSub=(SELECT MAX(idSub) FROM sub_actividad)"
    )
    idSubValor = idSub.fetchone()
    idSub.close()

    permiso = mysql.connection.cursor()
    permiso.execute(
        "INSERT INTO permiso (idCronograma, idAct, idSub, idUsuario) VALUES (%s, %s, %s, %s)",
        (idProyecto, idAct, idSubValor["idSub"], session["idUsuario"])
    )
    mysql.connection.commit()
    permiso.close()

    numeroSub = mysql.connection.cursor()
    numeroSub.execute(
        "SELECT * FROM actividad WHERE idAct = %s",
        (idAct,)
    )
    numeroSubTotal = numeroSub.fetchone()
    numeroSub.close()

    numeroSubTotal["numeroSubAct"] = numeroSubTotal["numeroSubAct"] + 1
    numeroSubTotal["numeroSubFinalizadas"] = numeroSubTotal["numeroSubFinalizadas"]  + 1    

    nuevaSub = mysql.connection.cursor()
    if finalizada == 'y':
        nuevaSub.execute(
            "UPDATE actividad SET numeroSubAct = %s, numeroSubFinalizadas = %s  WHERE idAct = %s",
            (numeroSubTotal["numeroSubAct"], numeroSubTotal["numeroSubFinalizadas"], idAct))

    elif finalizada == 'n':
        nuevaSub.execute(
            "UPDATE actividad SET numeroSubAct = %s WHERE idAct = %s",
            (numeroSubTotal['numeroSubAct'], idAct)) 
    mysql.connection.commit()
    nuevaSub.close()
    return redirect(url_for('sSubAll'))
#------------------------------------------     Editar subActividad        ----------------------------------------------#
@goliatApp.route('/uSubActividad', methods=["POST"])
def uSubActividad():
    idSub = request.form['idSub']
    idAct = request.form['idAct']
    titulo = request.form['tituloSub']
    proposito = request.form['propositoSub']
    fechaLimite = request.form['fechaPrevistaFinSub']
    fechaInicioSub = datetime.datetime.now()
    subActividad = mysql.connection.cursor()
    valor = request.form.get('subFinalizada')
    if valor:
        finalizada = 'y'
        progresoSub = 100
        fechaFinSub = datetime.datetime.now()
        subActividad.execute(
            "UPDATE sub_actividad SET tituloSub = %s, propositoSub = %s, progresoSub = %s, subFinalizada = %s, fechaIniSub  = %s, fechaPrevistaFinSub = %s, fechaFinSub = %s  WHERE idSub = %s",
            (titulo, proposito, progresoSub, finalizada, fechaInicioSub, fechaLimite, fechaFinSub, idSub))

        numeroSub = mysql.connection.cursor()
        numeroSub.execute(
            "SELECT * FROM actividad WHERE idAct = %s",
            (idAct,)
        )
        numeroSubTotal = numeroSub.fetchone()
        numeroSub.close()
        numeroSubTotal["numeroSubFinalizadas"] = numeroSubTotal["numeroSubFinalizadas"]  + 1    

        subFinalizada = mysql.connection.cursor()
        subFinalizada.execute(
            "UPDATE actividad SET numeroSubFinalizadas = %s  WHERE idAct = %s",
            (numeroSubTotal["numeroSubFinalizadas"], idAct)
        )
        subFinalizada.close()
    else:
        finalizada = 'n'
        progresoSub = request.form['progresoSub']
        subActividad.execute(
            "UPDATE sub_actividad SET tituloSub = %s, propositoSub = %s, progresoSub = %s, subFinalizada = %s, fechaIniSub = %s, fechaPrevistaFinSub = %s  WHERE idSub = %s",
            (titulo, proposito, progresoSub, finalizada, fechaInicioSub, fechaLimite, idSub)
        )

    mysql.connection.commit()
    subActividad.close()

    permiso = mysql.connection.cursor()
    permiso.execute(
        "UPDATE permiso SET idAct = %s, idUsuario = %s WHERE  idSub = %s ",
        (idAct, session["idUsuario"],  idSub)
    )
    mysql.connection.commit()
    permiso.close()
    return redirect(url_for('sSubAll'))

#------------------------------------------     Eliminar SubActividad      ----------------------------------------------#
@goliatApp.route('/dSub', methods=['POST'])
def dSubActividad():
    idSub = request.form["idSub"]
    delSub = mysql.connection.cursor()
    delSub.execute(
        "DELETE FROM sub_actividad WHERE idSub = %s", (idSub,)
    )
    mysql.connection.commit()
    delSub.close()
    return redirect(url_for('sSubAll'))

#*********************************          GRUPOS          **************************#
@goliatApp.route('/sGrupos', methods=["POST", "GET"])
def sGrupos():
    selGrupos = mysql.connection.cursor()
    selGrupos.execute(
        "SELECT * FROM grupo INNER JOIN usuario ON grupo.idUsuario = usuario.idUsuario WHERE grupo.idUsuario = %s GROUP BY nombreGrupo",
        (session["idUsuario"],)
    )
    grupo = selGrupos.fetchall()
    selGrupos.close()
    gruposPertenecientes = []
    for pertenece in grupo:
        selTablaGrupo = mysql.connection.cursor()
        selTablaGrupo.execute(
            "SELECT * FROM grupo INNER JOIN usuario ON grupo.idUsuario = usuario.idUsuario WHERE grupo.nombreGrupo = %s",
            (pertenece["nombreGrupo"],)
        )
        integrante = selTablaGrupo.fetchall()
        gruposPertenecientes.append(integrante)
    selTablaGrupo.close()
    gruposPertenecientes = json.dumps(gruposPertenecientes)

    selUsuarios = mysql.connection.cursor()
    selUsuarios.execute(
        "SELECT * FROM usuario"
    )
    usuario = selUsuarios.fetchall()
    selUsuarios.close()
    
    return render_template('grupo.html', grupos = grupo, usuarios = usuario, integrantes = gruposPertenecientes) 

@goliatApp.route('/iGrupos', methods=["POST"])
def iGrupo():
    grupo = request.get_json()
    for idUsuario in  grupo["idIntegrantes"]:
        insertGrupo = mysql.connection.cursor()
        insertGrupo.execute(
            "INSERT INTO grupo (idUsuario, idEncargado, nombreGrupo) VALUES(%s, %s, %s)",
            (idUsuario, grupo["idEncargado"], grupo["nombreGrupo"])
        )
        mysql.connection.commit()
        insertGrupo.close()
    return redirect(url_for('sGrupos'))
@goliatApp.route('/uGrupo', methods=["POST"])
def uGrupo():
    grupoEditar = request.get_json()
    print("\n\n\n", grupoEditar, "\n\n")
    deleteGrupo = mysql.connection.cursor()
    deleteGrupo.execute(
        "DELETE FROM grupo WHERE nombreGrupo = %s",
        (grupoEditar["anteriorGrupo"],)
    )
    mysql.connection.commit()
    deleteGrupo.close()
    
    
    for idUsuario in  grupoEditar["idIntegrantes"]:
        insertGrupo = mysql.connection.cursor()
        insertGrupo.execute(
            "INSERT INTO grupo (idUsuario, idEncargado, nombreGrupo) VALUES(%s, %s, %s)",
            (idUsuario, grupoEditar["idEncargado"], grupoEditar["nombreGrupo"])
        )
        mysql.connection.commit()
        insertGrupo.close()
        
    return redirect(url_for('sGrupos'))
@goliatApp.route('/dGrupo', methods=["POST"])
def dGrupo():
    idGrupo = request.form['idGrupo']
    deleteGrupo = mysql.connection.cursor()
    deleteGrupo.execute(
        "DELETE FROM grupo WHERE idGrupo = %s",
        (idGrupo,)
    )
    mysql.connection.commit()
    deleteGrupo.close()
    return redirect(url_for('sGrupos'))
#**********************         Proyecto         ******************#
@goliatApp.route('/sProyecto', methods=["POST", "GET"])
def sProyecto():
    selProyecto = mysql.connection.cursor()
    selProyecto.execute(
        "SELECT * FROM cronograma"
    )
    cronograma = selProyecto.fetchall()
    selProyecto.close()
    return render_template('proyectos.html',  cronograma = cronograma)
@goliatApp.route('/iProyecto', methods = ["POST"])
def iProyecto():
    nombreProyecto = request.form['nombreProyecto']
    descripcionProyecto = request.form['descripcionProyecto']
    insertProyecto = mysql.connection.cursor()
    insertProyecto.execute(
        "INSERT INTO cronograma (nombreProyecto, descripcionProyecto) VALUES (%s, %s)",
        (nombreProyecto, descripcionProyecto)
    )
    mysql.connection.commit()
    insertProyecto.close()

    #selecciona el ultimo proyecto para añadirlo a permiso
    selProyecto = mysql.connection.cursor()
    selProyecto.execute(
        "SELECT idCronograma FROM cronograma WHERE idCronograma=(SELECT MAX(idCronograma) FROM cronograma)"
    )
    idProyecto = selProyecto.fetchone()
    insertPermiso = mysql.connection.cursor()
    insertPermiso.execute(
        "INSERT INTO permiso (idCronograma, idUsuario) VALUES (%s, %s)",
        (idProyecto["idCronograma"], session["idUsuario"])
    )
    mysql.connection.commit()
    insertProyecto.close()
    return redirect(url_for('sProyecto'))

@goliatApp.route('/uProyecto', methods=["POST"])
def uProyecto():
    idCronograma = request.form['idCronograma']
    nombreProyecto = request.form['nombreProyecto']
    descripcionProyecto = request.form['descripcionProyecto']
    updateProyecto = mysql.connection.cursor()
    updateProyecto.execute(
        "UPDATE cronograma SET nombreProyecto = %s, descripcionProyecto = %s WHERE idCronograma = %s",
        (nombreProyecto, descripcionProyecto, idCronograma)
    )
    mysql.connection.commit()
    updateProyecto.close()
    return redirect(url_for('sProyecto'))
@goliatApp.route('/dProyecto', methods=["POST"])
def dProyecto():
    idCronograma = request.form['idCronograma']
    deleteProyecto = mysql.connection.cursor()
    deleteProyecto.execute(
        "DELETE FROM cronograma WHERE idCronograma = %s",
        (idCronograma,)
    )
    mysql.connection.commit()
    deleteProyecto.close()
    return redirect(url_for('sProyecto'))
    
if __name__ == '__main__':
    goliatApp.secret_key = 'goliatGana'
    goliatApp.run(port=3000, debug=True)