from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import re


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ELZC20051709*@localhost/kalypso_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


try:
    with app.app_context():
        db.session.execute(text('SELECT 1'))
    print("✅ Conexión exitosa a la base de datos.")
except Exception as e:
    print("❌ Error al conectar con la base de datos:",e)

# Modelos
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False) 
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class LoginAttempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    success = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # ← debe coincidir con __tablename__
    user = db.relationship('User', backref='login_attempts')

# Validación de nombre de usuario
def validar_username(username):
    return re.match(r'^[a-zA-Z0-9_]{3,30}$', username)

# Ruta raíz
@app.route('/')
def index():
    return redirect('/login')

# Ruta de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form.get('username', '').strip()
    password = request.form.get('password')

    if not validar_username(username):
        return '<p style="color:red;">Formato de usuario inválido</p>'

    user = User.query.filter_by(username=username).first()
    success = user and user.password == password  # Comparación directa

    login_attempt = LoginAttempt(user=user if success else None, username=username, success=success)
    db.session.add(login_attempt)
    db.session.commit()

    return '<p style="color:green;">Login exitoso</p>' if success else '<p style="color:red;">Usuario o contraseña incorrectos</p>'

# Ruta de registro
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    username = request.form.get('username', '').strip()
    email = request.form.get('email', '').strip()
    password = request.form.get('password')

    if not validar_username(username):
        return '<p style="color:red;">Nombre de usuario inválido</p>'

    if User.query.filter((User.username == username) | (User.email == email)).first():
        return '<p style="color:red;">Usuario o correo ya registrado</p>'

    new_user = User(
        username=username,
        email=email,
        password=password  # Texto plano solo para pruebas
    )
    db.session.add(new_user)
    db.session.commit()

    return '<p style="color:green;">Registro exitoso. Ya puedes <a href="/login">iniciar sesión</a>.</p>'

# Ruta para verificar la conexión con la base de datos


# Ejecutar aplicación
if __name__ == '__main__':
    app.run(debug=True)