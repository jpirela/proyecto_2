const { DataTypes } = require('sequelize');
const sequelize = require('../config/db');

const tarea = sequelize.define('tarea', {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true
  },
  titulo: {
    type: DataTypes.STRING(100),
    allowNull: false
  },
  descripcion: {
    type: DataTypes.TEXT,
    allowNull: false
  },
  prioridad: {
    type: DataTypes.INTEGER,
    allowNull: true,
    validate: {
      min: 1,
      max: 5
    },
    comment: '1: baja, 5: alta'
  },
  estado: {
    type: DataTypes.STRING(50),
    allowNull: false,
    validate: {
      isIn: [['pendiente', 'en progreso', 'completada']]
    },
  },
  fecha_tope: {
  type: DataTypes.DATEONLY, // Guarda solo la fecha (sin hora)
  allowNull: true
  },
  usuario_id: {
  type: DataTypes.INTEGER,
  allowNull: false,
  }
}, {
  tableName: 'tareas',
  timestamps: false // No usamos createdAt ni updatedAt automáticos
});

module.exports = tarea;
