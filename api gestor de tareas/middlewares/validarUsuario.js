module.exports = (req, res, next) => {
  const { nombre, email, ci } = req.body;

  if (!nombre || nombre.length < 3) {
    return res.status(400).json({ error: 'Nombre inválido' });
  }

  if (!email || !email.includes('@')) {
    return res.status(400).json({ error: 'Email inválido' });
  }

  if (!ci || ci.length < 6 || ci.length > 10) {
    return res.status(400).json({ error: 'Cédula inválida' });
  }

  next();
};
