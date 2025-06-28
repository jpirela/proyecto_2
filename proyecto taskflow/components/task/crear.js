// Ejecutar directamente cuando se carga
const btn = document.getElementById("btnGuardar");
if (btn) {
  btn.addEventListener("click", guardarTarea);
  console.log("🟢 Script de crear activo");
} else {
  console.warn("Botón 'Guardar' no encontrado");
}


async function guardarTarea() {
  const nuevaTarea = {
    titulo: document.getElementById("titulo").value,
    descripcion: document.getElementById("descripcion").value,
    prioridad: parseInt(document.getElementById("prioridad").value),
    fecha_tope: document.getElementById("fecha").value,
    
    estado:document.getElementById("estado").value,
    usuario_id: localStorage.getItem("usuarioId")
  };
  comentario= document.getElementById("comentarios").value,
  console.log(nuevaTarea)

  try {
    
  await axios.post("http://localhost:3000/tareas", nuevaTarea);
    
    
    /*
    const id= respuesta.data;
    const nuevocomentario={
        contenido: comentario,
        tarea_id: id.id,
        usuario_id:localStorage.getItem("usuarioId")
    };
    */


    alert("Tarea guardada exitosamente.");
    window.location.href = "../../index.html";
  } catch (error) {
    console.error("Error al guardar tarea:", error);
    alert("No se pudo guardar la tarea.");
  }
}
