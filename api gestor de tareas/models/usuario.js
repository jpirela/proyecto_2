const { DataTypes } = require('sequelize');
const sequelize = require('../config/db');

const Usuario = sequelize.define('Usuario', {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true
  },
  nombre: {
    type: DataTypes.STRING(100),
    allowNull: false
  },
  email: {
    type: DataTypes.STRING(100),
    allowNull: false,
    validate: {
      isEmail: true
    }
  },
  ci: {
    type: DataTypes.STRING(10),
    allowNull: false
  },
  fecha_creacion: {
    type: DataTypes.DATE,
    defaultValue: DataTypes.NOW
  },
  contrasena:{
    type: DataTypes.STRING(100),
    allowNull: false
  }

}, {
  tableName: 'usuarios',
  timestamps: false // No usamos createdAt ni updatedAt automáticos
});

module.exports = Usuario;
