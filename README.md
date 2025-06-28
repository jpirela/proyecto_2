# 📊 Sistema de Registro de Ventas

Una aplicación web moderna y elegante para gestionar y controlar las ventas de tu negocio. Desarrollada con Python Flask y una interfaz de usuario moderna, con arquitectura modular separando backend y frontend.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)
![Arquitectura](https://img.shields.io/badge/Arquitectura-Modular-orange.svg)

## 🏗️ Arquitectura del Proyecto

### **Estructura Modular**
```
registro-ventas/
├── app.py                 # Aplicación principal (coordinador)
├── backend.py            # Lógica de negocio y datos
├── frontend.py           # Interfaz de usuario y templates
├── config.py             # Configuración centralizada
├── Registro Ventas.py    # Archivo principal (compatibilidad)
├── README.md             # Documentación
└── get-pip.py           # Instalador de pip (opcional)
```

### **Separación de Responsabilidades**
- **`backend.py`**: Gestión de datos, lógica de negocio, validaciones
- **`frontend.py`**: Interfaz de usuario, estilos, JavaScript
- **`app.py`**: Coordinación, rutas API, configuración Flask
- **`config.py`**: Configuración centralizada y validaciones

## ✨ Características

### 🎨 **Diseño Moderno**
- Interfaz de usuario elegante con gradientes y animaciones
- Diseño completamente responsivo (móvil, tablet, desktop)
- Tipografía moderna (Inter) y iconos Font Awesome
- Colores profesionales y consistentes

### 📈 **Funcionalidades Principales**
- **Registro de Ventas**: Agregar productos, cantidades y precios
- **Panel de Estadísticas**: Métricas en tiempo real
  - Total de ventas registradas
  - Total de productos vendidos
  - Ingresos totales
- **Lista de Ventas**: Visualización clara de todas las transacciones
- **Cálculos Automáticos**: Total por venta calculado automáticamente
- **Eliminación de Ventas**: Borrar ventas individuales o todas

### 🚀 **Experiencia de Usuario**
- Formulario intuitivo con validación
- Mensajes de confirmación al registrar ventas
- Estado vacío informativo
- Animaciones suaves y feedback visual
- Interfaz en español

### 🔧 **Arquitectura Técnica**
- **Backend Modular**: Clase `VentasBackend` para lógica de negocio
- **Frontend Separado**: Clase `VentasFrontend` para interfaz
- **API REST**: Endpoints bien definidos
- **Configuración Centralizada**: Sistema de configuración flexible
- **Validación Robusta**: Validación de datos en múltiples niveles

## 🛠️ Requisitos del Sistema

- **Python**: 3.7 o superior
- **Flask**: Framework web
- **Navegador web**: Chrome, Firefox, Safari, Edge

## 📦 Instalación

### 1. Clonar o Descargar el Proyecto
```bash
# Si tienes Git instalado
git clone <url-del-repositorio>
cd registro-ventas

# O simplemente descarga los archivos
```

### 2. Instalar Dependencias
```bash
# Usando pip
pip install flask

# O usando py (Windows)
py -m pip install flask
```

### 3. Ejecutar la Aplicación

#### Opción A: Usando la nueva arquitectura modular
```bash
# Archivo principal modular
python app.py

# O usando py (Windows)
py app.py
```

#### Opción B: Usando el archivo de compatibilidad
```bash
# Archivo original (mantiene compatibilidad)
python "Registro Ventas.py"

# O usando py (Windows)
py "Registro Ventas.py"
```

### 4. Acceder a la Aplicación
Abre tu navegador web y visita:
```
http://localhost:5000
```

## 🎯 Cómo Usar

### Registrando una Nueva Venta

1. **Abrir la aplicación** en tu navegador
2. **Completar el formulario**:
   - **Producto**: Nombre del producto vendido
   - **Cantidad**: Número de unidades vendidas
   - **Precio Unitario**: Precio por unidad
3. **Hacer clic en "Registrar Venta"**
4. **Verificar** que aparece el mensaje de confirmación

### Visualizando Estadísticas

- **Panel superior**: Muestra métricas en tiempo real
- **Lista de ventas**: Todas las transacciones registradas
- **Totales**: Calculados automáticamente por venta

### Gestionando Ventas

- **Eliminar venta individual**: Botón "Eliminar" en cada venta
- **Limpiar todas las ventas**: Botón "Limpiar Todo" en la barra de acciones

## 🔧 API Endpoints

### Rutas Principales
- `GET /` - Página principal de la aplicación
- `GET /ventas` - Obtener todas las ventas
- `POST /ventas` - Crear nueva venta
- `DELETE /ventas/<id>` - Eliminar venta específica
- `DELETE /ventas/limpiar` - Eliminar todas las ventas

### Rutas Adicionales
- `GET /estadisticas` - Obtener estadísticas de ventas
- `GET /ventas/buscar/<id>` - Buscar venta específica
- `GET /ventas/producto/<nombre>` - Obtener ventas por producto
- `GET /api/health` - Estado del servidor

## 🎨 Características del Diseño

### Paleta de Colores
- **Primario**: Azul/Púrpura (#4f46e5, #7c3aed)
- **Secundario**: Verde (#10b981, #059669)
- **Neutros**: Grises (#f8fafc, #e2e8f0, #6b7280)

### Componentes
- **Header**: Gradiente con título y descripción
- **Formulario**: Campos estilizados con iconos
- **Estadísticas**: Tarjetas con métricas importantes
- **Lista de Ventas**: Items con hover effects

## 📱 Compatibilidad

- ✅ **Desktop**: Windows, macOS, Linux
- ✅ **Tablet**: iPad, Android tablets
- ✅ **Móvil**: iPhone, Android phones
- ✅ **Navegadores**: Chrome, Firefox, Safari, Edge

## 🔄 Funcionalidades Futuras

- [ ] Persistencia de datos (base de datos SQLite/PostgreSQL)
- [ ] Exportación de reportes (PDF, Excel)
- [ ] Filtros y búsqueda avanzada de ventas
- [ ] Gráficos y análisis estadísticos
- [ ] Sistema de usuarios y autenticación
- [ ] Backup automático de datos
- [ ] API REST completa con documentación
- [ ] Tests unitarios y de integración

## 🐛 Solución de Problemas

### Error: "Flask no está instalado"
```bash
pip install flask
# o
py -m pip install flask
```

### Error: "Puerto 5000 en uso"
La aplicación se ejecutará en el puerto 5000 por defecto. Si está ocupado, modifica `config.py`:
```python
PORT = 5001  # Cambia el puerto
```

### Error: "Python no reconocido"
Asegúrate de que Python esté instalado y en el PATH del sistema.

### Error: "Módulos no encontrados"
Si usas la arquitectura modular, asegúrate de que todos los archivos estén en el mismo directorio:
- `app.py`
- `backend.py`
- `frontend.py`
- `config.py`

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 👨‍💻 Autor

Desarrollado como una aplicación de gestión de ventas moderna y funcional con arquitectura modular.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

---

⭐ **¡Si te gusta este proyecto, dale una estrella!** 