# Frontend - Sistema de Gestión de Usuarios

Este frontend es una aplicación React que permite a los usuarios autenticarse, ver su perfil y ejecutar aplicaciones asignadas, interactuando con el backend vía API REST.

## 🚀 Requisitos
- Node.js 14+
- npm (Node Package Manager)

## 📦 Instalación y Ejecución

1. **Instalar dependencias:**
   ```bash
   cd frontend
   npm install
   ```

2. **Iniciar la aplicación:**
   ```bash
   npm start
   ```
   Esto abrirá la app en [http://localhost:3000](http://localhost:3000)

> **Nota:** El backend debe estar corriendo en [http://localhost:8000](http://localhost:8000) para que la autenticación y las funciones de usuario funcionen correctamente.

## 🗂️ Estructura de Archivos

- `src/App.js`: Configura las rutas principales de la app.
- `src/components/Home.js`: Página de bienvenida e inicio.
- `src/components/Login.js`: Formulario de inicio de sesión, obtiene el token JWT del backend.
- `src/components/Perfil.js`: Muestra información del usuario autenticado (pendiente de integración real).
- `src/components/MisApps.js`: Lista y permite ejecutar las aplicaciones asignadas al usuario.
- `public/index.html`: Punto de entrada HTML.

## 🧩 Descripción de Componentes

### App.js
Define las rutas principales:
- `/` → Home
- `/login` → Login
- `/perfil` → Perfil de usuario
- `/mis-apps` → Aplicaciones asignadas

### Home.js
Pantalla de bienvenida con acceso al login.

### Login.js
Formulario de autenticación. Envía usuario y contraseña al backend (`/api/token`). Si es exitoso, guarda el token JWT en `localStorage` y redirige a `/perfil`.

### Perfil.js
Muestra información del usuario autenticado (nombre y rol). Actualmente, los datos son estáticos, pero se recomienda integrar la consulta real al backend usando el token JWT.

### MisApps.js
- Obtiene la lista de aplicaciones permitidas para el usuario autenticado (`/api/apps`).
- Permite ejecutar una app haciendo POST a `/api/apps/{id}/run`.
- Muestra mensajes de error o éxito según la respuesta del backend.

## 🔗 Integración con Backend
- El frontend se comunica con el backend FastAPI en `http://localhost:8000`.
- El token JWT se almacena en `localStorage` y se envía en el header `Authorization` para endpoints protegidos.
- Si el token no es válido o falta, se muestra un error y se solicita iniciar sesión.

## 🛠️ Personalización y Desarrollo
- Puedes modificar los estilos en `src/styles/` o usando Bootstrap.
- Para agregar nuevas páginas, crea un componente y agrégalo a las rutas en `App.js`.
- Para consumir nuevos endpoints, usa `fetch` o una librería como `axios`.

## 🧪 Pruebas
- Usa `npm test` para ejecutar los tests incluidos por Create React App.

## 📝 Notas
- El frontend está pensado para funcionar junto al backend incluido en este proyecto.
- Si cambias la URL o el puerto del backend, actualiza las URLs en los componentes que hacen fetch.

---

**Sistema de Gestión de Usuarios - Frontend React** 