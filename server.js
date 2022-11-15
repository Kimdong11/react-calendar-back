import express from 'express';
import morgan from 'morgan';
import { mohoRouter, myownhomeRouter } from './route';
const cors = require('cors');

const PORT = 5000;

const app = express();
const logger = morgan('dev');

app.use(logger);
app.use(cors());
app.use('/', mohoRouter);
app.use('/', myownhomeRouter);

const startMessage = () => {
   console.log('Server is listening On PORT Number 5000');
};

app.listen(PORT, startMessage);
