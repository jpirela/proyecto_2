# Proyecto: Registro Web, Backend y Aplicación de Escritorio

Este proyecto es una solución simple que conecta una página web (frontend), un servidor backend con Node.js, y una aplicación de escritorio con Python. Permite registrar usuarios con nombre y correo electrónico, verlos en una app de escritorio, y almacenarlos temporalmente en memoria a través del backend.

---

## 📁 Estructura del Proyecto

```
web_desktop_backend/
├── frontend/        # Página web (HTML + JS)
│   └── index.html
├── backend/         # Servidor con Node.js (API REST)
│   └── server.js
├── desktop/         # Aplicación de escritorio (Python + Tkinter)
│   └── desktop_app.py
└── README.md        # Este archivo
```

---

## ✅ Requisitos

- Node.js instalado
- Python 3 instalado
- Módulo `requests` de Python (`pip install requests`)

---

## 🚀 Instrucciones para Ejecutar

### 🔧 1. Iniciar el Backend

```bash
cd backend
npm init -y
npm install express cors
node server.js
```

> El servidor se ejecutará en: `http://localhost:3000`

---

### 🌐 2. Ejecutar la Página Web

Abre el archivo `frontend/index.html` en tu navegador (doble clic o con [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)).

- Completa el formulario
- Haz clic en "Enviar"
- Los datos se enviarán al backend

---

### 💻 3. Ejecutar la Aplicación de Escritorio

```bash
cd desktop
pip install requests   # (solo la primera vez)
python desktop_app.py
```

- Haz clic en **"Cargar Usuarios"**
- Se mostrarán los datos enviados desde la web

---

## 🧠 ¿Cómo Funciona?

1. La web envía datos al backend (POST).
2. El backend guarda esos datos en una lista en memoria.
3. La app de escritorio consulta los datos al backend (GET) y los muestra.

---

## 📌 Notas

- Los datos se guardan solo en memoria (no hay base de datos).
- Al reiniciar el servidor, se pierden los datos.
- Se puede ampliar con una base de datos como SQLite o MongoDB.

---

## 👤 Desarrollado por

**Miguelangel Contreras**
