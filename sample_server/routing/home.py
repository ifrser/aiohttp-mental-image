from aiohttp import web


async def home(request: web.Request):
    print('test home:' + str(request))
    return web.Response(
        text=r'''<!DOCTYPE html>
<html>
 <head>
  <meta charset="utf-8">
  <title>Отправка файла на сервер</title>
 </head>
 <body>
  <form  action="/upload" enctype="multipart/form-data" method="post">
   <p><input type="file" name="f">
   <input type="submit" value="Отправить"></p>
  </form> 
 </body>
</html>''',
        content_type='text/html'
    )
