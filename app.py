from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# 1) Ajusta estos datos según tu entorno MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="TU_CONTRASEÑA",
    database="formulario_db"
)
cursor = conn.cursor(dictionary=True)

# Página principal con el formulario
@app.route('/')
def index():
    return render_template('formulario.html')

# Ruta que recibe el POST del formulario
@app.route('/enviar', methods=['POST'])
def enviar():
    nombre = request.form['nombre']
    correo = request.form['correo']
    mensaje = request.form['mensaje']

    cursor.execute(
        "INSERT INTO persona (nombre, correo, mensaje) VALUES (%s, %s, %s)",
        (nombre, correo, mensaje)
    )
    conn.commit()
    # Respuesta que HTMX inyectará en la página
    return '<div class="success">✅ Formulario enviado correctamente</div>'

# Página que muestra todas las respuestas
@app.route('/ver-respuestas')
def ver_respuestas():
    cursor.execute(
        "SELECT nombre, correo, mensaje, fecha_envio "
        "FROM persona ORDER BY fecha_envio DESC"
    )
    respuestas = cursor.fetchall()
    return render_template('respuestas.html', respuestas=respuestas)

if __name__ == '__main__':
    app.run(debug=True)