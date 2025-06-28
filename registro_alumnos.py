try:
    from flask import Flask, request, jsonify, render_template_string
except ImportError:
    print("Error: Flask no está instalado. Por favor instala Flask con: pip install flask")
    exit(1)

app = Flask(__name__)

alumnos = []

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registro de Alumnos</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {
            font-family: 'Inter', sans-serif;
        }
        .no-scrollbar::-webkit-scrollbar {
            display: none;
        }
        .no-scrollbar {
            -ms-overflow-style: none;
            scrollbar-width: none;
        }
    </style>
</head>
<body class="bg-gradient-to-br from-blue-50 to-indigo-100 min-h-screen flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl shadow-xl p-8 max-w-4xl w-full flex flex-col md:flex-row gap-8">
        <div class="flex-1">
            <h1 class="text-3xl font-bold text-gray-800 mb-6 text-center">Registrar Nuevo Alumno</h1>
            <form id="alumnoForm" class="space-y-4">
                <div>
                    <label for="nombre" class="block text-gray-700 text-sm font-semibold mb-2">Nombre:</label>
                    <input type="text" id="nombre" name="nombre" required
                           class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition duration-200 ease-in-out">
                </div>
                <div>
                    <label for="apellido" class="block text-gray-700 text-sm font-semibold mb-2">Apellido:</label>
                    <input type="text" id="apellido" name="apellido" required
                           class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition duration-200 ease-in-out">
                </div>
                <div>
                    <label for="cedula" class="block text-gray-700 text-sm font-semibold mb-2">Cédula:</label>
                    <input type="number" id="cedula" name="cedula" required
                           class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition duration-200 ease-in-out">
                </div>
                <button type="submit"
                        class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-lg shadow-md transition duration-300 ease-in-out transform hover:scale-105">
                    Agregar Alumno
                </button>
            </form>
            <div id="messageContainer" class="mt-4 p-3 rounded-lg text-sm hidden"></div>
        </div>

        <div class="flex-1">
            <h2 class="text-3xl font-bold text-gray-800 mb-6 text-center">Lista de Alumnos</h2>
            <div class="bg-gray-50 rounded-lg p-4 shadow-inner max-h-96 overflow-y-auto no-scrollbar">
                <table class="min-w-full bg-white rounded-lg shadow-md overflow-hidden">
                    <thead class="bg-gray-200 sticky top-0">
                        <tr>
                            <th class="py-3 px-4 text-left text-sm font-semibold text-gray-700">Nombre Completo</th>
                            <th class="py-3 px-4 text-left text-sm font-semibold text-gray-700">Cédula</th>
                            <th class="py-3 px-4 text-center text-sm font-semibold text-gray-700">Acciones</th>
                        </tr>
                    </thead>
                    <tbody id="alumnosTableBody" class="divide-y divide-gray-200">
                    </tbody>
                </table>
                <p id="noAlumnosMessage" class="text-center text-gray-500 mt-4 hidden">No hay alumnos registrados aún.</p>
            </div>
        </div>
    </div>

    <script>
        function showMessage(message, type = 'success') {
            const container = document.getElementById('messageContainer');
            container.textContent = message;
            container.className = 'mt-4 p-3 rounded-lg text-sm';
            if (type === 'success') {
                container.classList.add('bg-green-100', 'text-green-800');
            } else if (type === 'error') {
                container.classList.add('bg-red-100', 'text-red-800');
            }
            container.classList.remove('hidden');
            setTimeout(() => {
                container.classList.add('hidden');
            }, 5000);
        }

        async function cargarAlumnos() {
            try {
                const res = await fetch('/alumnos');
                if (!res.ok) throw new Error('Error al cargar alumnos');
                const data = await res.json();
                const tableBody = document.getElementById('alumnosTableBody');
                tableBody.innerHTML = '';
                const noAlumnosMessage = document.getElementById('noAlumnosMessage');

                if (data.length === 0) {
                    noAlumnosMessage.classList.remove('hidden');
                } else {
                    noAlumnosMessage.classList.add('hidden');
                    data.forEach(alumno => {
                        const row = tableBody.insertRow();
                        row.className = 'hover:bg-gray-50';
                        row.setAttribute('data-cedula', alumno.cedula);

                        const nombreCell = row.insertCell();
                        nombreCell.className = 'py-3 px-4';
                        nombreCell.textContent = `${alumno.nombre} ${alumno.apellido}`;

                        const cedulaCell = row.insertCell();
                        cedulaCell.className = 'py-3 px-4';
                        cedulaCell.textContent = alumno.cedula;

                        const accionesCell = row.insertCell();
                        accionesCell.className = 'py-3 px-4 text-center';
                        const deleteButton = document.createElement('button');
                        deleteButton.textContent = 'Eliminar';
                        deleteButton.className = 'bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded-lg shadow-md transition duration-300 ease-in-out transform hover:scale-105';
                        deleteButton.onclick = () => eliminarAlumno(alumno.cedula);
                        accionesCell.appendChild(deleteButton);
                    });
                }
            } catch (error) {
                console.error('Error al cargar alumnos:', error);
                showMessage('Error al cargar la lista de alumnos.', 'error');
            }
        }

        document.getElementById('alumnoForm').onsubmit = async function(e) {
            e.preventDefault();
            const formData = new FormData(e.target);
            const cedula = parseInt(formData.get('cedula'));

            const currentAlumnosRes = await fetch('/alumnos');
            const currentAlumnos = await currentAlumnosRes.json();
            if (currentAlumnos.some(a => a.cedula === cedula)) {
                showMessage('Ya existe un alumno con esta cédula.', 'error');
                return;
            }

            try {
                const res = await fetch('/alumnos', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        nombre: formData.get('nombre'),
                        apellido: formData.get('apellido'),
                        cedula: cedula
                    })
                });
                if (!res.ok) {
                    const errorData = await res.json();
                    throw new Error(errorData.error || 'Error al agregar alumno');
                }

                e.target.reset();
                await cargarAlumnos();
                showMessage('Alumno agregado correctamente.');
            } catch (error) {
                console.error('Error al agregar alumno:', error);
                showMessage(`Error al agregar el alumno: ${error.message}`, 'error');
            }
        };

        async function eliminarAlumno(cedula) {
            if (!confirm(`¿Estás seguro de que quieres eliminar al alumno con cédula ${cedula}?`)) {
                return;
            }

            try {
                const res = await fetch(`/alumnos/${cedula}`, {
                    method: 'DELETE'
                });
                if (!res.ok) {
                    const errorData = await res.json();
                    throw new Error(errorData.error || 'Error al eliminar alumno');
                }

                await cargarAlumnos();
                showMessage('Alumno eliminado correctamente.');
            } catch (error) {
                console.error('Error al eliminar alumno:', error);
                showMessage(`Error al eliminar el alumno: ${error.message}`, 'error');
            }
        }

        window.onload = cargarAlumnos;
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/alumnos', methods=['GET', 'POST'])
def alumnos_route():
    if request.method == 'POST':
        data = request.get_json()
        nombre = data.get('nombre')
        apellido = data.get('apellido')
        cedula = int(data.get('cedula'))

        if any(a['cedula'] == cedula for a in alumnos):
            return jsonify({'error': 'Cédula ya registrada. Por favor, usa una cédula única.'}), 409

        alumnos.append({
            'nombre': nombre,
            'apellido': apellido,
            'cedula': cedula,
        })
        return jsonify({'status': 'ok', 'message': 'Alumno agregado'}), 201
    else:
        return jsonify(alumnos)

@app.route('/alumnos/<int:cedula>', methods=['DELETE'])
def eliminar_alumno_route(cedula):
    global alumnos
    alumnos_original_count = len(alumnos)
    alumnos = [a for a in alumnos if a['cedula'] != cedula]
    if len(alumnos) < alumnos_original_count:
        return jsonify({'status': 'ok', 'message': 'Alumno eliminado'})
    return jsonify({'error': 'Alumno no encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
