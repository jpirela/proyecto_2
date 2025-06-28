const comentarios = require('../models/comentario');

exports.crearComentario = async (req, res) => {
  try {
    const nuevo = await comentarios.create(req.body);
    res.status(201).json(nuevo);
  } catch (error) {
    res.status(500).json({ error: 'Error al crear el comentario', detalles: error.message });
  }
};

exports.obtenerComentario = async (req, res) => {
  try {
    const lista = await comentarios.findAll();

    if (lista.length<1){
        res.status(404).json({ error: 'No se encontraron comentarios' });
    }else{
    res.json(lista);
    }
  } catch (error) {
    res.status(500).json({ error: 'Error al obtener comentario' });
  }
};

exports.eliminarComentariosporid = async (req, res) => {
  try {
    const comentario = await comentarios.findByPk(req.params.id);
    console.log(req.params.id);
    if (comentario) {
        await comentario.destroy(); // Borra esa tupla directamente
         res.status(200).json({ mensaje: 'comentario eliminada correctamente' });
    }else{
        res.status(404).json({ error: 'No se encontro comentario' });
    }
    
    
  } catch (error) {
    res.status(500).json({ error: 'Error al obtener comentarios' });
  }
};

exports.obtenerComentariosporid = async (req, res) => {
  try {
    const comentario = await comentarios.findByPk(req.params.id);
    console.log(req.params.id);

    if (comentario) {
      return res.status(200).json(comentario);
    } else {
      return res.status(404).json({ error: 'No se encontró el comentario' });
    }
  } catch (error) {
    res.status(500).json({ error: 'Error al obtener comentario', detalles: error.message });
  }
};

exports.updateComentarioporid = async (req, res) => {
  try {
    const comentarioExistente = await comentarios.findByPk(req.params.id);

    if (!comentarioExistente) {
      return res.status(404).json({ error: 'No se encontró el comentario' });
    }

    // Validación básica: asegurarse de que los campos obligatorios estén presentes
    const { contenido, tarea_id, usuario_id } = req.body;

    if (!contenido || !tarea_id || !usuario_id) {
      return res.status(400).json({ error: 'Faltan campos obligatorios: contenido, tareaid o usuarioId' });
    }

    await comentarios.update(
      { contenido, tarea_id, usuario_id },
      { where: { id: req.params.id } }
    );

    const comentarioActualizado = await comentarios.findByPk(req.params.id);
    return res.status(200).json(comentarioActualizado);

  } catch (error) {
    res.status(500).json({ error: 'Error al reemplazar el comentario', detalles: error.message });
  }
};
