const express = require('express');
const router = express.Router();
const controlador = require('../controllers/comentariosController');
const validar = require('../middlewares/validarComentario');

router.get('/:id', controlador.obtenerComentariosporid);

router.delete('/:id', controlador.eliminarComentariosporid);

router.get('/', controlador.obtenerComentario);

router.post('/', validar, controlador.crearComentario);
router.put('/:id', validar, controlador.updateComentarioporid);

module.exports = router;