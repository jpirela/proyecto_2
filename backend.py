from flask import Flask, request, jsonify, render_template_string
import os
from config import config

class Alumno:
    """Clase que representa un alumno"""
    def __init__(self, nombre, apellido, cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
    
    def to_dict(self):
        """Convierte el objeto alumno a diccionario"""
        return {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'cedula': self.cedula
        }
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} - Cédula: {self.cedula}"

class AlumnoManager:
    """Clase que maneja las operaciones con alumnos"""
    def __init__(self):
        self.alumnos = []
    
    def agregar_alumno(self, nombre, apellido, cedula):
        """Agrega un nuevo alumno al sistema"""
        # Validaciones
        if not nombre or not apellido:
            raise ValueError('Nombre y apellido son obligatorios')
        
        if not isinstance(cedula, int) or cedula <= 0:
            raise ValueError('La cédula debe ser un número entero positivo')
        
        # Verificar si la cédula ya existe
        if any(a.cedula == cedula for a in self.alumnos):
            raise ValueError('Cédula ya registrada. Por favor, usa una cédula única.')
        
        alumno = Alumno(nombre, apellido, cedula)
        self.alumnos.append(alumno)
        return alumno
    
    def obtener_alumnos(self):
        """Retorna la lista de todos los alumnos"""
        return [alumno.to_dict() for alumno in self.alumnos]
    
    def obtener_alumno_por_cedula(self, cedula):
        """Busca un alumno por su cédula"""
        for alumno in self.alumnos:
            if alumno.cedula == cedula:
                return alumno
        return None
    
    def eliminar_alumno(self, cedula):
        """Elimina un alumno por su cédula"""
        alumnos_original_count = len(self.alumnos)
        self.alumnos = [a for a in self.alumnos if a.cedula != cedula]
        return len(self.alumnos) < alumnos_original_count
    
    def obtener_cantidad_alumnos(self):
        """Retorna la cantidad total de alumnos"""
        return len(self.alumnos)

class RegistroAlumnosApp:
    """Clase principal de la aplicación Flask"""
    def __init__(self, config_class=None):
        self.app = Flask(__name__)
        self.config = config_class or config
        self.app.config.from_object(self.config)
        self.alumno_manager = AlumnoManager()
        self.setup_routes()
    
    def setup_routes(self):
        """Configura las rutas de la aplicación"""
        @self.app.route('/')
        def index():
            return render_template_string(self.get_html_template())
        
        @self.app.route('/alumnos', methods=['GET', 'POST'])
        def alumnos_route():
            if request.method == 'POST':
                return self.agregar_alumno()
            else:
                return jsonify(self.alumno_manager.obtener_alumnos())
        
        @self.app.route('/alumnos/<int:cedula>', methods=['DELETE'])
        def eliminar_alumno_route(cedula):
            return self.eliminar_alumno(cedula)
        
        @self.app.route('/alumnos/count', methods=['GET'])
        def contar_alumnos_route():
            return jsonify({'count': self.alumno_manager.obtener_cantidad_alumnos()})
    
    def agregar_alumno(self):
        """Maneja la adición de un nuevo alumno"""
        try:
            data = request.get_json()
            
            if not data:
                return jsonify({'error': 'Datos no proporcionados'}), 400
            
            nombre = data.get('nombre', '').strip()
            apellido = data.get('apellido', '').strip()
            cedula = data.get('cedula')
            
            if not nombre or not apellido:
                return jsonify({'error': 'Nombre y apellido son obligatorios'}), 400
            
            try:
                cedula = int(cedula)
            except (ValueError, TypeError):
                return jsonify({'error': 'La cédula debe ser un número válido'}), 400
            
            self.alumno_manager.agregar_alumno(nombre, apellido, cedula)
            return jsonify({
                'status': 'ok', 
                'message': 'Alumno agregado correctamente',
                'alumno': {'nombre': nombre, 'apellido': apellido, 'cedula': cedula}
            }), 201
            
        except ValueError as e:
            return jsonify({'error': str(e)}), 409
        except Exception as e:
            return jsonify({'error': f'Error interno del servidor: {str(e)}'}), 500
    
    def eliminar_alumno(self, cedula):
        """Maneja la eliminación de un alumno"""
        try:
            if self.alumno_manager.eliminar_alumno(cedula):
                return jsonify({
                    'status': 'ok', 
                    'message': f'Alumno con cédula {cedula} eliminado correctamente'
                })
            else:
                return jsonify({'error': 'Alumno no encontrado'}), 404
        except Exception as e:
            return jsonify({'error': f'Error interno del servidor: {str(e)}'}), 500
    
    def get_html_template(self):
        """Obtiene el template HTML del frontend"""
        try:
            with open('frontend.html', 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return self.get_default_html_template()
    
    def get_default_html_template(self):
        """Template HTML por defecto si no se encuentra el archivo frontend.html"""
        return """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registro de Alumnos</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { font-family: 'Inter', sans-serif; }
        .no-scrollbar::-webkit-scrollbar { display: none; }
        .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
    </style>
</head>
<body class="bg-gradient-to-br from-blue-50 to-indigo-100 min-h-screen flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl shadow-xl p-8 max-w-4xl w-full">
        <h1 class="text-3xl font-bold text-gray-800 mb-6 text-center">Registro de Alumnos</h1>
        <p class="text-center text-gray-600 mb-4">Error: No se pudo cargar la interfaz de usuario</p>
        <p class="text-center text-sm text-gray-500">Asegúrate de que el archivo frontend.html esté presente</p>
    </div>
</body>
</html>
"""
    
    def run(self, debug=None, host=None, port=None):
        """Ejecuta la aplicación Flask"""
        debug = debug if debug is not None else self.config.DEBUG
        host = host or self.config.HOST
        port = port or self.config.PORT
        
        print(f"Iniciando {self.config.APP_NAME} v{self.config.APP_VERSION}")
        print(f"Servidor corriendo en http://{host}:{port}")
        print(f"Modo debug: {'Activado' if debug else 'Desactivado'}")
        
        self.app.run(debug=debug, host=host, port=port)

if __name__ == '__main__':
    try:
        app = RegistroAlumnosApp()
        app.run()
    except ImportError:
        print("Error: Flask no está instalado. Por favor instala Flask con: pip install flask")
        exit(1) 