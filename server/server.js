// server.js
require('dotenv').config();
const express = require('express');
const cors = require('cors');
const { Pool } = require('pg');

const app = express();
const PORT = process.env.PORT || 3000;

// Configuración de la conexión a PostgreSQL
const pool = new Pool({
  user: process.env.DB_USER,
  host: process.env.DB_HOST,
  database: 'Recetario_db',
  password: 'superusuario',
  port: process.env.DB_PORT,
});

// Middlewares
app.use(cors());
app.use(express.json());

// Rutas de la API

// Obtener todas las recetas (GET)
app.get('/api/recetas', async (req, res) => {
  try {
    const { rows } = await pool.query('SELECT * FROM recetas');
    res.json(rows);
  } catch (error) {
    console.error(error);
    res.status(500).json({detalles: error.message});
  }
});

// Agregar una nueva receta (POST)
app.post('/api/recetas', async (req, res) => {
  const { nombre, ingredientes, instrucciones } = req.body;

  if (!nombre || !ingredientes || !instrucciones) {
    return res.status(400).json({ message: 'Todos los campos son obligatorios' });
  }

  try {
    const nuevaReceta = await pool.query(
  'INSERT INTO recetas (nombre, ingredientes, instrucciones) VALUES ($1, $2, $3) RETURNING *',
  [nombre, ingredientes, instrucciones]
);
    res.status(201).json(nuevaReceta.rows[0]);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Error al guardar la receta' });
  }
});

// Iniciar el servidor
app.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
