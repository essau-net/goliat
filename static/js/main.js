window.addEventListener("load",loadPagina)

function loadPagina(){
    var radioAgregar = {
        actFinalizada: document.getElementById("actFinalizada"),
        actPendiente: document.getElementById("actPorRealizar")
    }
    var radioModificar = {
        actFinalizada: document.getElementById("actFinalizadaM"),
        actPendiente: document.getElementById("actPorRealizarM")
    }

    
    radioAgregar.actFinalizada.addEventListener("click", manejoRadioAgregarF)
    radioAgregar.actPendiente.addEventListener("click", manejoRadioAgregarP)
    radioModificar.actFinalizada.addEventListener("click", manejoRadioModificarF)
    radioModificar.actPendiente.addEventListener("click", manejoRadioModificarP)

    var grafica = document.getElementsByClassName("progresoGrafica")
    var porcentaje = document.getElementsByClassName("progresoNum")  

    for (var contador = 0; contador < grafica.length; contador++){
        var numero = porcentaje[contador].innerHTML
        numero = numero.replace('%', '')
        segundoNumero = 100 - parseInt(numero)
        valorString = numero + "," + segundoNumero
        graficaChida = grafica[contador]
        graficaChida.style.strokeDasharray = valorString
        
    }
    
}

function manejoRadioAgregarF() {
    radioAgregar.actFinalizada.checked = true
    radioAgregar.actPendiente.checked = false
}

function manejoRadioAgregarP() {
    radioAgregar.actFinalizada.checked = false
    radioAgregar.actPendiente.checked = true
}

function manejoRadioModificarF() {
    radioModificar.actFinalizada.checked = true
    radioModificar.actPendiente.checked = false
}

function manejoRadioModificarP() {
    radioModificar.actFinalizada.checked = false
    radioModificar.actPendiente.checked = true
}