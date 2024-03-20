const alertaDesplegar=document.getElementById("main")
const botonDeDesplegue=document.getElementById("abrir-crud")
const botonDeCierre=document.getElementById("cerrar-crud")
botonDeDesplegue.addEventListener('click', () => {
    alertaDesplegar.classList.add("ver")
    botonDeDesplegue.classList.add("desvanecer")
       })
botonDeCierre.addEventListener('click', () => {
alertaDesplegar.classList.remove("ver")
botonDeDesplegue.classList.remove("desvanecer")   
           })

           const botonDerSimple = document.getElementById("simply-right")
           const deslizador=document.getElementById("tabla")
           const botonIzqSimple = document.getElementById("izquierda")
           
           botonDerSimple.addEventListener('click', () => {
             const porcentajeDesplazamiento = 100;
             const desplazamiento = deslizador.offsetWidth * (porcentajeDesplazamiento / 100);
              deslizador.scrollLeft+=desplazamiento;
           })
           
           
           botonIzqSimple.addEventListener('click', () => {
             const porcentajeDesplazamiento = 100;
             const desplazamiento = deslizador.offsetWidth * (porcentajeDesplazamiento / 100);
               deslizador.scrollLeft-=desplazamiento;
                })


                var deleteButtons = document.getElementsByClassName('delete-button');
                const launcAlert=document.getElementById("alertitaz");
                const closeButton=document.getElementById("close");
              
                for (var i = 0; i < deleteButtons.length; i++) {
                  deleteButtons[i].addEventListener('click', function(e) {
                    e.preventDefault(); // Prevenir el comportamiento predeterminado del enlace
                    var id = this.getAttribute('data-id'); // Obtener la ID almacenada en data-id
                
                    // Mostrar una alerta con la ID correspondiente
                    launcAlert.classList.add("launch")
                    var lil=document.getElementById("inp");
                    lil.value = id;
                  });
                }
                closeButton.addEventListener('click', function(){
                    launcAlert.classList.remove("launch");
                })
                         
           
