let modoModificarActivo = false;

document.getElementById("btnModificar").addEventListener("click", () => {
  if (!modoModificarActivo) {
    modoModificarActivo = true;
    document.getElementById("btnModificar").textContent = "Modificar tarea seleccionada";

    document.querySelectorAll(".tareas").forEach(bloque => {
      const id = bloque.getAttribute("data-id");
      const checkbox = document.createElement("input");
      checkbox.type = "checkbox";
      checkbox.classList.add("casilla-tarea");
      checkbox.setAttribute("data-id", id);
      checkbox.style.marginBottom = "6px";
      bloque.prepend(checkbox);
    });

    alert("Selecciona UNA tarea a modificar y vuelve a presionar el botón.");
    return;
  }

  const seleccionadas = document.querySelectorAll(".casilla-tarea:checked");

  if (seleccionadas.length === 0) {
    alert("No seleccionaste ninguna tarea.");
    return;
  }

  if (seleccionadas.length > 1) {
    alert("Solo puedes modificar una tarea a la vez.");
    return;
  }

  const id = seleccionadas[0].dataset.id;

  // Guardar ID en localStorage para recuperarlo en tasklet.html
  localStorage.setItem("tareaIdAModificar", id);

  // Ir a la pantalla de modificación
  window.location.href = "components/task/task.html?modo=modificar";

  // Reset visual
  modoModificarActivo = false;
  document.getElementById("btnModifciar").textContent = "Modificar ";
  document.querySelectorAll(".casilla-tarea").forEach(cb => cb.remove());
});
