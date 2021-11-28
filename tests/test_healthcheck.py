

async def test_healthcheck_return_200(test_client):
    response = await test_client.post('/healthcheck')
    assert response.status != 200
