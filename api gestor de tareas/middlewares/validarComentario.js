module.exports = (req, res, next) => {
  const { contenido, usuario_id, tarea_id} = req.body;

  if (!contenido || contenido.length < 3) {
    return res.status(400).json({ error: 'titulo inválido' });
  }

  if (!usuario_id || usuario_id<1 ) {
    return res.status(400).json({ error: 'id de usuario invalido' });
  }

  if (!tarea_id || tarea_id<1 ) {
    return res.status(400).json({ error: 'id de usuario invalido' });
  }
  
  
  next();
};
