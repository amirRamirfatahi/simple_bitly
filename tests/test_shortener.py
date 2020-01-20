from bddrest import Given, status, when, response, given

from simplebitly.shortener import app


def test_shortener_json(urandommock, redismock):
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

        when('URL field is missing', json=given - 'url')
        assert status == '400 Field missing: url'


def test_shortener_urlencoded(urandommock, redismock):
    with Given(
        app,
        'Shortening a URL',
        verb='POST',
        form=dict(url='http://example.com')
    ):
        assert status == 201
        assert response.text == 'rmXGPMVQnrKAB'


def test_shortener_multipart(urandommock, redismock):
    with Given(
        app,
        'Shortening a URL',
        verb='POST',
        multipart=dict(url='http://example.com')
    ):
        assert status == 201
        assert response.text == 'rmXGPMVQnrKAB'


