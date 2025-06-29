from flask import Flask, render_template, request, redirect, url_for
from models import db, Contacto

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:clave@localhost:5432/contactos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    contactos = Contacto.query.all()
    return render_template('index.html', contactos=contactos)

@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    correo = request.form['correo']
    nuevo = Contacto(nombre=nombre, telefono=telefono, correo=correo)
    db.session.add(nuevo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/eliminar/<int:id>')
def eliminar(id):
    contacto = Contacto.query.get(id)
    db.session.delete(contacto)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/editar/<int:id>', methods=['POST'])
def editar(id):
    contacto = Contacto.query.get(id)
    contacto.nombre = request.form['nombre']
    contacto.telefono = request.form['telefono']
    contacto.correo = request.form['correo']
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
