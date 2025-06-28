const express = require('express');
const router = express.Router();
const controlador = require('../controllers/tareasController');
const validar = require('../middlewares/validarTarea');


router.get('/', controlador.obtenerTarea);

router.post('/', validar, controlador.crearTarea);

router.get('/usuario/:idusuario', controlador.obtenerTareasporidUsuario);
router.get('/:id', controlador.obtenerTareaporid);

router.delete('/:id', controlador.eliminarTareasporid);

router.put('/:id', validar, controlador.updateTareaPorId);

module.exports = router;