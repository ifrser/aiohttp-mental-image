from aiohttp import web

from sample_server.routing.healthcheck import healthcheck

routes = [
    web.get('/healthcheck', healthcheck),
    web.post('/healthcheck', healthcheck),

]
