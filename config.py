# ============================================================================
# CONFIGURACIÓN DEL SISTEMA DE REGISTRO DE VENTAS
# ============================================================================

class Config:
    """Clase de configuración centralizada para la aplicación"""
    
    # Configuración del servidor
    HOST = '0.0.0.0'
    PORT = 5000
    DEBUG = True
    
    # Configuración de la aplicación
    APP_NAME = "Sistema de Registro de Ventas"
    APP_VERSION = "2.0.0"
    APP_DESCRIPTION = "Sistema moderno para gestión y control de ventas"
    
    # Configuración de la base de datos (futuro)
    DATABASE_URL = None  # Para futuras implementaciones con base de datos
    
    # Configuración de seguridad
    SECRET_KEY = "tu_clave_secreta_aqui_cambiala_en_produccion"
    
    # Configuración de logging
    LOG_LEVEL = "INFO"
    LOG_FILE = "ventas.log"
    
    # Configuración de la interfaz
    THEME_COLORS = {
        'primary': '#4f46e5',
        'secondary': '#7c3aed',
        'success': '#10b981',
        'danger': '#ef4444',
        'warning': '#f59e0b',
        'info': '#3b82f6'
    }
    
    # Configuración de estadísticas
    STATS_REFRESH_INTERVAL = 5000  # milisegundos
    
    # Configuración de validación
    MIN_CANTIDAD = 1
    MIN_PRECIO = 0.01
    MAX_PRODUCTO_LENGTH = 100
    
    @classmethod
    def get_config(cls):
        """Retorna la configuración como diccionario"""
        return {
            'host': cls.HOST,
            'port': cls.PORT,
            'debug': cls.DEBUG,
            'app_name': cls.APP_NAME,
            'app_version': cls.APP_VERSION,
            'app_description': cls.APP_DESCRIPTION
        }
    
    @classmethod
    def validate_venta_data(cls, producto, cantidad, precio):
        """Valida los datos de una venta"""
        errors = []
        
        if not producto or len(producto.strip()) == 0:
            errors.append("El producto es requerido")
        elif len(producto) > cls.MAX_PRODUCTO_LENGTH:
            errors.append(f"El nombre del producto no puede exceder {cls.MAX_PRODUCTO_LENGTH} caracteres")
        
        try:
            cantidad_int = int(cantidad)
            if cantidad_int < cls.MIN_CANTIDAD:
                errors.append(f"La cantidad debe ser al menos {cls.MIN_CANTIDAD}")
        except (ValueError, TypeError):
            errors.append("La cantidad debe ser un número entero válido")
        
        try:
            precio_float = float(precio)
            if precio_float < cls.MIN_PRECIO:
                errors.append(f"El precio debe ser al menos ${cls.MIN_PRECIO}")
        except (ValueError, TypeError):
            errors.append("El precio debe ser un número válido")
        
        return errors

class DevelopmentConfig(Config):
    """Configuración para desarrollo"""
    DEBUG = True
    LOG_LEVEL = "DEBUG"

class ProductionConfig(Config):
    """Configuración para producción"""
    DEBUG = False
    LOG_LEVEL = "WARNING"
    HOST = '127.0.0.1'  # Más seguro para producción

class TestingConfig(Config):
    """Configuración para testing"""
    DEBUG = True
    PORT = 5001
    LOG_LEVEL = "DEBUG"

# Configuración por defecto
config = DevelopmentConfig() 