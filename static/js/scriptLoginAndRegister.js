let login=document.getElementById("container-login")
let registro=document.getElementById("container-registro")
let boton=document.getElementById("button")
let volver=document.getElementById("volver")

boton.addEventListener('click', () => {
    login.classList.add("ver")
    registro.classList.add("aparecer")
               })
               volver.addEventListener('click', () => {
                login.classList.remove("ver")
                registro.classList.remove("aparecer")
                           })

    

