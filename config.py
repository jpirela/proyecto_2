"""
Configuraciones de la aplicación de Registro de Alumnos
"""

class Config:
    """Configuración base de la aplicación"""
    
    # Configuraciones del servidor
    HOST = '127.0.0.1'
    PORT = 5000
    DEBUG = True
    
    # Configuraciones de la aplicación
    APP_NAME = 'Registro de Alumnos'
    APP_VERSION = '1.0.0'
    
    # Configuraciones de la base de datos (para futuras implementaciones)
    DATABASE_URL = None
    
    # Configuraciones de seguridad
    SECRET_KEY = 'tu_clave_secreta_aqui_cambiala_en_produccion'
    
    # Configuraciones de logging
    LOG_LEVEL = 'INFO'
    LOG_FILE = 'app.log'

class DevelopmentConfig(Config):
    """Configuración para desarrollo"""
    DEBUG = True
    LOG_LEVEL = 'DEBUG'

class ProductionConfig(Config):
    """Configuración para producción"""
    DEBUG = False
    HOST = '0.0.0.0'
    LOG_LEVEL = 'WARNING'

# Configuración por defecto
config = DevelopmentConfig() 