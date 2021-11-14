from aiohttp import web
from functools import cached_property

from routes import routes


class Server:
    """ Сервер для запуска приложения. """

    def __init__(self):
        self.port = 5000

    @cached_property
    def app(self):
        """ Приложение для запуска. """
        app = web.Application()
        app.add_routes(routes)
        return app

    def run(self):
        """ Запустить сервер. """
        web.run_app(
            self.app,
            port=self.port
        )
