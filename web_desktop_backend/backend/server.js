const express = require("express");
const cors = require("cors");
const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());

let datos = [];

app.post("/api/usuarios", (req, res) => {
  datos.push(req.body);
  res.json(req.body);
});

app.get("/api/usuarios", (req, res) => {
  res.json(datos);
});

app.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
});