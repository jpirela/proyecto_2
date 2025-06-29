// app.js
const API_URL = 'http://localhost:3000/api/recetas'; // URL de tu API backend

const formulario = document.getElementById('formulario-receta');
const listaRecetas = document.getElementById('lista-recetas');

// Cargar y mostrar las recetas existentes
async function cargarRecetas() {
    try {
        const respuesta = await fetch(API_URL);
        if (!respuesta.ok) throw new Error('Error en la respuesta de la red');
        
        const recetas = await respuesta.json();
        listaRecetas.innerHTML = '';

        if (recetas.length === 0) {
            listaRecetas.innerHTML = '<p>No hay recetas guardadas todavía. ¡Agrega una!</p>';
            return;
        }

        recetas.forEach(receta => {
            const elementoReceta = document.createElement('div');
            elementoReceta.classList.add('receta');
            elementoReceta.innerHTML = `
                <h3>${receta.nombre}</h3>
                <h4>Ingredientes:</h4>
                <p>${receta.ingredientes.replace(/\n/g, '<br>')}</p>
                <h4>Instrucciones:</h4>
                <p>${receta.instrucciones.replace(/\n/g, '<br>')}</p>
            `;
            listaRecetas.appendChild(elementoReceta);
        });

    } catch (error) {
        console.error('Error al cargar las recetas:', error);
        listaRecetas.innerHTML = '<p>No se pudieron cargar las recetas. Intenta de nuevo más tarde.</p>';
    }
}

// Manejar el envío del formulario para agregar una nueva receta
formulario.addEventListener('submit', async function(evento) {
    evento.preventDefault(); // Evita que la página se recargue

    const nombre = document.getElementById('nombre').value;
    const ingredientes = document.getElementById('ingredientes').value;
    const instrucciones = document.getElementById('instrucciones').value;

    const nuevaReceta = { nombre, ingredientes, instrucciones };

    try {
        const respuesta = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(nuevaReceta),
        });

        if (!respuesta.ok) throw new Error('Error al guardar la receta.');

        formulario.reset(); // Limpiar el formulario
        await cargarRecetas(); // Recargar la lista de recetas

    } catch (error) {
        console.error('Error al enviar el formulario:', error);
        alert('No se pudo guardar la receta.');
    }
});

// Cargar las recetas cuando la página se carga por primera vez
document.addEventListener('DOMContentLoaded', cargarRecetas);
