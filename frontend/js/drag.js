// drag.js
// Arrastrar y soltar real para los íconos del escritorio
// Menú contextual básico y selección de íconos

document.addEventListener('DOMContentLoaded', () => {
    const icons = document.querySelectorAll('.icon');
    let dragged = null;
    let offsetX = 0;
    let offsetY = 0;

    icons.forEach(icon => {
        icon.addEventListener('mousedown', (e) => {
            if (e.button === 2) return; // botón derecho: menú contextual
            dragged = icon;
            offsetX = e.offsetX;
            offsetY = e.offsetY;
            icon.style.zIndex = 1000;
            icon.classList.add('selected');
        });
        icon.addEventListener('contextmenu', (e) => {
            e.preventDefault();
            showContextMenu(e.pageX, e.pageY, icon);
        });
    });

    document.addEventListener('mousemove', (e) => {
        if (dragged) {
            dragged.style.position = 'absolute';
            dragged.style.left = (e.pageX - offsetX) + 'px';
            dragged.style.top = (e.pageY - offsetY) + 'px';
        }
    });

    document.addEventListener('mouseup', () => {
        if (dragged) {
            dragged.style.zIndex = '';
            dragged.classList.remove('selected');
            dragged = null;
        }
    });

    // Menú contextual básico
    function showContextMenu(x, y, icon) {
        let menu = document.getElementById('contextMenu');
        if (!menu) {
            menu = document.createElement('div');
            menu.id = 'contextMenu';
            menu.style.position = 'absolute';
            menu.style.background = 'rgba(40,40,40,0.97)';
            menu.style.color = '#fff';
            menu.style.borderRadius = '8px';
            menu.style.boxShadow = '0 2px 12px #0007';
            menu.style.padding = '8px 0';
            menu.style.zIndex = 9999;
            menu.innerHTML = '<div style="padding:8px 24px;cursor:pointer;">Abrir</div>' +
                             '<div style="padding:8px 24px;cursor:pointer;">Propiedades</div>';
            document.body.appendChild(menu);
        }
        menu.style.left = x + 'px';
        menu.style.top = y + 'px';
        menu.style.display = 'block';
        // Cerrar menú al hacer click fuera
        setTimeout(() => {
            document.addEventListener('click', closeMenu, { once: true });
        }, 10);
        function closeMenu() { menu.style.display = 'none'; }
    }
});
