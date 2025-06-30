# Proyecto eEscritorio ANGEL OJEDA

Este proyecto es una recreación visual y funcional de un escritorio tipo GNOME, accesible desde el navegador web. Utiliza Python (Flask) para el backend, JavaScript para la lógica dinámica del frontend y CSS moderno para el diseño visual.

## Características principales

- **Frontend visual tipo GNOME:**
  - Fondo de pantalla moderno y responsivo.
  - Barra de búsqueda superior con diseño profesional y SVG animado.
  - Cuadrícula de iconos de aplicaciones, todos en formato SVG.
  - Dock inferior con accesos directos.
  - Iconos arrastrables por el escritorio con el mouse.
- **Backend Flask:**
  - API para servir la lista de iconos dinámicamente desde la carpeta `/frontend/icons`.
  - Poblado automático de la base de datos con los iconos SVG.
  - Servidor preparado para desarrollo local y fácil adaptación a red local o pública.
- **100% SVG:**
  - Todos los iconos son SVG para máxima calidad y compatibilidad.

## Estructura del proyecto

```
Proyecto eEscritorio ANGEL OJEDA/
├── backend/
│   ├── __init__.py
│   ├── db.py
│   ├── main.py
│   ├── models.py
│   └── templates/
│       └── index.html (vacío)
├── frontend/
│   ├── index.html
│   ├── css/
│   │   └── desktop.css
│   ├── icons/
│   │   └── *.svg
│   └── js/
│       └── (scripts opcionales)
└── requirements.txt
```

## Instalación y ejecución

1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Inicia el servidor Flask:
   ```bash
   python backend/main.py
   ```
3. Accede desde tu navegador a:
   ```
   http://localhost:5000
   ```

## Notas técnicas y desafíos

- **Integración de SVG:**
  - Fue necesario adaptar tanto el backend como el frontend para que solo se usen iconos `.svg`, evitando errores 404 por archivos `.png`.
- **Sincronización de rutas:**
  - Hubo que vaciar el `index.html` de `backend/templates` para que Flask no sirviera una versión antigua y así mostrar siempre el frontend real.
- **Arrastrar iconos:**
  - Implementar el drag & drop puro en JS, sin librerías externas, para que los iconos sean movibles y se mantenga la experiencia de escritorio.
- **Estilo visual:**
  - Se aplicó un fondo de pantalla avanzado con CSS puro y una barra de búsqueda moderna inspirada en Uiverse.io.
- **Accesibilidad en red:**
  - El proyecto puede ser adaptado para acceso en red local o pública, aunque esto requiere configuración de firewall y router.



**Este proyecto sigue en desarrollo y a la espera de modificaciones futuras...**
