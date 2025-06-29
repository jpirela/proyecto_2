from app import app
from models import db, MenuItem

with app.app_context():
    platos = [
        MenuItem(nombre='Pasta Alfredo', descripcion='Cremosa salsa de queso parmesano.', precio=11.99),
        MenuItem(nombre='Hamburguesa Clásica', descripcion='Carne jugosa y pan artesanal.', precio=9.99),
        MenuItem(nombre='Tiramisú', descripcion='Postre italiano con café y mascarpone.', precio=6.50),
        MenuItem(nombre='Limonada', descripcion='Refrescante bebida natural.', precio=3.00),
        MenuItem(nombre='Refresco', descripcion='Refrescante bebida gaseosa.', precio=4.00),
    ]
    db.session.bulk_save_objects(platos)
    db.session.commit()
    print("✅ Menú cargado en la base de datos.")
