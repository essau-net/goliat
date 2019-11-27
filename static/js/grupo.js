var idIntegrantes = []

function seleccionado(idCheckbox){
    var checkBox = document.getElementById(idCheckbox)
    if (checkBox.checked){
        
        var eliminar = idIntegrantes.indexOf(checkBox.value)
        idIntegrantes.splice(eliminar, 1)
        console.log(idIntegrantes, "Posiscion a eliminar" + eliminar)
        checkBox.removeAttribute("name")
        checkBox.checked = false
    } else{
        idIntegrantes.push(checkBox.value)
        checkBox.setAttribute("name","idUsuario")
        checkBox.checked = true
        console.log("idIntegrantes al seleccionar: "+ idIntegrantes)
    }
}
function pasandoIntegrantes (){
    var misCabeceras = new Headers({
        "Content-Type": "application/json"
    })
    const parametros = {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(idIntegrantes),
        cache: "no-cache",
        headers: misCabeceras
    }
    console.log("idIntegrantes antes de fetch" + idIntegrantes)
    fetch('/iGrupos', parametros).then( function (response){
                                                manejoFetch(response)
                                        }).catch(function (error) {
                                                    errorInfo(error)
    })
    console.log("idIntegrantes despues de fetch" + idIntegrantes)
}

function manejoFetch(response1){
    if(response1.status != 200){
        console.log('Looks like there was a problem. Status code:' + response1.status)
        console.log("idIntegrantes despues de fetch" + idIntegrantes)
        setTimeout(3000)
        return;
    }
    response.json().then(function (data){
        console.log("idIntegrantes despues de fetch" + idIntegrantes)
        setTimeout(3000)
        console.log(data)
        
    })
}

function errorInfo(error1){
    console.log("Fetch error: " + error1)
}