
import express from 'express';
import * as auth from './auth.controller';

const router = express.Router();

// Routes for authentication
router.post('/signup', auth.registerUser);
router.post('/login', auth.setLogin);

export default router;
