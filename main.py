#!/usr/bin/env python3
"""
Punto de entrada principal para la aplicación de Registro de Alumnos
"""

try:
    from backend import RegistroAlumnosApp
except ImportError as e:
    print(f"Error al importar el backend: {e}")
    print("Asegúrate de que el archivo backend.py esté en el mismo directorio")
    exit(1)

def main():
    """Función principal que inicia la aplicación"""
    try:
        print("Iniciando aplicación de Registro de Alumnos...")
        print("Accede a http://127.0.0.1:5000 en tu navegador")
        print("Presiona Ctrl+C para detener la aplicación")
        
        app = RegistroAlumnosApp()
        app.run(debug=True, host='127.0.0.1', port=5000)
        
    except KeyboardInterrupt:
        print("\nAplicación detenida por el usuario")
    except Exception as e:
        print(f"Error al iniciar la aplicación: {e}")
        exit(1)

if __name__ == '__main__':
    main() 