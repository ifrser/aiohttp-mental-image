from aiohttp import web
from functools import cached_property


class Server:
    """ Сервер для запуска приложения. """

    def __init__(self):
        self.port = 5000

    @cached_property
    def app(self):
        """ Приложение для запуска. """
        return web.Application()

    def run(self):
        """ Запустить сервер. """
        web.run_app(
            self.app,
            port=self.port
        )
