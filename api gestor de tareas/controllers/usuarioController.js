const Usuario = require('../models/usuario');

exports.crearUsuario = async (req, res) => {
  try {
    const nuevo = await Usuario.create(req.body);
    res.status(201).json(nuevo);
  } catch (error) {
    res.status(500).json({ error: 'Error al crear usuario', detalles: error.message });
  }
};

exports.obtenerUsuariosporid = async (req, res) => {
  try {
    const usuario = await Usuario.findByPk(req.params.id);
    console.log(req.params.id);

    if (usuario) {
      return res.status(200).json(usuario);
    } else {
      return res.status(404).json({ error: 'No se encontró usuario' });
    }
  } catch (error) {
    res.status(500).json({ error: 'Error al obtener usuario', detalles: error.message });
  }
};


exports.obtenerUsuarios = async (req, res) => {
  try {
    const lista = await Usuario.findAll();

    if (lista.length<1){
        res.status(404).json({ error: 'No se encontraron usuarios' });
    }else{
    res.json(lista);
    }
  } catch (error) {
    res.status(500).json({ error: 'Error al obtener usuarios' });
  }
};

exports.eliminarUsuariosporid = async (req, res) => {
  try {
    const usuario = await Usuario.findByPk(req.params.id);
    console.log(req.params.id);
    if (usuario) {
        await usuario.destroy(); // Borra esa tupla directamente
         res.status(200).json({ mensaje: 'Usuario eliminado correctamente' });
    }else{
        res.status(404).json({ error: 'No se encontro usuario' });
    }
    
    
  } catch (error) {
    res.status(500).json({ error: 'Error al obtener usuarios' });
  }
};
