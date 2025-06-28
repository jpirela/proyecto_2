let modoEliminarActivo = false;

document.getElementById("btnEliminar").addEventListener("click", () => {
  const contenedor = document.getElementById("contenedor-tareas");

  if (!modoEliminarActivo) {
    // Activar modo de selección
    modoEliminarActivo = true;
    document.getElementById("btnEliminar").textContent = "Eliminar seleccionadas";
    
    // Añadir casillas
    document.querySelectorAll(".tareas").forEach(bloque => {
        const id = bloque.getAttribute("data-id");
        const checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        checkbox.classList.add("casilla-tarea");
        checkbox.setAttribute("data-id", id);
        checkbox.style.marginBottom = "6px";
        bloque.prepend(checkbox);
    });
    
    alert("Marca las tareas a eliminar y vuelve a presionar el botón.");
    return;
  }

  // Si ya está activo, eliminar las tareas seleccionadas
  const seleccionadas = document.querySelectorAll(".casilla-tarea:checked");

  if (seleccionadas.length === 0) {
    alert("No seleccionaste ninguna tarea.");
    return;
  }

  const ids = Array.from(seleccionadas).map(cb => cb.dataset.id);
  console.log(ids)
  eliminarTareasPorId(ids);

  // Restaurar estado
  modoEliminarActivo = false;
  document.getElementById("btnEliminar").textContent = "Eliminar tarea";

  // Limpiar checkboxes
  document.querySelectorAll(".casilla-tarea").forEach(cb => cb.remove());
});

function eliminarTareasPorId(ids) {
  ids.forEach(id => {
    axios.delete(`http://localhost:3000/tareas/${id}`)
      .then(() => {
        console.log(`✅ Tarea ${id} eliminada`);
        // Puedes actualizar la vista después de cada eliminación:
        // cargarTareas(localStorage.getItem("usuarioId"));
        window.location.href = "../../index.html";
      })
      .catch(error => {
        console.error(`❌ Error al eliminar la tarea ${id}`, error);
      });
  });
}