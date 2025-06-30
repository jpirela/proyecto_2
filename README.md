# 🔐 Kalypso Auth

Sistema de autenticación web desarrollado con **Flask**, **PostgreSQL**, **SQLAlchemy** y **HTMX**, enfocado en el registro y acceso de usuarios con una interfaz limpia, validaciones seguras y un backend modular y escalable.

---

## 🧩 Tecnologías utilizadas

- **Python 3** + **Flask** – Framework web ligero
- **SQLAlchemy** – ORM para modelar la base de datos
- **PostgreSQL** – Base de datos relacional
- **HTMX** – Interacción asincrónica sin recarga de página
- **Werkzeug** – Hash seguro de contraseñas
- **HTML/CSS** – Frontend semántico y moderno

---

## 📁 Estructura del proyecto

kalypso_auth/
├── app/
│   ├── __init__.py                 # Inicializa Flask + SQLAlchemy
│   ├── routes.py                   # Rutas /login y /register
│   ├── models.py                   # Definición de User y LoginAttempt (SQLAlchemy)
│   ├── static/
│   │   └── css/
│   │       └── styles.css          # Estilos del frontend
│   └── templates/
│       ├── layout.html             # Plantilla base
│       ├── login.html              # Formulario de inicio de sesión con HTMX
│       └── register.html           # Formulario de registro con HTMX
├── kalypso_auth.sql                # Script SQL alternativo para crear tablas (opcional)
├── requirements.txt                # flask, flask_sqlalchemy, werkzeug, psycopg2
├── run.py                          # Script de arranque del servidor Flask
└── README.md                       # Documentación del proyecto


---

## 🛠️ Instalación

1. **Clona el repositorio:**


git clone https://github.com/tuusuario/kalypso_auth.git
cd kalypso_auth

2. **Activa el entorno virtual:**

python -m venv env
source env/bin/activate  # o env\Scripts\activate en Windows


3. **Instala dependencias:**

pip install -r requirements.txt

4. **Configura tu base de datos PostgreSQL:**


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:contraseña@localhost/kalypso_db'


5. **Crea las tablas desde consola Python:**

python
>>> from app import db
>>> db.create_all()
>>> exit()


6. **Lanza el servidor:**

python run.py

✨ Funcionalidades
Registro de usuarios con validación de nombre, email y contraseña

Hash de contraseñas seguro con Werkzeug

Inicio de sesión con validación de credenciales

Registro automático de intentos de acceso (exitosos y fallidos)

Interfaz fluida con HTMX (sin recarga de página)

Validación de username contra inyecciones SQL y datos maliciosos

Modelo extensible con relaciones entre usuarios e intentos