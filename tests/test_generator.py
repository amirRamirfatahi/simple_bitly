import io
import json
from bddrest.authoring import Given, when, response, status
from tests import mocks
from simplebitly.generator import generator
from constants import MAX_SHORTURL_LENGTH


class TestGenerator:

    def test_generator(self, mocker):
        longurl = {"url": "https://www.google.com"}
        invalid_url = {"url": "http://something"}

        environ = {
            'wsgi.input': io.BytesIO(json.dumps(longurl).encode()),
        }
        mocked_redis = mocker.patch('simplebitly.generator.redis',
                                    new_callable=mocks.RedisMock)
        call = {
            "title": "short URL generation",
            "verb": "POST",
            "json": longurl
        }
        with Given(generator, **call) as story:
            shorturl = response.body.decode()
            assert len(shorturl) == MAX_SHORTURL_LENGTH
            assert longurl.get('url') ==  mocked_redis.get(shorturl).decode()
            assert status == '201 Created'

            when('Trying an invalid URL', json=invalid_url)

            errormessage = response.body.decode()
            assert status == '400 Bad Request'
            assert errormessage == 'Invalid URL.'

