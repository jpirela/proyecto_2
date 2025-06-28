const express = require('express');
const app = express();
const sequelize = require('./config/db');
const usuarioRoutes = require('./routes/usuarioRoutes');
const tareaRoutes = require('./routes/tareaRoutes');
const comentarioRoutes = require('./routes/comentarioRoutes');
const swagger = require('./swagger/swagger');
const cors = require('cors');
app.use(cors());
app.use(express.json());
app.use('/usuarios', usuarioRoutes);
app.use('/tareas', tareaRoutes);
app.use('/comentarios', comentarioRoutes);
swagger(app);

sequelize.sync().then(() => {
  app.listen(3000, () => {
    console.log('🚀 Servidor corriendo en http://localhost:3000');
    console.log('📘 Documentación Swagger en http://localhost:3000/api-docs');
  });
});
