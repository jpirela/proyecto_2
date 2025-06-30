# 🍰 Cupcake – Sistema de Inicio de Sesión con HTMX y Flask

Este proyecto es una implementación ligera y moderna de un sistema de autenticación, diseñado para ofrecer una experiencia fluida al usuario mediante tecnologías web modernas como HTMX, Flask y PostgreSQL.

---

## 🚀 Tecnologías utilizadas

- **HTML5 + CSS3**: estructura y diseño responsivo para una interfaz visual agradable y funcional.
- **HTMX**: permite enviar peticiones HTTP desde elementos HTML sin escribir JavaScript. Aquí se usa para enviar el formulario de inicio de sesión sin recargar la página.
- **Flask (Python)**: microframework web que gestiona las rutas, la lógica de autenticación y las respuestas dinámicas.
- **PostgreSQL**: sistema de base de datos relacional donde se almacenan los usuarios y su actividad.
- **SQL (pg_dump)**: se utilizó un volcado estructurado de la base de datos (`.sql`) para definir la tabla `users` y sus restricciones.

---

## 🧠 ¿Cómo funciona?

1. El usuario accede a una página de inicio de sesión con una interfaz clara y amigable.
2. Al enviar el formulario, HTMX realiza una solicitud `POST` a `/login` sin recargar la página.
3. El backend en Flask:
   - Conecta con PostgreSQL.
   - Valida si el usuario y contraseña coinciden con los registros.
   - Si es correcto, actualiza la columna `last_login` y devuelve un fragmento HTML de bienvenida o redirección.
   - Si hay un error, responde con un nuevo fragmento HTML que muestra un mensaje de error.
4. También están disponibles botones para iniciar sesión con Google o Facebook, listos para integrarse con OAuth si se desea expandir la autenticación.

---

## 📂 Base de datos

La tabla `users` contiene:
- `id`: clave primaria auto-incremental.
- `username`, `email`: únicos para cada usuario.
- `password`: almacenada en texto plano (recomendación futura: aplicar hash con bcrypt).
- `created_at`, `last_login`: para trazabilidad y control de acceso.

---

