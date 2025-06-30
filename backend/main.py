from flask import Flask, render_template, jsonify, request
from backend.db import init_db, db
from backend.models import DesktopItem
import os

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), 'templates'),
    static_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), '../frontend'))
)
init_db(app)

@app.route("/")
def home():
    items = DesktopItem.query.all()
    return render_template("index.html", items=items)

# Ruta temporal para poblar la base de datos con los íconos PNG detectados en la carpeta icons
@app.route("/poblar_iconos")
def poblar_iconos():
    iconos = [
        ("Navegador", "browser.svg"),
        ("Documentos", "doc.svg"),
        ("Archivos", "folder.svg"),
        ("Imágenes", "image.svg"),
        ("Menú", "menu.svg"),
        ("Configuración", "settings.svg"),
        ("Terminal", "terminal.svg"),
        ("Usuario", "user.svg")
    ]
    for i, (nombre, archivo) in enumerate(iconos):
        existe = DesktopItem.query.filter_by(icon_url=archivo).first()
        if not existe:
            item = DesktopItem(name=nombre, icon_url=archivo, x=100 + i*100, y=100)
            db.session.add(item)
    db.session.commit()
    return "Íconos insertados correctamente. Puedes volver al escritorio principal."

@app.route("/api/icons")
def listar_iconos():
    icons_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../frontend/icons'))
    archivos = [f for f in os.listdir(icons_path) if f.endswith('.svg')]
    return jsonify(archivos)

if __name__ == "__main__":
    app.run(debug=True)
