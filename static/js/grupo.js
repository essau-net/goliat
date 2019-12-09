
var idIntegrante = []
var idIntegranteEditar = {}
var checkBoxP =  document.getElementsByClassName("modificandoCheckbox")
for (var y = 0; y < tablaGrupo.length ; y++){
    var ulGrupo = document.getElementById(tablaGrupo[y][0]["nombreGrupo"])
        for (var x = 0; x< tablaGrupo[y].length; x++){
            var contenido = '<li class="list-group-item"><b>Integrante:</b>' + tablaGrupo[y][x].nombresUsua + tablaGrupo[y][x].apellidosUsua + '</li>'
            ulGrupo.insertAdjacentHTML('beforeend', contenido)
            for (var z=0; z < checkBoxP.length; z++){
                if (checkBoxP[z].id == "modificar" + tablaGrupo[y][x].idUsuario + tablaGrupo[y][x].nombreGrupo){
                    checkBoxP[z].checked = true
                    if(idIntegranteEditar[tablaGrupo[y][x].nombreGrupo] == undefined){
                        identificarGrupo["nombreGrupos"].push(tablaGrupo[y][x].nombreGrupo)
                        idIntegranteEditar[tablaGrupo[y][x].nombreGrupo] = []
                    }
                    idIntegranteEditar[tablaGrupo[y][x].nombreGrupo].push(tablaGrupo[y][x].idUsuario)
                }
            }
        }
}
function seleccionado(idCheckbox){
    var checkBox = document.getElementById(idCheckbox)
    if (checkBox.checked){
        
        var eliminar = idIntegrante.indexOf(checkBox.value)
        idIntegrante.splice(eliminar, 1)
        checkBox.removeAttribute("name")
        checkBox.checked = false
    } else{
        idIntegrante.push(checkBox.value)
        checkBox.setAttribute("name","idUsuario")
        checkBox.checked = true
    }
}
function editar(idCheckbox, nombreGrupo){
    var checkB = document.getElementById(idCheckbox)
    if (checkB.checked){
        var eliminar = idIntegranteEditar[nombreGrupo].indexOf(checkB.value)
        idIntegranteEditar[nombreGrupo].splice(eliminar, 1)
        checkB.removeAttribute("name")
        checkB.checked = false
    } else{
        idIntegranteEditar[nombreGrupo].push(parseInt(checkB.value))
        checkB.setAttribute("name","idUsuario")
        checkB.checked = true
    }
}
function editandoIntegrantes (nomGrupo, encargado, newNombre){
    console.log(nomGrupo)
    var grupoEditar = {
        idEncargado: document.getElementById(encargado).value,
        idIntegrantes: idIntegranteEditar[nomGrupo],
        anteriorGrupo: nomGrupo,
        nombreGrupo: document.getElementById(newNombre).value
    }
    console.log(grupoEditar)
    var misCabeceras = new Headers({
        "content-type": "application/json"
    })
    const parametros = {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(grupoEditar),
        cache: "no-cache",
        headers: misCabeceras
    }

    fetch('uGrupo', parametros).then( function (response){
                                                manejoFetch(response)
                                        }).catch(function (error) {
                                                    errorInfo(error)
    })
}
function pasandoIntegrantes (){
    var grupo = {
        idEncargado: document.getElementById("idEncargado").value,
        idIntegrantes: idIntegrante,
        nombreGrupo: document.getElementById("nombreGrupo").value 
    }
    var misCabeceras = new Headers({
        "content-type": "application/json"
    })
    const parametros = {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(grupo),
        cache: "no-cache",
        headers: misCabeceras
    }

    fetch('iGrupos', parametros).then( function (response){
                                                manejoFetch(response)
                                        }).catch(function (error) {
                                                    errorInfo(error)
    })
}

function manejoFetch(response){
    if(response.status !== 200){
        alert('Looks like there was a problem. Status code:' + response.status)
        
        return;
    }
    response.json().then(function (data){
        alert(data)
        
    })
}

function errorInfo(error){
    alert("Fetch error: " + error)
}