from aiohttp import web


async def upload(request: web.Request):
    """Сохраняем файл из запроса"""
    content = await get_file_from_request(request)
    save_as_file(content)
    return web.Response(body='upload_complete')

async def get_file_from_request(request):
    reader = await request.multipart()
    file = await reader.next()
    file_data = await file.read()
    return file_data

def save_as_file(content):
    with open(f'storage/2', 'wb') as file:
        file.write(content)