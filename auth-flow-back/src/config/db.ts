const mysql = require('mysql2/promise');

const dbConfig = mysql.createPool({
  host: 'localhost',
  user: 'diegus',
  password: '1358971165231sd',
  database: 'authFlow',
  waitForConnections: true,
  connectionLimit: 10,
  queueLimit: 0
});

async function getConnection() {
  try {
    const pool = await mysql.connect(dbConfig);
    return pool;
  } catch (err) {
    console.error('Error al conectar a la base de datos:', err);
    throw err;
  }
}

module.exports = {getConnection};