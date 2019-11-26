function seleccionado(idCheckbox){
    var checkBox = document.getElementById(idCheckbox)
    if (checkBox.checked){
        console.log("UnChecked")
        checkBox.removeAttribute("name")
        checkBox.checked = false
    } else{
        console.log("Checked")
        checkBox.setAttribute("name","idUsuario")
        checkBox.checked = true
    }
}