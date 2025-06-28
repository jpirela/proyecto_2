// Mostrar y ocultar el modal
function mostrarModal() {
  document.getElementById("modal").style.display = "block";
}

function mostrarModalR() {
  cerrarModal();
  document.getElementById("modal-registro").style.display = "block";
}

function cerrarModal() {
  document.getElementById("modal").style.display = "none";
}
function cerrarModalR() {
  document.getElementById("modal-registro").style.display = "none";
}


// Iniciar sesión
async function Iniciarsesion() {
  const usuarioIngresado = document.getElementById("Usuario").value;
  const contrasenaIngresada = document.getElementById("Contrasena").value;

  try {
    const respuesta = await axios.get('http://localhost:3000/usuarios');
    const usuarios = respuesta.data;

    const usuarioEncontrado = usuarios.find(user =>
      user.nombre === usuarioIngresado && user.contrasena === contrasenaIngresada
    );

    if (usuarioEncontrado) {
      alert(`Inicio de sesión exitoso. ¡Bienvenido, ${usuarioEncontrado.nombre}!`);

      // Limpiar campos del modal
      document.getElementById("Usuario").value = "";
      document.getElementById("Contrasena").value = "";

      // Guardar datos en localStorage
      localStorage.setItem("usuarioId", usuarioEncontrado.id);
      localStorage.setItem("usuarioNombre", usuarioEncontrado.nombre);

      // Cargar tareas y cerrar modal
      cargarTareas(usuarioEncontrado.id);
      cerrarModal();

      // Actualizar el botón de sesión
      actualizarBotonSesion(usuarioEncontrado.nombre);
    } else {
      alert("Usuario o contraseña incorrectos.");
    }

  } catch (error) {
    console.error("Error al validar credenciales:", error);
    alert("Ocurrió un error al conectarse con el servidor.");
  }
}

// Cerrar sesión
function cerrarSesion() {
  localStorage.removeItem("usuarioId");
  localStorage.removeItem("usuarioNombre");

  const contenedor = document.getElementById("contenedor-tareas");
  if (contenedor) contenedor.innerHTML = "";

  const boton = document.getElementById("botonLogin");
  if (boton) {
    boton.textContent = "Iniciar sesión";
    boton.onclick = mostrarModal;
  }

  alert("Sesión cerrada correctamente.");
}

// Cambiar el botón según estado
function actualizarBotonSesion() {
  const boton = document.getElementById("botonLogin");
  if (boton) {
    boton.textContent = `Cerrar sesión `;
    boton.onclick = cerrarSesion;
  }
}

// Cargar al entrar a la página
document.addEventListener("DOMContentLoaded", () => {
  const id = localStorage.getItem("usuarioId");
  const nombre = localStorage.getItem("usuarioNombre");

  if (id ) {
    cargarTareas(id);
    actualizarBotonSesion();
  }
});

function abrirFormularioNuevaTarea() {
  const id = localStorage.getItem("usuarioId");
   if (id ) {
    window.location.href = "../components/task/task.html?modo=crear";

   }else{
    alert("inicie sesion para crear tareas")
   }
}


async function guardarUsuario() {
  const nuevoUsuario = {
    nombre: document.getElementById("nombre").value,
    contrasena: document.getElementById("ContrasenaR").value,
    ci: parseInt(document.getElementById("ci").value),
    email: document.getElementById("email").value
    
  };


  try {
    
  await axios.post("http://localhost:3000/usuarios", nuevoUsuario);
   alert("usuario guardado exitosamente.");
   cerrarModalR();
  } catch (error) {
    console.error("Error al guardar usuario:", error);
    alert("No se pudo guardar elusuario");
  }
}
