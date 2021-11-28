from aiohttp import web

from sample_server.routing.healthcheck import healthcheck
from sample_server.routing.upload import upload
from sample_server.routing.home import home

routes = [
    web.get('/healthcheck', healthcheck),
    web.post('/healthcheck', healthcheck),
    web.post('/upload', upload),
    web.get('/home', home),
]
