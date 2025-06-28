const express = require('express');
const router = express.Router();
const controlador = require('../controllers/usuarioController');
const validar = require('../middlewares/validarUsuario');


router.get('/', controlador.obtenerUsuarios);


router.get('/:id', controlador.obtenerUsuariosporid);


router.post('/', validar, controlador.crearUsuario);


router.delete('/:id', controlador.eliminarUsuariosporid);


module.exports = router;
