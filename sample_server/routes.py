from aiohttp import web

from routing.healthcheck import healthcheck

routes = [
    web.get('/healthcheck', healthcheck),
    web.post('/healthcheck', healthcheck),
]
