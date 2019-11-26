//Obtiene los radios botones de Actividades
var radioAgregar = {
    actFinalizada: document.getElementById("actFinalizada"),
    actPendiente: document.getElementById("actPorRealizar")
}

//Obtiene valores para personalizar grafica
var grafica = document.getElementsByClassName("progresoGrafica")
var porcentaje = document.getElementsByClassName("progresoNum")

for (var contador = 0; contador < grafica.length; contador++) {
    var numero = porcentaje[contador].innerHTML
    numero = numero.replace('%', '')
    segundoNumero = 100 - parseInt(numero)
    valorString = numero + "," + segundoNumero
    graficaChida = grafica[contador]
    graficaChida.style.strokeDasharray = valorString

}
//Manejo de redio botones de actividades 
radioAgregar.actFinalizada.addEventListener("click", manejoRadioAgregarF)
radioAgregar.actPendiente.addEventListener("click", manejoRadioAgregarP)

function manejoRadioAgregarF() {
    radioAgregar.actFinalizada.checked = true
    radioAgregar.actPendiente.checked = false
}

function manejoRadioAgregarP() {
    radioAgregar.actFinalizada.checked = false
    radioAgregar.actPendiente.checked = true
}

function manejoRadioModificarF(idRadioFinalizada, idRadioPorRealiza) {
    var actFinalizada =  document.getElementById(idRadioFinalizada)
    var actPendiente = document.getElementById(idRadioPorRealiza)
    console.log("Finalizada:  \t",  idRadioFinalizada, "\nactPendiente:\t", idRadioPorRealiza)
    actFinalizada.checked = true
    actPendiente.checked = false
}

function manejoRadioModificarP(idRadioFinalizada, idRadioPorRealiza) {
    var actFinalizada =  document.getElementById(idRadioFinalizada)
    var actPendiente = document.getElementById(idRadioPorRealiza)
    actFinalizada.checked = false
    actPendiente.checked = true
}