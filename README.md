
# Sistema de Registro y Login con Flask

## 🛠 Tecnologías utilizadas

- **Python 3.11**
- **Flask** – Framework web para crear la aplicación.
- **HTML5** – Para la estructura de la interfaz de usuario.
- **CSS3** – Para el diseño visual y estilos.
- **HTMX** – Para interactividad dinámica sin necesidad de JavaScript completo.
- **Werkzeug** – Para el manejo seguro de contraseñas (hash).
- **PostgreSQL** – Base de datos para almacenar usuarios.

## ⚙️ ¿Cómo funciona?

Este proyecto es una aplicación web simple que permite a los usuarios registrarse y luego iniciar sesión. Los datos del usuario (nombre de usuario, correo electrónico y contraseña) se almacenan en una base de datos PostgreSQL, donde la contraseña se guarda cifrada.

HTMX se utiliza para mejorar la interactividad del sitio web, permitiendo actualizaciones parciales de la página sin recargar por completo.

Cuando un usuario inicia sesión correctamente, es redirigido a una página protegida. Si las credenciales son incorrectas, se muestra un mensaje de error. El diseño de la interfaz está hecho con HTML, CSS y HTMX, y la lógica del backend con Flask en Python.
