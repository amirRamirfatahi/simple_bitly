from bddrest import Given, status, when, response

from simplebitly.shortener import app


def test_shortener(urandommock, redismock):
    with Given(
        app,
        'Shortening a URL',
        verb='POST',
        json=dict(url='http://example.com')
    ):
        assert status == 201
        assert response.text == 'rmXGPMVQnrKAB'

        when('URL is not valid', json=dict(url='invalidurl'))
        assert status == 400


