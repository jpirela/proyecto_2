// Función para hacer editable el nombre de una pestaña
function hacerEditableTab(tabElement) {
    tabElement.addEventListener('dblclick', function () {
        this.setAttribute('contenteditable', 'true');
        this.focus();
        // Seleccionar todo el texto
        const range = document.createRange();
        range.selectNodeContents(this);
        const sel = window.getSelection();
        sel.removeAllRanges();
        sel.addRange(range);
    });
    tabElement.addEventListener('blur', function () {
        this.removeAttribute('contenteditable');
    });
}

// Función para hacer editable el nombre de una tarea
function hacerEditableTask(taskElement) {
    taskElement.addEventListener('dblclick', function () {
        this.setAttribute('contenteditable', 'true');
        this.focus();
        // Seleccionar todo el texto
        const range = document.createRange();
        range.selectNodeContents(this);
        const sel = window.getSelection();
        sel.removeAllRanges();
        sel.addRange(range);
    });
    taskElement.addEventListener('blur', function () {
        this.removeAttribute('contenteditable');
    });
}

// Función para eliminar tarea y sus hr exteriores
function eliminarTareaYHrs(elemento) {
    const taskDiv = elemento.closest('.task');
    if (taskDiv) {
        const prev = taskDiv.previousElementSibling;
        const next = taskDiv.nextElementSibling;
        if (prev && prev.tagName === 'HR') {
            prev.remove();
        }
        taskDiv.remove();
    }
}

// Inicializar eventos para pestañas existentes
document.querySelectorAll('.tab p').forEach(hacerEditableTab);

// Inicializar eventos para tareas existentes
document.querySelectorAll('.task p').forEach(hacerEditableTask);

// Añadir nueva tarea
function agregarNuevaTarea() {
    const taskDiv = document.createElement('div');
    taskDiv.className = 'task';
    taskDiv.innerHTML = `
        <input type="checkbox" name="taskCheck">
        <p>Doble click para asignar nombre</p>
        <div id="taskButtons">
            <img id="checkTask" src="../public/assets/images/check.png" alt="">
            <hr>
            <img id="deleteTask" src="../public/assets/images/trash.png" alt="">
        </div>
    `;

    // Crear el <hr> que irá después de la tarea
    const hr = document.createElement('hr');

    // Insertar antes de #addTask
    const addTaskDiv = document.getElementById('addTask');
    addTaskDiv.parentNode.insertBefore(taskDiv, addTaskDiv);
    addTaskDiv.parentNode.insertBefore(hr, addTaskDiv);

    // Hacer el nombre editable al hacer doble clic
    const taskName = taskDiv.querySelector('p');
    hacerEditableTask(taskName);
}

document.querySelector('#addTask img').addEventListener('click', agregarNuevaTarea);

// Función para agregar una nueva pestaña
function agregarNuevaPestana() {
    const tabDiv = document.createElement('div');
    tabDiv.className = 'tab';
    tabDiv.innerHTML = `
        <p>nueva</p>
        <img class="close-icon" src="../public/assets/images/close.png" alt="">
    `;

    // Insertar antes de .addTab
    const addTabDiv = document.querySelector('.addTab');
    addTabDiv.parentNode.insertBefore(tabDiv, addTabDiv);

    // Hacer el nombre editable al hacer doble clic
    const tabName = tabDiv.querySelector('p');
    hacerEditableTab(tabName);
}

// Asignar evento al botón de agregar pestaña
document.querySelector('.addTab img').addEventListener('click', agregarNuevaPestana);

// Función para eliminar una pestaña
function eliminarPestana(elemento) {
    const tabDiv = elemento.closest('.tab');
    if (tabDiv) {
        tabDiv.remove();
    }
}

// Delegación de eventos para eliminar pestañas
document.querySelector('#TabHeader').addEventListener('click', function (e) {
    if (e.target && e.target.classList.contains('close-icon')) {
        eliminarPestana(e.target);
    }
});

// Eliminar tarea y los hr exteriores usando delegación de eventos
document.querySelector('.todoContainer').addEventListener('click', function (e) {
    if (e.target && e.target.id === 'deleteTask') {
        eliminarTareaYHrs(e.target);
    }
});