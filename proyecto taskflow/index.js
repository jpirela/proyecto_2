document.addEventListener("DOMContentLoaded", () => {
  const usuarioId = localStorage.getItem("usuarioId")
  if (usuarioId) {
    cargarTareas(usuarioId);
  }
});

async function cargarTareas(usuarioId) {
  try {
    const res = await axios.get(`http://localhost:3000/tareas/usuario/${usuarioId}`);
    const tareas = res.data;

    const contenedor = document.getElementById("contenedor-tareas");
    contenedor.innerHTML = ""; // Limpia tareas anteriores

    tareas.forEach(tarea => {
      const bloque = document.createElement("div");
      bloque.classList.add("tareas");
      bloque.setAttribute("data-id", tarea.id);

      bloque.innerHTML = `
        <div class="escrito">
          <ul class="lista">
            <li class="il">titulo: ${tarea.titulo}</li>
            <li class="il">descripcion: ${tarea.descripcion}</li>
            <li class="il">prioridad: ${tarea.prioridad}</li>
            <li class="il" >estado: ${tarea.estado}</li>
            <li class="il">fecha: ${tarea.fecha_tope}</li>
            <li class="il" style="display: none;">id: ${tarea.id}</li>
          </ul>
        </div>
      `;

      contenedor.appendChild(bloque);
    });

  } catch (error) {
    console.error("Error al cargar tareas:", error);
  }
}
