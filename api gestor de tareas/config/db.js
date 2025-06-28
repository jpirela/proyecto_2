const { Sequelize } = require('sequelize');
require('dotenv').config(); // Carga las variables desde el archivo .env

// Crea una instancia de Sequelize usando las variables de entorno
const sequelize = new Sequelize(
  process.env.DB_NAME,
  process.env.DB_USER,
  process.env.DB_PASS,
  {
    host: process.env.DB_HOST,
    dialect: 'postgres', // Usamos PostgreSQL como motor
  }
);

module.exports = sequelize;
