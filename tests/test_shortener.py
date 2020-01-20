import functools

from bddrest import Given as Given_, status, when, response

from simplebitly.shortener import app


Given = functools.partial(Given_, app)


def test_shortener(urandommock, redismock):
    with Given(
        'Shortening a URL',
        verb='POST',
        json=dict(url='http://example.com')
    ):
        assert status == 201
        assert response.text == 'rmXGPMVQnrKAB'


