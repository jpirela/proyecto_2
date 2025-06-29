


````
# 📇 Gestor de Contactos

Este es un **Gestor de Contactos** web simple desarrollado con **Python (Flask)**, **PostgreSQL**, **SQLAlchemy**, y una interfaz hecha con **HTML y CSS**. Permite agregar, editar y eliminar contactos.

---

## 🧩 Tecnologías utilizadas

- **Python **
- **Flask**
- **PostgreSQL**
- **SQLAlchemy**
- **HTML**
- **CSS**
- **pgAdmin** (para gestión visual de la base de datos)

---

## 🚀 ¿Qué se puede hacer?

✅ Agregar nuevos contactos  
✅ Editar información de un contacto existente  
✅ Eliminar contactos  

---

## 🛠️ Instalación

###  Instalar las dependencias

Flask
Flask-SQLAlchemy
psycopg2-binary

###  Configurar la conexión en `app.py`

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:contraseña@localhost:5432/contactos'
```

Reemplazar `usuario` y `contraseña` por los datos reales de tu base de datos.

---

## ▶️ Ejecución

Ejecutar el servidor Flask:

```
python app.py
```

Abrir el navegador en:

```
http://localhost:5000
```

---