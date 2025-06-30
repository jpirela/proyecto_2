from flask import (
    Flask, render_template, request,
    redirect, url_for, flash, session,
    send_from_directory
)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from datetime import datetime

# Flask levantado desde la raíz: busca HTML y estáticos en el directorio actual
app = Flask(
    __name__,
    template_folder='.',
    static_folder='.',
    static_url_path=''
)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://postgres:Nana030106@localhost/roxx'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'cambia_esta_clave_por_una_segura'

db = SQLAlchemy(app)

# Test de conexión a la BD
with app.app_context():
    try:
        db.session.execute(text('SELECT 1'))
        print("✅ Conexión exitosa a la base de datos.")
    except Exception as e:
        print("❌ Error al conectar:", e)

# Modelo de usuario con contraseña en texto plano
class User(db.Model):
    __tablename__ = 'users'

    id          = db.Column(db.BigInteger, primary_key=True)
    username    = db.Column(db.String, unique=True, nullable=False)
    password    = db.Column(db.String, nullable=False)  # texto plano
    email       = db.Column(db.String, unique=True, nullable=False)
    created_at  = db.Column(db.DateTime(timezone=True),
                            default=datetime.utcnow)
    last_login  = db.Column(db.DateTime(timezone=True))

    def __repr__(self):
        return f'<User {self.username}>'

# Rutas ----------------------------------------------------

# Página de login
@app.route('/')
def home():
    return render_template('interfaz.html')

# Página de registro
@app.route('/register-page')
def register_page():
    return render_template('register.html')

# Sirve tu CSS (suponiendo que tienes un style.css en la raíz)
@app.route('/style.css')
def css():
    return send_from_directory('.', 'style.css', mimetype='text/css')

# Registro de usuario
@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    email    = request.form['email']

    # Evita duplicados
    if User.query.filter((User.username==username)|(User.email==email)).first():
        flash('Usuario o email ya registrado')
        return redirect(url_for('register_page'))

    nuevo = User(username=username, password=password, email=email)
    db.session.add(nuevo)
    db.session.commit()

    flash('Registro exitoso. Por favor inicia sesión.')
    return redirect(url_for('home'))

# Login de usuario
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()

    if user and user.password == password:  # comparar directamente la cadena
        user.last_login = db.func.current_timestamp()
        db.session.commit()
        return "<p style='color:pink;'>BIENVENIDO!!</p>"
    return "<p style='color:red;'>Credenciales inválidas</p>"

# (Opcional) Endpoints OAuth simulados:
@app.route('/oauth/google')
def oauth_google():
    return '<h1>Iniciando OAuth Google…</h1>'

@app.route('/oauth/facebook')
def oauth_facebook():
    return '<h1>Iniciando OAuth Facebook…</h1>'

# Ejecutar
if __name__ == '__main__':
    app.run(debug=True)