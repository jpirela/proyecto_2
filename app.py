# ============================================================================
# APLICACIÓN PRINCIPAL - COORDINADOR DE BACKEND Y FRONTEND
# ============================================================================

try:
    from flask import Flask, request, jsonify, render_template_string
except ImportError:
    print("Error: Flask no está instalado. Por favor instala Flask con: pip install flask")
    exit(1)

from backend import VentasBackend
from frontend import VentasFrontend

class AplicacionVentas:
    """Clase principal que coordina el backend y frontend"""
    
    def __init__(self):
        self.app = Flask(__name__)
        self.backend = VentasBackend()
        self.frontend = VentasFrontend()
        self.configurar_rutas()
    
    def configurar_rutas(self):
        """Configura todas las rutas de la aplicación"""
        
        @self.app.route('/')
        def index():
            """Ruta principal - Página de inicio"""
            return render_template_string(self.frontend.obtener_html_template())
        
        @self.app.route('/ventas', methods=['GET', 'POST'])
        def ventas_route():
            """API para gestionar ventas"""
            if request.method == 'POST':
                # Crear nueva venta
                data = request.get_json()
                resultado = self.backend.agregar_venta(
                    data['producto'],
                    data['cantidad'],
                    data['precio']
                )
                return jsonify(resultado)
            else:
                # Obtener todas las ventas
                return jsonify(self.backend.obtener_ventas())
        
        @self.app.route('/ventas/<int:venta_id>', methods=['DELETE'])
        def eliminar_venta(venta_id):
            """API para eliminar una venta específica"""
            resultado = self.backend.eliminar_venta(venta_id)
            return jsonify(resultado)
        
        @self.app.route('/ventas/limpiar', methods=['DELETE'])
        def limpiar_ventas():
            """API para eliminar todas las ventas"""
            resultado = self.backend.limpiar_ventas()
            return jsonify(resultado)
        
        @self.app.route('/ventas/buscar/<int:venta_id>', methods=['GET'])
        def buscar_venta(venta_id):
            """API para buscar una venta específica"""
            venta = self.backend.buscar_venta(venta_id)
            if venta:
                return jsonify({'status': 'success', 'venta': venta})
            else:
                return jsonify({'status': 'error', 'message': 'Venta no encontrada'})
        
        @self.app.route('/ventas/producto/<producto>', methods=['GET'])
        def ventas_por_producto(producto):
            """API para obtener ventas de un producto específico"""
            ventas = self.backend.obtener_ventas_por_producto(producto)
            return jsonify(ventas)
        
        @self.app.route('/estadisticas')
        def estadisticas():
            """API para obtener estadísticas de ventas"""
            return jsonify(self.backend.obtener_estadisticas())
        
        @self.app.route('/api/health')
        def health_check():
            """API para verificar el estado del servidor"""
            return jsonify({
                'status': 'ok',
                'message': 'Servidor funcionando correctamente',
                'ventas_registradas': len(self.backend.obtener_ventas())
            })
    
    def ejecutar(self, debug=True, host='0.0.0.0', port=5000):
        """Ejecuta la aplicación Flask"""
        print("=" * 60)
        print("🚀 SISTEMA DE REGISTRO DE VENTAS")
        print("=" * 60)
        print(f"📊 Backend: VentasBackend")
        print(f"🎨 Frontend: VentasFrontend")
        print(f"🌐 Servidor: http://localhost:{port}")
        print(f"🔧 Modo debug: {'Activado' if debug else 'Desactivado'}")
        print(f"📈 API Endpoints:")
        print(f"   - GET  /ventas - Obtener todas las ventas")
        print(f"   - POST /ventas - Crear nueva venta")
        print(f"   - DELETE /ventas/<id> - Eliminar venta")
        print(f"   - DELETE /ventas/limpiar - Limpiar todas las ventas")
        print(f"   - GET  /estadisticas - Obtener estadísticas")
        print(f"   - GET  /api/health - Estado del servidor")
        print("=" * 60)
        
        try:
            self.app.run(debug=debug, host=host, port=port)
        except KeyboardInterrupt:
            print("\n🛑 Servidor detenido por el usuario")
        except Exception as e:
            print(f"❌ Error al iniciar el servidor: {e}")

# ============================================================================
# PUNTO DE ENTRADA DE LA APLICACIÓN
# ============================================================================

if __name__ == '__main__':
    # Crear y ejecutar la aplicación
    app = AplicacionVentas()
    app.ejecutar() 