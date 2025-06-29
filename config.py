import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://user:clave@localhost:5432/pedidos")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
