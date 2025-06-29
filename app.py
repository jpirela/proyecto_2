from flask import Flask, jsonify, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import json
import os

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:clave@localhost:5432/pedidos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    items = db.Column(db.Text, nullable=False)  
    total = db.Column(db.Float, nullable=False)


@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)


@app.route('/pedidos', methods=['GET'])
def obtener_pedidos():
    try:
        pedidos = Pedido.query.order_by(Pedido.id.desc()).all()
        respuesta = []

        for p in pedidos:
            try:
                items = json.loads(p.items) if p.items else []
            except json.JSONDecodeError:
                items = []

            respuesta.append({
                "id": p.id,
                "items": items,
                "total": p.total
            })

        return jsonify(respuesta)

    except Exception as e:
        print("❌ Error al obtener pedidos:", e)
        return jsonify({"error": "Error interno del servidor"}), 500


@app.route('/pedido', methods=['POST'])
def crear_pedido():
    try:
        data = request.get_json()
        items = data.get('items', [])
        total = data.get('total', 0.0)

        # Validar datos
        if not isinstance(items, list) or not isinstance(total, (int, float)):
            return jsonify({"error": "Datos inválidos"}), 400

        pedido = Pedido(items=json.dumps(items), total=total)
        db.session.add(pedido)
        db.session.commit()
        return jsonify({"mensaje": "✅ Pedido guardado con éxito"})

    except Exception as e:
        print("❌ Error al guardar pedido:", e)
        return jsonify({"error": "No se pudo guardar el pedido"}), 500


@app.route('/pedido/<int:pedido_id>', methods=['DELETE'])
def eliminar_pedido(pedido_id):
    try:
        pedido = Pedido.query.get(pedido_id)
        if pedido:
            db.session.delete(pedido)
            db.session.commit()
            return jsonify({"mensaje": "🗑️ Pedido eliminado"})
        else:
            return jsonify({"error": "Pedido no encontrado"}), 404
    except Exception as e:
        print("❌ Error al eliminar pedido:", e)
        return jsonify({"error": "Error interno al eliminar"}), 500


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
