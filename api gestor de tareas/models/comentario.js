const { DataTypes } = require('sequelize');
const sequelize = require('../config/db');

const tarea = sequelize.define('tarea', {
  
  contenido: {
    type: DataTypes.TEXT,
    allowNull: false
  },
  
  tarea_id: {
  type: DataTypes.INTEGER,
  allowNull: false,
  },
  usuario_id: {
  type: DataTypes.INTEGER,
  allowNull: false,
  }

}, {
  tableName: 'comentarios',
  timestamps: false // No usamos createdAt ni updatedAt automáticos
});

module.exports = tarea;
