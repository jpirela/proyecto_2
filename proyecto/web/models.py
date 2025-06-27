from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Llave(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(50), unique=True, nullable=False)

class Texto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto_inicial = db.Column(db.String(50))
    texto_resultante = db.Column(db.String(50))
    key_id = db.Column(db.Integer)