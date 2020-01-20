from bddrest import Given, status, when, response

from simplebitly.redirector import app


def test_redirector(redismock):
    redismock.set('foo', 'https://example.com')
    with Given(
        app,
        'Redirect a short url',
        '/foo'
    ):
        print(response.text)
        assert status == 302
        assert response.headers['LOCATION'] == 'https://example.com'

        when('URL does not exist', '/notexists')
        assert status == 404

