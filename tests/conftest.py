import pytest

from sample_server.server import Server


@pytest.fixture()
def test_client(aiohttp_client, loop):

    app = Server().app
    return loop.run_until_complete(aiohttp_client(app))
