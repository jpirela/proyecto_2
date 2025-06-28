const id = localStorage.getItem("tareaIdAModificar");

if (id) {
  axios.get(`http://localhost:3000/tareas/${id}`)
    .then(res => {
      const tarea = res.data;
      // Llena los campos con los datos de la tarea
      document.getElementById("titulo").value = tarea.titulo;
      document.getElementById("descripcion").value = tarea.descripcion;
      document.getElementById("prioridad").value = tarea.prioridad;
      document.getElementById("estado").value = tarea.estado;
      document.getElementById("fecha").value = tarea.fecha_tope;
      document.getElementById("comentarios").value = tarea.comentario;
      // Puedes guardar el ID oculto también si lo necesitas al momento de hacer el PUT

    })
    .catch(err => {
      console.error("Error al cargar tarea para modificar:", err);
    });
}

const btn = document.getElementById("btnGuardar");
if (btn) {
  btn.addEventListener("click", guardarTarea);
} else {
  console.warn(" Botón 'Guardar' no encontrado");
}


async function guardarTarea() {
  const nuevaTarea = {
    titulo: document.getElementById("titulo").value,
    descripcion: document.getElementById("descripcion").value,
    prioridad: parseInt(document.getElementById("prioridad").value),
    fecha_tope: document.getElementById("fecha").value,
    
    estado:document.getElementById("estado").value,
    usuario_id: parseInt(localStorage.getItem("usuarioId"))
  };
  comentario= document.getElementById("comentarios").value,
  console.log(nuevaTarea)

  try {
    const tareaId = id; // o cualquier ID que tengas
    await axios.put(`http://localhost:3000/tareas/${tareaId}`, nuevaTarea);
    /*
    const id= respuesta.data;
    const nuevocomentario={
        contenido: comentario,
        tarea_id: id.id,
        usuario_id:localStorage.getItem("usuarioId")
    };
    */


    alert("Tarea modificada exitosamente.");
    window.location.href = "../../index.html";
  } catch (error) {
    console.error("Error al guardar tarea:", error);
    alert("No se pudo guardar la tarea.");
  }
}
