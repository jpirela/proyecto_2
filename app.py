from flask import Flask, request, redirect, url_for, render_template_string, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:yolo1300@localhost/login'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

try:
    with app.app_context():
        db.session.execute(text('SELECT 1'))
    print("✅ Conexión exitosa a la base de datos.")
except Exception as e:
    print("❌ Error al conectar con la base de datos:", e)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)  # <-- cambiar a password sin hash
    email = db.Column(db.String, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    last_login = db.Column(db.DateTime)

@app.route('/')
def home():
    with open('interfaz.html', 'r', encoding='utf-8') as f:
        return render_template_string(f.read())

@app.route('/register-page')
def register_page():
    with open('register.html', 'r', encoding='utf-8') as f:
        return render_template_string(f.read())

@app.route('/style.css')
def style():
    return send_from_directory('.', 'style.css')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

    
    existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
    if existing_user:
        return "<p style='color:red;'>❌ Usuario o correo ya registrado.</p>"

    new_user = User(username=username, password=password, email=email)
    db.session.add(new_user)
    db.session.commit()
    return "<h1>✅ Registro exitoso</h1><a href='/'>Ir al login</a>"


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()

    if user and user.password == password:  
        user.last_login = db.func.current_timestamp()
        db.session.commit()
        return "<h1>Inicio exitoso</h1>"
    return "<p style='color:red;'>Credenciales inválidas</p>"

if __name__ == '__main__':
    app.run(debug=True)
