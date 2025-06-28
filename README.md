# Registro de Alumnos

Una aplicación web moderna para gestionar el registro de alumnos con una interfaz de usuario intuitiva y un backend robusto.

## 🏗️ Estructura del Proyecto

```
registro_alumnos/
├── backend.py          # Lógica del servidor y clases del backend
├── frontend.html       # Interfaz de usuario (HTML, CSS, JavaScript)
├── config.py           # Configuraciones de la aplicación
├── main.py             # Punto de entrada principal
├── requirements.txt    # Dependencias del proyecto
└── README.md          # Este archivo
```

## 🚀 Características

- **Arquitectura Separada**: Frontend y backend completamente separados
- **Interfaz Moderna**: Diseño responsive con Tailwind CSS
- **Validaciones Robustas**: Validación de datos en el backend
- **Manejo de Errores**: Gestión completa de errores y mensajes al usuario
- **Configuración Flexible**: Sistema de configuración para diferentes entornos

## 📋 Requisitos

- Python 3.7 o superior
- Flask

## 🛠️ Instalación

1. **Clona o descarga el proyecto**
2. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Uso

### Opción 1: Usar el punto de entrada principal
```bash
python main.py
```

### Opción 2: Ejecutar directamente el backend
```bash
python backend.py
```

### Opción 3: Usar Flask directamente
```bash
export FLASK_APP=backend.py
export FLASK_ENV=development
flask run
```

## 🌐 Acceso

Una vez iniciada la aplicación, accede a:
- **URL**: http://127.0.0.1:5000
- **Puerto por defecto**: 5000

## 📁 Estructura de Clases

### Backend (`backend.py`)

#### `Alumno`
- Representa un alumno individual
- Métodos: `to_dict()`, `__str__()`

#### `AlumnoManager`
- Gestiona todas las operaciones con alumnos
- Métodos: `agregar_alumno()`, `obtener_alumnos()`, `eliminar_alumno()`, etc.

#### `RegistroAlumnosApp`
- Clase principal de la aplicación Flask
- Maneja rutas y configuración del servidor

### Frontend (`frontend.html`)

#### `AlumnoUI`
- Clase JavaScript que maneja toda la lógica del frontend
- Métodos: `cargarAlumnos()`, `handleFormSubmit()`, `eliminarAlumno()`, etc.

## 🔧 Configuración

El archivo `config.py` contiene las configuraciones de la aplicación:

- **DevelopmentConfig**: Para desarrollo (debug activado)
- **ProductionConfig**: Para producción (debug desactivado)

### Personalizar Configuración

```python
# En config.py
class CustomConfig(Config):
    HOST = '0.0.0.0'
    PORT = 8080
    DEBUG = False
```

## 📡 API Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/` | Página principal con interfaz de usuario |
| GET | `/alumnos` | Obtener lista de todos los alumnos |
| POST | `/alumnos` | Agregar un nuevo alumno |
| DELETE | `/alumnos/<cedula>` | Eliminar alumno por cédula |
| GET | `/alumnos/count` | Obtener cantidad total de alumnos |

## 🔒 Validaciones

### Backend
- Nombre y apellido obligatorios
- Cédula debe ser un número entero positivo
- Cédula única (no duplicados)
- Sanitización de datos de entrada

### Frontend
- Validación de formularios en tiempo real
- Verificación de cédulas duplicadas antes del envío
- Confirmación antes de eliminar

## 🎨 Interfaz de Usuario

- **Diseño Responsive**: Se adapta a diferentes tamaños de pantalla
- **Animaciones**: Transiciones suaves y efectos hover
- **Mensajes de Estado**: Notificaciones de éxito y error
- **Tabla Interactiva**: Lista de alumnos con acciones

## 🚨 Manejo de Errores

- **Errores de Validación**: Mensajes claros para datos inválidos
- **Errores de Servidor**: Respuestas HTTP apropiadas
- **Errores de Red**: Manejo de fallos de conexión
- **Logging**: Registro de errores para debugging

## 🔄 Flujo de Datos

1. **Frontend** envía datos al **Backend** via API REST
2. **Backend** valida y procesa los datos
3. **Backend** responde con estado y mensajes
4. **Frontend** actualiza la interfaz según la respuesta

## 🧪 Próximas Mejoras

- [ ] Persistencia de datos (base de datos)
- [ ] Autenticación de usuarios
- [ ] Exportación de datos (PDF, Excel)
- [ ] Búsqueda y filtros
- [ ] Paginación para grandes volúmenes
- [ ] Tests unitarios y de integración

## 📝 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o pull request para sugerir mejoras. 