import express from "express";
import cors from "cors";
import routes from "./src/modules";


const app = express();

app.disable('x-powered-by');

app.use(express.json({'limit':'5mb'}));
app.use(express.urlencoded({ extended: true }));

app.use(cors({
  origin: '*',
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
}));

app.use('/api', routes);

app.get('/status', function(_, res) {
  res.status(200).send('OK');
});

export default app;
