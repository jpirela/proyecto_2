# User Management System Backend v2.0

A stable, modern backend for user and application management with a beautiful admin interface.

## 🚀 Features

- **User Management**: Create, edit, delete users with admin/regular roles
- **App Management**: Register and manage applications with permissions
- **Beautiful Admin Interface**: Modern web interface with Bootstrap 5
- **JWT Authentication**: Secure token-based authentication
- **Permission System**: Granular app access control
- **Pre-configured Apps**: Notebook (available) and MediaPlayer (blocked)
- **RESTful API**: Complete API with interactive documentation

## 📋 Requirements

- Python 3.8+
- pip (Python package manager)

## 🛠️ Installation

1. **Navigate to the backend directory:**
   ```bash
   cd backend
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the server:**
   ```bash
   python start_server.py
   ```

   Or alternatively:
   ```bash
   python main.py
   ```

## 🔑 Default Credentials

- **Username**: `admin`
- **Password**: `admin123`

## 🌐 Access Points

- **Admin Interface**: http://localhost:8000/admin
- **API Documentation**: http://localhost:8000/docs
- **API Root**: http://localhost:8000/

## 📊 Admin Interface Features

### Dashboard
- System statistics and overview
- Quick action buttons
- Recent user activity
- System status monitoring

### User Management
- View all users with roles
- Add new users (admin/regular)
- Edit user passwords and privileges
- Delete users (with confirmation)

### App Management
- View all registered applications
- Add new applications with categories
- Edit app details and blocking status
- Manage user permissions per app
- Delete applications

## 🔧 API Endpoints

### Authentication
- `POST /api/token` - Login and get JWT token
- `GET /api/me` - Get current user info

### User Management
- `GET /api/users` - List all users (admin only)
- `POST /api/users` - Create new user (admin only)
- `GET /api/users/{username}` - Get user details (admin only)
- `PUT /api/users/{username}` - Update user (admin only)
- `DELETE /api/users/{username}` - Delete user (admin only)

### App Management
- `GET /api/apps` - List apps (filtered by permissions)
- `POST /api/apps` - Create new app (admin only)
- `GET /api/apps/{app_id}` - Get app details
- `PUT /api/apps/{app_id}` - Update app (admin only)
- `DELETE /api/apps/{app_id}` - Delete app (admin only)
- `POST /api/apps/{app_id}/run` - Run application

### Permissions
- `GET /api/apps/{app_id}/permissions` - Get app permissions (admin only)
- `POST /api/apps/{app_id}/permissions/{username}` - Grant permission (admin only)
- `DELETE /api/apps/{app_id}/permissions/{username}` - Revoke permission (admin only)

## 🗄️ Database

The system uses SQLite for data storage. The database file (`app.db`) is automatically created on first run with:

- Default admin user
- Pre-configured apps (Notebook, MediaPlayer)
- Proper table structure

## 🔒 Security Features

- **JWT Authentication**: Secure token-based sessions
- **Password Hashing**: bcrypt password encryption
- **Role-based Access**: Admin and regular user roles
- **Permission System**: Granular app access control
- **Input Validation**: Pydantic model validation

## 🎨 UI Features

- **Modern Design**: Bootstrap 5 with custom styling
- **Responsive Layout**: Works on desktop and mobile
- **Interactive Elements**: Modals, alerts, and dynamic content
- **Real-time Updates**: Live statistics and data refresh
- **User-friendly**: Intuitive navigation and clear actions

## 📱 Pre-configured Apps

### Notebook
- **Category**: Productivity
- **Path**: `notepad.exe`
- **Status**: Available to all users
- **Description**: Simple text editor

### MediaPlayer
- **Category**: Media
- **Path**: `wmplayer.exe`
- **Status**: Blocked by default
- **Description**: Video and audio player

## 🚨 Troubleshooting

### Common Issues

1. **Port already in use**
   - Change port in `main.py` or `start_server.py`
   - Kill existing processes on port 8000

2. **Database errors**
   - Delete `app.db` file to reset
   - Restart the server

3. **Template not found**
   - Ensure `templates/` directory exists
   - Check file permissions

4. **Import errors**
   - Install requirements: `pip install -r requirements.txt`
   - Check Python version (3.8+)

### Logs

The server provides detailed logs for debugging. Check the console output for:
- Server startup messages
- Database initialization
- API request logs
- Error messages

## 🔄 Development

### Adding New Features

1. **New API Endpoints**: Add to `main.py`
2. **New Templates**: Add to `templates/` directory
3. **New Static Files**: Add to `static/` directory
4. **Database Changes**: Modify `init_database()` function

### Testing

- Use the interactive API docs at `/docs`
- Test admin interface at `/admin`
- Check API responses with tools like Postman

## 📄 License

This project is part of the User Management System v2.0.

## 🤝 Support

For issues or questions:
1. Check the troubleshooting section
2. Review the API documentation
3. Check server logs for errors

---

# 🧭 Guía de Funcionamiento del Backend

## Estructura General
- **main.py**: Archivo principal. Contiene la lógica de la API, inicialización de la base de datos, modelos y rutas web.
- **static/**: Archivos estáticos (CSS, JS, imágenes) para la interfaz web.
- **templates/**: Plantillas HTML para la interfaz de administración y usuario.
- **app.db**: Base de datos SQLite generada automáticamente.

## Flujo Principal
1. **Inicialización**: Al iniciar, se crea la base de datos y se insertan datos por defecto (admin y apps).
2. **Autenticación**: Se usa JWT para autenticar usuarios. El endpoint `/api/token` genera el token.
3. **Gestión de Usuarios**: Admins pueden crear, editar, eliminar y listar usuarios vía API o interfaz web.
4. **Gestión de Apps**: Admins pueden registrar, editar, bloquear/desbloquear y eliminar aplicaciones.
5. **Permisos**: Los usuarios solo ven y ejecutan apps para las que tienen permiso. Los admins pueden gestionar estos permisos.
6. **Ejecución de Apps**: El backend puede lanzar aplicaciones locales (ej: notepad.exe) usando `subprocess`.

## Modelos Principales
- **User**: Usuario del sistema (admin o regular).
- **App**: Aplicación registrada (nombre, descripción, ejecutable, categoría, estado).
- **UserAppPermissions**: Relación usuario-app para permisos de acceso.

## Endpoints Clave
- `/api/token`: Login y obtención de JWT.
- `/api/users`, `/api/apps`: CRUD de usuarios y apps (solo admin).
- `/api/apps/{id}/run`: Ejecuta la app si el usuario tiene permiso.
- `/api/apps/{id}/permissions`: Gestión de permisos por app.

## Interacción con la Base de Datos
- Usa SQLite y se conecta/desconecta en cada petición.
- Las tablas principales son `users`, `apps` y `user_app_permissions`.
- La función `init_database()` asegura que la estructura y datos iniciales existan.

## Interfaz Web
- Rutas `/admin`, `/admin/dashboard`, `/admin/users`, `/admin/apps` para admins.
- Rutas `/login`, `/perfil`, `/mis-apps` para usuarios.
- Usa Jinja2 para renderizar plantillas HTML.

## Integración con el Frontend
- El frontend React consume los endpoints REST del backend.
- El token JWT se usa para autenticar y autorizar peticiones.
- Los endpoints devuelven JSON para el frontend y HTML para la interfaz web.

## Seguridad
- Contraseñas hasheadas con bcrypt.
- JWT para sesiones seguras.
- Validación de roles y permisos en cada endpoint.

---

**User Management System v2.0** - A stable, modern backend for user and application management. 