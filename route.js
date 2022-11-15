import { Router } from 'express';
import { handleMohoRouter, handleMyOwnHomeRouter } from './controller';

export const mohoRouter = Router();
export const myownhomeRouter = Router();

mohoRouter.get('/moho', handleMohoRouter);
myownhomeRouter.get('/myownhome', handleMyOwnHomeRouter);
