from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from logging import getLogger
from src.routers import main_router


logger = getLogger(__name__)


class AppFactory:
    @staticmethod
    def get_app() -> FastAPI:
        logger.info('app setup is started')
        app = FastAPI()

        origins: list[str] = ['http://0.0.0.0:8000']

        app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*'],
        )

        app.include_router(main_router)
        logger.info('app setup is finished')
        return app
