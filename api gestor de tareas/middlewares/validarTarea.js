module.exports = (req, res, next) => {
  const { titulo, prioridad, estado , descripcion, usuario_id} = req.body;

  if (!titulo || titulo.length < 3) {
    return res.status(400).json({ error: 'titulo inválido' });
  }

  if (!prioridad || prioridad<1 || prioridad>5) {
    return res.status(400).json({ error: 'la prioridad debe ser entre 1 y 5' });
  }

 if (!estado || !["pendiente", "en progreso", "completada"].includes(estado)) {
  return res.status(400).json({ error: 'estado inválido' });
}


  if (!descripcion || descripcion.length < 3) {
    return res.status(400).json({ error: 'descripcion invalida' });
  }

  if (!usuario_id || usuario_id<1 ) {
    return res.status(400).json({ error: 'id de usuario invalido' });
  }


  next();
};
