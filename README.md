Página Web del Calendario de Fórmula 1

Este proyecto es una página web básica en HTML con estilos CSS, diseñada para mostrar información sobre la Fórmula 1. Utiliza HTMX para la carga dinámica de contenido en diferentes secciones del sitio sin necesidad de recargar la página completa.

Características

    Menú de Navegación: Una barra de navegación horizontal permite a los usuarios alternar entre diferentes vistas relacionadas con la F1:

        Pilotos

        Equipos

        Carreras

        Campeonato de Pilotos

        Campeonato de Constructores

    Información de la Próxima Carrera: Muestra detalles sobre la siguiente carrera de Fórmula 1, incluyendo:

        Nombre de la Carrera (ej. "España")

        Fecha y Hora

        Mejor tiempo de vuelta del circuito y el piloto que lo logró

        Nombre de la Pista

Tecnologías Utilizadas

    HTML5: Para la estructura de la página web.

    CSS3: Para los estilos y el diseño.

    HTMX: Una librería JavaScript pequeña y moderna que permite acceder a AJAX, transiciones CSS, WebSockets y Server Sent Events directamente en HTML, utilizando atributos. En este proyecto, se usa para intercambiar contenido en el div con id="content" (que, aunque no está presente en el HTML proporcionado, se asume para el contenido dinámico).

Cómo Funciona

Los enlaces de navegación están configurados con los atributos hx-get y hx-target. Cuando se hace clic en un enlace, HTMX envía una solicitud AJAX a la URL especificada en hx-get (por ejemplo, /pilotos). La respuesta de esa solicitud se inserta entonces en el elemento identificado por hx-target.

El contenido estático actual en la página muestra información sobre la "Próxima Carrera", codificada directamente en el HTML.

Configuración y Uso

Para ejecutar este proyecto:

    Guarda el código HTML como index.html.

    Guarda el código CSS como styles.css en el mismo directorio.

    Abre index.html en tu navegador web.
