🍳 Mi Recetario Online
Una aplicación web sencilla pero potente para guardar y consultar tus recetas de cocina favoritas. Construida con un stack tecnológico moderno (PostgreSQL, Express, Node.js y Vanilla JS) para demostrar una arquitectura Full-Stack completa.



¡Aquí puedes agregar una captura de pantalla de tu aplicación en funcionamiento! Simplemente toma un screenshot, súbelo a la carpeta del proyecto y cambia el nombre del archivo en la siguiente línea.

🚀 Características
Añadir nuevas recetas: Un formulario intuitivo para guardar el nombre, los ingredientes y las instrucciones de tus platos.

Visualización instantánea: Las recetas se muestran en tiempo real en una lista ordenada cronológicamente.

Arquitectura desacoplada: El frontend (cliente) y el backend (servidor) funcionan de manera independiente, comunicándose a través de una API REST.

Persistencia de datos: Todas las recetas se almacenan de forma segura en una base de datos PostgreSQL.

🔧 Stack Tecnológico
Este proyecto fue construido utilizando las siguientes tecnologías:

Frontend:

HTML5

CSS3 (sin frameworks)

JavaScript (Vanilla JS con Fetch API para peticiones a la API)

Backend:

Node.js: Entorno de ejecución para JavaScript en el servidor.

Express.js: Framework para construir la API REST de forma rápida y organizada.

Base de Datos:

PostgreSQL: Sistema de gestión de bases de datos relacional, potente y de código abierto.

Herramientas de Desarrollo:

Nodemon: Para reiniciar el servidor automáticamente durante el desarrollo.

Dotenv: Para la gestión de variables de entorno de forma segura.

📂 Requisitos Previos
Antes de comenzar, asegúrate de tener instalado el siguiente software en tu sistema:

Node.js (versión 14 o superior)

npm (normalmente viene con Node.js)

PostgreSQL

🛠️ Instalación y Configuración
Sigue estos pasos para tener una copia del proyecto funcionando en tu máquina local.

Clona el repositorio (o simplemente descarga los archivos en tu carpeta):

Bash

git clone https://github.com/tu-usuario/mi-recetario-app.git
cd mi-recetario-app
Configuración del Backend (Servidor):

Navega a la carpeta del servidor:

Bash

cd server
Instala todas las dependencias de npm:

Bash

npm install
Configura la base de datos: Abre psql o tu cliente de PostgreSQL preferido y ejecuta lo siguiente para crear la base de datos y la tabla:

SQL

CREATE DATABASE recetario_db;

-- Conéctate a la base de datos recién creada antes de ejecutar el siguiente comando
\c recetario_db

CREATE TABLE recetas (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    ingredientes TEXT NOT NULL,
    instrucciones TEXT NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
Configura las variables de entorno: Crea una copia del archivo de ejemplo .env.example (o crea uno nuevo) y llámalo .env.

Bash

# Puedes usar 'cp .env.example .env' en Linux/Mac
# o simplemente crea el archivo .env manualmente
Abre tu nuevo archivo .env y rellena los datos de tu base de datos. ¡No olvides tu contraseña!

DB_USER=postgres
DB_PASSWORD=tu_contraseña_secreta
DB_HOST=localhost
DB_PORT=5432
DB_DATABASE=recetario_db
Configuración del Frontend (Cliente):

El frontend es estático (HTML, CSS, JS puros), por lo que no requiere instalación de dependencias. ¡Ya está listo para usarse!

🏃‍♂️ Cómo Ejecutar la Aplicación
Para que la aplicación funcione, necesitas tener el servidor y el cliente corriendo al mismo tiempo.

Iniciar el Servidor Backend:

En una terminal, navega a la carpeta server y ejecuta:

Bash

npm run dev
Verás un mensaje de confirmación: ✅ Servidor escuchando en http://localhost:3000. ¡Déjalo corriendo!

Iniciar el Cliente Frontend:

Abre una nueva terminal o simplemente navega en tu explorador de archivos a la carpeta client.

Abre el archivo index.html en tu navegador web.

Recomendación: Usa la extensión Live Server en Visual Studio Code. Haz clic derecho en index.html y selecciona "Open with Live Server".

¡Y listo! Ya puedes empezar a añadir y ver tus recetas.

🗺️ Endpoints de la API
El backend expone los siguientes endpoints:

Método HTTP

Ruta

Descripción

GET

/api/recetas

Obtiene una lista de todas las recetas.

POST

/api/recetas

Crea una nueva receta.


Exportar a Hojas de cálculo
📝 Próximas Mejoras (To-Do)
[ ] Implementar funcionalidad para Eliminar una receta.

[ ] Implementar funcionalidad para Editar una receta existente.

[ ] Añadir un sistema de autenticación de usuarios para que cada persona tenga su propio recetario.

[ ] Crear un campo de búsqueda para filtrar recetas por nombre o ingredientes.

[ ] Mejorar la interfaz de usuario y la experiencia de usuario (UI/UX).