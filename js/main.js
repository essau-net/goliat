var navbar = {
    inicio = getElementById("#inicio"),
    informacion = getElementById("#info"),
    contacto = getElementById("#contacto")
}

navbar.contacto.addEventListener("mousedown", contacto)

function contacto() {
    window.sr = ScrollReveal()

    sr.reveal('.contacto', {
        duration: 3000,
        diastance: '300px',
        origin: 'bottom'
    })

}