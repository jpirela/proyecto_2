# ============================================================================
# BACKEND - GESTIÓN DE DATOS Y LÓGICA DE NEGOCIO
# ============================================================================

class VentasBackend:
    """Clase para manejar la lógica de negocio y datos de ventas"""
    
    def __init__(self):
        self.ventas = []
    
    def agregar_venta(self, producto, cantidad, precio):
        """Agrega una nueva venta al sistema"""
        try:
            venta = {
                'id': len(self.ventas) + 1,
                'producto': producto,
                'cantidad': int(cantidad),
                'precio': float(precio),
                'total': int(cantidad) * float(precio)
            }
            self.ventas.append(venta)
            return {'status': 'success', 'venta': venta}
        except (ValueError, TypeError) as e:
            return {'status': 'error', 'message': f'Error en los datos: {str(e)}'}
    
    def obtener_ventas(self):
        """Obtiene todas las ventas registradas"""
        return self.ventas
    
    def obtener_estadisticas(self):
        """Calcula y retorna estadísticas de ventas"""
        if not self.ventas:
            return {
                'total_ventas': 0,
                'total_productos': 0,
                'ingresos_totales': 0,
                'promedio_venta': 0
            }
        
        total_ventas = len(self.ventas)
        total_productos = sum(v['cantidad'] for v in self.ventas)
        ingresos_totales = sum(v['total'] for v in self.ventas)
        promedio_venta = ingresos_totales / total_ventas if total_ventas > 0 else 0
        
        return {
            'total_ventas': total_ventas,
            'total_productos': total_productos,
            'ingresos_totales': ingresos_totales,
            'promedio_venta': promedio_venta
        }
    
    def eliminar_venta(self, venta_id):
        """Elimina una venta específica"""
        for i, venta in enumerate(self.ventas):
            if venta['id'] == venta_id:
                del self.ventas[i]
                return {'status': 'success', 'message': 'Venta eliminada'}
        return {'status': 'error', 'message': 'Venta no encontrada'}
    
    def buscar_venta(self, venta_id):
        """Busca una venta específica por ID"""
        for venta in self.ventas:
            if venta['id'] == venta_id:
                return venta
        return None
    
    def obtener_ventas_por_producto(self, producto):
        """Obtiene todas las ventas de un producto específico"""
        return [v for v in self.ventas if v['producto'].lower() == producto.lower()]
    
    def limpiar_ventas(self):
        """Elimina todas las ventas (reset del sistema)"""
        self.ventas.clear()
        return {'status': 'success', 'message': 'Todas las ventas han sido eliminadas'} 