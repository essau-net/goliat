//Obtiene los radios botones de Actividades
var radioAgregar = {
    actFinalizada: document.getElementById("subFinalizada"),
    actPendiente: document.getElementById("subPorRealizar")
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

function manejoRadioModificarF(idRadioFinalizada, idRadioPorRealizar) {
    var subFinalizada = document.getElementById(idRadioFinalizada) 
    var subPendiente = document.getElementById(idRadioPorRealizar)
    subFinalizada.checked = true
    subPendiente.checked = false
}

function manejoRadioModificarP(idRadioFinalizada, idRadioPorRealizar) {
    var subFinalizada = document.getElementById(idRadioFinalizada) 
    var subPendiente = document.getElementById(idRadioPorRealizar)
    subFinalizada.checked = false
    subPendiente.checked = true
}