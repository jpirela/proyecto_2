# Gestor de Tareas MC

Aplicación full stack para la gestión personal de tareas, construida con **Node.js**, **Express**, **Sequelize** y **PostgreSQL** en el backend, y una interfaz web dinámica en **HTML**, **CSS** y **JavaScript** puro. Incluye autenticación básica, documentación Swagger y una arquitectura modular enfocada en buenas prácticas.

## Tecnologías Utilizadas

### Backend – API RESTful
- **Node.js v18+**: Entorno de ejecución para servidor JavaScript
- **Express.js v5.1.0**: Framework para ruteo, middlewares y estructura REST
- **Sequelize v6.37.7**: ORM para definir modelos, relaciones y validaciones
- **PostgreSQL v17.5**: Base de datos robusta con integridad referencial y consultas avanzadas
- **dotenv v16.5.0**: Manejo seguro de variables de entorno
- **pg / pg-hstore**: Conexión nativa a PostgreSQL y serialización JSON

### Documentación y Validación
- **Swagger UI Express v5.0.1**: Documentación interactiva disponible en `/api-docs`
- **YAMLJS v0.3.0**: Carga del esquema OpenAPI desde `docs/usuario.yaml`
- **Middlewares personalizados**: Validación manual antes de acceder a los controladores

### Frontend – Interfaz Web
- **HTML5 & CSS3**: Estructura semántica con estilos visuales modernos
- **JavaScript (ES6)**: Scripts modulares para renderizado y consumo de la API
- **Axios v1.10.0**: Peticiones HTTP eficientes y simplificadas
- **LocalStorage**: Gestión del estado de autenticación del usuario
- **Componentes reutilizables**: Scripts independientes para crear, modificar y eliminar tareas
- **Diseño temático**: Fondos texturizados, botones animados y modales personalizados



## Estructura del Proyecto

```bash
proyecto-gestor-de-tareas/
├── base-de-datos/
│   └── bade_tarea.sql
├── proyecto-taskflow/
│   ├── index.html
│   ├── index.css
│   ├── index.js
│   ├── modal.js
│   ├── modal.css
│   ├── assets/
│   │   ├── image.png
│   │   └── madera.png
│   └── components/
│       ├── task/
│       │   ├── task.html
│       │   ├── task.css
│       │   └── crear.js
│       ├── modificar/
│       │   ├── modificar.js
│       │   └── modificar-task.js
│       └── eliminar/
│           └── eliminar.js
├── apigestordetareas/
│   ├── app.js
│   ├── config/
│   │   └── db.js
│   ├── controllers/
│   │   ├── usuarioController.js
│   │   ├── tareaController.js
│   │   └── comentarioController.js
│   ├── docs/
│   │   └── usuario.yaml
│   ├── middlewares/
│   │   ├── validarComentario.js
│   │   ├── validarUsuario.js
│   │   └── validarTarea.js
│   ├── models/
│   │   ├── usuario.js
│   │   ├── tarea.js
│   │   └── comentario.js
│   ├── routes/
│   │   ├── usuarioRoutes.js
│   │   ├── tareaRoutes.js
│   │   └── comentarioRoutes.js
│   ├── swagger/
│   │   └── swagger.js
│   ├── .env
│   ├── APP.js
│   ├── nodemon.json
│   └── package.json
```



## ¿Cómo funciona?

### 1. Servidor (API)
- Gestiona rutas RESTful para `usuarios`, `tareas` y `comentarios`
- Realiza operaciones CRUD conectadas a PostgreSQL
- Expone documentación Swagger
- Aplica validaciones manuales antes de registrar datos en la BD

### 2. Cliente (Web)
- Carga dinámica de tareas según el usuario autenticado
- Manejo de sesión con `localStorage` y modales interactivos
- Permite registrar usuarios, crear/modificar/eliminar tareas



## Cómo correr el servidor desde la carpeta API

```bash
cd /ruta/a/gestor-tareas-mc
npm install
```

Archivo `.env` necesario:

```env
DB_NAME=gestor_tareas
DB_USER=postgres
DB_PASS=tu_contraseña
DB_HOST=localhost
```

Importa la base de datos:

```bash
psql -U postgres -d gestor_tareas -f base-de-datos/bade_tarea.sql
```

Corre el servidor:

```bash
npm run dev
# o
npm start
```


## Cómo usar la interfaz web

1. Abre `index.html` en tu navegador
2. Regístrate o inicia sesión
3. Crea, modifica o elimina tareas usando los botones y modales


## Documentación Swagger

Disponible en:  
`http://localhost:3000/api-docs`



## Base de Datos

Incluye validaciones, relaciones `ON DELETE CASCADE`, y claves únicas.



## Autor

Desarrollado por **Marco**, con enfoque en organización y buenas prácticas.




