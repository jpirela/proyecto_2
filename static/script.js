document.addEventListener('DOMContentLoaded', () => {
  const menuSection = document.getElementById('menu-section');
  const orderList = document.querySelector('.order-items');
  const confirmBtn = document.querySelector('.order-btn');
  const editBtn = document.querySelector('.order-btn.secondary');
  const cancelBtn = document.querySelector('.order-btn.danger');
  const historialLista = document.querySelector('.pedidos-guardados');

  let pedido = [];
  let modoEditar = false;

  
  const menu = [
    { nombre: "Pasta Alfredo", descripcion: "Cremosa salsa de queso parmesano.", precio: 11.99 },
    { nombre: "Hamburguesa Clásica", descripcion: "Carne jugosa y pan artesanal.", precio: 9.99 },
    { nombre: "Tiramisú", descripcion: "Postre italiano con café y mascarpone.", precio: 6.50 },
    { nombre: "Limonada", descripcion: "Refrescante bebida natural.", precio: 3.00 },
    {nombre: "Refresco", descripcion:"Refrescante bebida gaseosa.", precio: 4.00}
  ];

  
  menu.forEach(plato => {
    const item = document.createElement('div');
    item.classList.add('item');
    item.innerHTML = `
      <h3>${plato.nombre}</h3>
      <p>${plato.descripcion}</p>
      <span class="price">$${plato.precio.toFixed(2)}</span>
      <button class="btn">Añadir al pedido</button>
    `;
    item.querySelector('button').addEventListener('click', () => {
      pedido.push({ nombre: plato.nombre, precio: plato.precio });
      actualizarPedido();
    });
    menuSection.appendChild(item);
  });

  function actualizarPedido() {
    orderList.innerHTML = '';
    if (pedido.length === 0) {
      orderList.innerHTML = '<li>No hay items en tu pedido.</li>';
      return;
    }

    pedido.forEach((item, index) => {
      const li = document.createElement('li');
      li.innerHTML = `
        ${item.nombre} <span>$${item.precio.toFixed(2)}</span>
        ${modoEditar ? '<button class="remove-btn">❌</button>' : ''}
      `;

      if (modoEditar) {
        li.querySelector('.remove-btn').addEventListener('click', () => {
          pedido.splice(index, 1);
          actualizarPedido();
        });
      }

      orderList.appendChild(li);
    });

    const total = pedido.reduce((sum, item) => sum + item.precio, 0);
    const totalLi = document.createElement('li');
    totalLi.innerHTML = `<strong>Total:</strong> <span>$${total.toFixed(2)}</span>`;
    orderList.appendChild(totalLi);
  }

  confirmBtn.addEventListener('click', () => {
    if (pedido.length === 0) {
      alert("⚠️ No hay nada que confirmar.");
      return;
    }

    const items = pedido.map(i => i.nombre);
    const total = pedido.reduce((sum, i) => sum + i.precio, 0);

    fetch('/pedido', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ items, total })
    })
    .then(res => res.json())
    .then(data => {
      alert(data.mensaje || "✅ Pedido enviado correctamente.");
      pedido = [];
      actualizarPedido();
      cargarHistorialPedidos();
    })
    .catch(() => {
      alert("❌ Error al enviar el pedido.");
    });
  });

  cancelBtn.addEventListener('click', () => {
    if (confirm("¿Seguro que quieres cancelar el pedido actual?")) {
      pedido = [];
      actualizarPedido();
    }
  });

  editBtn.addEventListener('click', () => {
    modoEditar = !modoEditar;
    editBtn.textContent = modoEditar ? "✔️ Terminar Edición" : "✏️ Editar Pedido";
    actualizarPedido();
  });

  function cargarHistorialPedidos() {
    historialLista.innerHTML = '⏳ Cargando pedidos...';

    fetch('/pedidos')
      .then(res => res.json())
      .then(data => {
        historialLista.innerHTML = '';

        if (data.length === 0) {
          historialLista.innerHTML = '<li>No hay pedidos guardados.</li>';
          return;
        }

        data.forEach(p => {
          const li = document.createElement('li');
          li.innerHTML = `
            ${p.items.join(', ')} - Total: $${p.total.toFixed(2)}
            <button class="remove-btn" data-id="${p.id}">❌</button>
          `;

          li.querySelector('.remove-btn').addEventListener('click', () => {
            if (confirm("¿Eliminar este pedido guardado?")) {
              fetch(`/pedido/${p.id}`, { method: 'DELETE' })
                .then(() => {
                  alert("🗑️ Pedido eliminado.");
                  cargarHistorialPedidos();
                });
            }
          });

          historialLista.appendChild(li);
        });
      });
  }

  cargarHistorialPedidos();
});
