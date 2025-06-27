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

function mostrarModalUsuario() {
    // Evita duplicar el modal
    if (document.getElementById('modalUsuario')) return;

    // Fondo del modal
    const modalBg = document.createElement('div');
    modalBg.id = 'modalUsuario';
    modalBg.style.position = 'fixed';
    modalBg.style.top = '0';
    modalBg.style.left = '0';
    modalBg.style.width = '100vw';
    modalBg.style.height = '100vh';
    modalBg.style.boxShadow = '0 0 10px 1px #000';
    modalBg.style.background = 'rgba(0,0,0,0.4)';
    modalBg.style.display = 'flex';
    modalBg.style.alignItems = 'center';
    modalBg.style.justifyContent = 'center';
    modalBg.style.zIndex = '1000';

    // Contenido del modal
    const modalContent = document.createElement('div');
    modalContent.style.background = '#242424';
    modalContent.style.padding = '30px 40px';
    modalContent.style.borderRadius = '12px';
    modalContent.style.boxShadow = '0 2px 10px rgba(0,0,0,0.3)';
    modalContent.style.display = 'flex';
    modalContent.style.flexDirection = 'column';
    modalContent.style.alignItems = 'center';

    // Título
    const titulo = document.createElement('h2');
    titulo.textContent = 'TodoList App';
    titulo.style.color = '#fff';
    titulo.style.background = 'transparent';
    titulo.style.marginBottom = '20px';
    modalContent.appendChild(titulo);

    // Botón Iniciar Sesión
    const btnLogin = document.createElement('button');
    btnLogin.textContent = 'Iniciar sesión';
    btnLogin.style.color = '#fff';
    btnLogin.style.borderColor = '#fff';
    btnLogin.style.borderRadius = '8px';
    btnLogin.style.borderStyle = 'solid';
    btnLogin.style.margin = '10px';
    btnLogin.style.padding = '10px 20px';
    btnLogin.style.fontSize = '16px';
    btnLogin.onclick = function() {
        btnLogin.style.borderColor = '#000';
        setTimeout(() => {
            document.body.removeChild(modalBg);
            mostrarModalLogin(); // Mostrar el modal de login
        }, 100);
    };
    modalContent.appendChild(btnLogin);

    // Botón Registrar
    const btnRegister = document.createElement('button');
    btnRegister.textContent = 'Registrar usuario';
    btnRegister.style.color = '#fff';
    btnRegister.style.borderColor = '#fff';
    btnRegister.style.borderRadius = '8px';
    btnRegister.style.borderStyle = 'solid';
    btnRegister.style.margin = '10px';
    btnRegister.style.padding = '10px 20px';
    btnRegister.style.fontSize = '16px';
    btnRegister.onclick = function() {
        btnRegister.style.borderColor = '#000';
        setTimeout(() => {
            document.body.removeChild(modalBg);
            mostrarModalRegistro(); // Mostrar el modal de registro
        }, 100);
    };
    modalContent.appendChild(btnRegister);

    // Botón cerrar
    const btnCerrar = document.createElement('button');
    btnCerrar.textContent = 'Cerrar';
    btnCerrar.style.color = '#fff';
    btnCerrar.style.borderColor = '#fff';
    btnCerrar.style.borderRadius = '8px';
    btnCerrar.style.borderStyle = 'solid';
    btnCerrar.style.marginTop = '20px';
    btnCerrar.style.padding = '6px 16px';
    btnCerrar.onclick = function() {
        btnCerrar.style.borderColor = '#000'; // Cambia el borde a negro al hacer click
        setTimeout(() => {
            document.body.removeChild(modalBg);
        }, 100);
    };
    modalContent.appendChild(btnCerrar);

    modalBg.appendChild(modalContent);
    document.body.appendChild(modalBg);
}

// Nueva función para mostrar el modal de registro
function mostrarModalRegistro() {
    // Evita duplicar el modal
    if (document.getElementById('modalRegistro')) return;

    // Fondo del modal
    const modalBg = document.createElement('div');
    modalBg.id = 'modalRegistro';
    modalBg.style.position = 'fixed';
    modalBg.style.top = '0';
    modalBg.style.left = '0';
    modalBg.style.width = '100vw';
    modalBg.style.height = '100vh';
    modalBg.style.background = 'rgba(0,0,0,0.5)';
    modalBg.style.display = 'flex';
    modalBg.style.alignItems = 'center';
    modalBg.style.justifyContent = 'center';
    modalBg.style.zIndex = '1000';

    // Contenido del modal
    const modalContent = document.createElement('div');
    modalContent.style.background = '#242424';
    modalContent.style.padding = '30px 40px';
    modalContent.style.borderRadius = '12px';
    modalContent.style.boxShadow = '0 2px 10px rgba(0,0,0,0.3)';
    modalContent.style.display = 'flex';
    modalContent.style.flexDirection = 'column';
    modalContent.style.alignItems = 'center';

    // Título
    const titulo = document.createElement('h2');
    titulo.textContent = 'Registro de usuario';
    titulo.style.color = '#fff';
    titulo.style.background = 'transparent';
    titulo.style.marginBottom = '20px';
    modalContent.appendChild(titulo);

    // Campos de registro
    const campos = [
        { label: 'Nombre', type: 'text', id: 'nombre' },
        { label: 'Apellido', type: 'text', id: 'apellido' },
        { label: 'Usuario', type: 'text', id: 'usuario' },
        { label: 'Contraseña', type: 'password', id: 'contrasena' }
    ];

    campos.forEach(campo => {
        const label = document.createElement('label');
        label.textContent = campo.label;
        label.style.backgroundColor = 'transparent';
        label.style.color = '#fff';
        label.style.marginTop = '10px';
        label.style.display = 'block';
        label.setAttribute('for', campo.id);

        const input = document.createElement('input');
        input.type = campo.type;
        input.id = campo.id;
        input.style.color = '#fff';
        input.style.margin = '5px 0 15px 0';
        input.style.padding = '8px';
        input.style.borderRadius = '6px';
        input.style.border = '1px solid #ccc';
        input.style.width = '200px';

        modalContent.appendChild(label);
        modalContent.appendChild(input);
    });

    // Botón Registrar
    const btnRegistrar = document.createElement('button');
    btnRegistrar.textContent = 'Registrar';
    btnRegistrar.style.color = '#fff';
    btnRegistrar.style.background = '#007bff';
    btnRegistrar.style.border = 'none';
    btnRegistrar.style.borderRadius = '8px';
    btnRegistrar.style.margin = '10px';
    btnRegistrar.style.padding = '10px 20px';
    btnRegistrar.style.fontSize = '16px';
    btnRegistrar.onclick = function() {
        // Aquí puedes manejar el registro
        alert('Usuario registrado');
        document.body.removeChild(modalBg);
    };
    modalContent.appendChild(btnRegistrar);

    // Botón cerrar
    const btnCerrar = document.createElement('button');
    btnCerrar.textContent = 'Cerrar';
    btnCerrar.style.color = '#fff';
    btnCerrar.style.background = '#dc3545';
    btnCerrar.style.border = 'none';
    btnCerrar.style.borderRadius = '8px';
    btnCerrar.style.marginTop = '10px';
    btnCerrar.style.padding = '6px 16px';
    btnCerrar.onclick = function() {
        document.body.removeChild(modalBg);
    };
    modalContent.appendChild(btnCerrar);

    modalBg.appendChild(modalContent);
    document.body.appendChild(modalBg);
}

// Nueva función para mostrar el modal de inicio de sesión
function mostrarModalLogin() {
    // Evita duplicar el modal
    if (document.getElementById('modalLogin')) return;

    // Fondo del modal
    const modalBg = document.createElement('div');
    modalBg.id = 'modalLogin';
    modalBg.style.position = 'fixed';
    modalBg.style.top = '0';
    modalBg.style.left = '0';
    modalBg.style.width = '100vw';
    modalBg.style.height = '100vh';
    modalBg.style.background = 'rgba(0,0,0,0.5)';
    modalBg.style.display = 'flex';
    modalBg.style.alignItems = 'center';
    modalBg.style.justifyContent = 'center';
    modalBg.style.zIndex = '1000';

    // Contenido del modal
    const modalContent = document.createElement('div');
    modalContent.style.background = '#242424';
    modalContent.style.padding = '30px 40px';
    modalContent.style.borderRadius = '12px';
    modalContent.style.boxShadow = '0 2px 10px rgba(0,0,0,0.3)';
    modalContent.style.display = 'flex';
    modalContent.style.flexDirection = 'column';
    modalContent.style.alignItems = 'center';

    // Título
    const titulo = document.createElement('h2');
    titulo.textContent = 'Iniciar sesión';
    titulo.style.color = '#fff';
    titulo.style.background = 'transparent';
    titulo.style.marginBottom = '20px';
    modalContent.appendChild(titulo);

    // Campos de login
    const campos = [
        { label: 'Usuario', type: 'text', id: 'usuarioLogin' },
        { label: 'Contraseña', type: 'password', id: 'contrasenaLogin' }
    ];

    campos.forEach(campo => {
        const label = document.createElement('label');
        label.textContent = campo.label;
        label.style.backgroundColor = 'transparent';
        label.style.color = '#fff';
        label.style.marginTop = '10px';
        label.style.display = 'block';
        label.setAttribute('for', campo.id);

        const input = document.createElement('input');
        input.type = campo.type;
        input.id = campo.id;
        input.style.color = '#fff';
        input.style.margin = '5px 0 15px 0';
        input.style.padding = '8px';
        input.style.borderRadius = '6px';
        input.style.border = '1px solid #ccc';
        input.style.width = '200px';

        modalContent.appendChild(label);
        modalContent.appendChild(input);
    });

    // Botón Iniciar sesión
    const btnIniciar = document.createElement('button');
    btnIniciar.textContent = 'Iniciar sesión';
    btnIniciar.style.color = '#fff';
    btnIniciar.style.background = '#007bff';
    btnIniciar.style.border = 'none';
    btnIniciar.style.borderRadius = '8px';
    btnIniciar.style.margin = '10px';
    btnIniciar.style.padding = '10px 20px';
    btnIniciar.style.fontSize = '16px';
    btnIniciar.onclick = function() {
        // Aquí puedes manejar el inicio de sesión
        alert('Sesión iniciada');
        document.body.removeChild(modalBg);
    };
    modalContent.appendChild(btnIniciar);

    // Botón cerrar
    const btnCerrar = document.createElement('button');
    btnCerrar.textContent = 'Cerrar';
    btnCerrar.style.color = '#fff';
    btnCerrar.style.background = '#dc3545';
    btnCerrar.style.border = 'none';
    btnCerrar.style.borderRadius = '8px';
    btnCerrar.style.marginTop = '10px';
    btnCerrar.style.padding = '6px 16px';
    btnCerrar.onclick = function() {
        document.body.removeChild(modalBg);
    };
    modalContent.appendChild(btnCerrar);

    modalBg.appendChild(modalContent);
    document.body.appendChild(modalBg);
}

function acountClick() {
    const userImage = document.getElementById('userImage');
    if (userImage) {
        userImage.addEventListener('click', mostrarModalUsuario);
    }
}

document.addEventListener('DOMContentLoaded', function () {
    acountClick();
});

// Eliminar tarea y los hr exteriores usando delegación de eventos
document.querySelector('.todoContainer').addEventListener('click', function (e) {
    if (e.target && e.target.id === 'deleteTask') {
        eliminarTareaYHrs(e.target);
    }
});