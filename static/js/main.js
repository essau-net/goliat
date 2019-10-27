window.addEventListener("load",loadPagina)

function loadPagina(){
    var asideMenu = {
        home: document.getElementById("homeM"),
        perfil: document.getElementById("perfilM"),
        actividades: document.getElementById("actividadesM")
    }
    asideMenu.home.addEventListener("click", cambioMenu)
}
function cambioMenu (event){
    console.log(event)
}
function probando(){
    alert("Fuck yeaH it works")
}

/*;
var home = document.getElementById("homeM")

console.log(asideMenu.home)
console.log(home)
//asideMenu.home.addEventListener("click", probando)



asideMenu.home.addEventListener("click", cambioPagina(asideMenu.home))
 var cambioPagina = function (eleccion){
     return function cambioColor(event){
         if(asideMenu.home == eleccion){

         }else
        asideMenu.home.classList.remove("active")
        asideMenu.perfil.classList.remove("active")
        asideMenu.perfil.classList.remove("active")
        eleccion.classList.add("active")
     }
 }*/
