import aiohttp


async def test_upload_(test_client):
    with open('tests/test_file') as file:
        root = aiohttp.FormData()
        root.add_field('file', file)
        response = await test_client.post('/upload', data=root)
        assert response.status != 200

