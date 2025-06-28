const tarea = require('../models/tareas');

exports.crearTarea = async (req, res) => {
  try {
    const nuevo = await tarea.create(req.body);
    res.status(201).json(nuevo);
  } catch (error) {
    res.status(500).json({ error: 'Error al crear tarea', detalles: error.message });
  }
};

exports.obtenerTarea = async (req, res) => {
  try {
    const lista = await tarea.findAll();

    if (lista.length<1){
        res.status(404).json({ error: 'No se encontraron tarea' });
    }else{
    res.json(lista);
    }
  } catch (error) {
    res.status(500).json({ error: 'Error al obtener tarea' });
  }
};

exports.eliminarTareasporid = async (req, res) => {
  try {
    const tareas = await tarea.findByPk(req.params.id);
    console.log(req.params.id);
    if (tareas) {
        await tareas.destroy(); // Borra esa tupla directamente
         res.status(200).json({ mensaje: 'tarea eliminada correctamente' });
    }else{
        res.status(404).json({ error: 'No se encontro tarea' });
    }
    
    
  } catch (error) {
    res.status(500).json({ error: 'Error al obtener usuarios' });
  }
};

exports.obtenerTareasporidUsuario = async (req, res) => {
  try {
    const tareas = await tarea.findAll({
      where: { usuario_id: req.params.idusuario }
    });

    if (tareas.length > 0) {
      return res.status(200).json(tareas);
    } else {
      return res.status(404).json({ error: 'No se encontraron tareas para este usuario' });
    }
  } catch (error) {
    res.status(500).json({ error: 'Error al obtener tareas', detalles: error.message });
  }
};

exports.obtenerTareaporid = async (req, res) => {
  try {
    const tareaEncontrada = await tarea.findByPk(req.params.id);

    if (!tareaEncontrada) {
      return res.status(404).json({ error: 'No se encontró la tarea' });
    }

    return res.status(200).json(tareaEncontrada);
  } catch (error) {
    res.status(500).json({ error: 'Error al obtener la tarea', detalles: error.message });
  }
};




exports.updateTareaPorId = async (req, res) => {
  try {
    const tareaExistente = await tarea.findByPk(req.params.id);

    if (!tareaExistente) {
      return res.status(404).json({ error: 'No se encontró la tarea' });
    }

    const {
      titulo,
      descripcion,
      prioridad,
      estado,
      fecha_tope,
      usuario_id
    } = req.body;

    // Validar campos obligatorios
    if (!titulo || !descripcion || !estado || usuario_id === undefined) {
      return res.status(400).json({
        error: 'Faltan campos obligatorios: titulo, descripcion, estado o usuario_id'
      });
    }

        // Actualizar directamente sobre la instancia encontrada
    await tareaExistente.update({
      titulo,
      descripcion,
      prioridad,
      estado,
      fecha_tope,
      usuario_id
    });

    return res.status(200).json(tareaExistente);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Error al actualizar la tarea', detalles: error.message });
  }
};

