from aiohttp import web


async def healthcheck(request: web.Request):
    """ Проверка доступности сервера. """
    return web.Response(body='sample response')
