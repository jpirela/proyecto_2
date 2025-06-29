import "reflect-metadata";

import app from './app';

const port = 3000;

app.listen(port, () => {
	console.log(`Servidor - http://localhost:${port}/api/`);
});