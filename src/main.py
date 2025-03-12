from fastapi import FastAPI

from src.core.init_app import AppFactory

from logging import getLogger

logger = getLogger(__name__)


logger.info('main.py setuped')


app: FastAPI = AppFactory.get_app()