from unittest import TestCase, mock
import io

from tests import mocks
from simplebitly.generator import generator
from constants import MAX_SHORTURL_LENGTH


@mock.patch('simplebitly.generator.redis', new_callable=mocks.RedisMock)
class GeneratorTests(TestCase):

    def test_anyValidURL_submitted_aShortURLIsReturned(self, redis_mock):
        longurl = b'url=https://www.google.com'
        environ = {
            'wsgi.input': io.BytesIO(longurl),
            'CONTENT_LENGTH': len(longurl)
        }
        result = generator(environ, mocks.mock_start_response)
        shorturl = result[0].decode()
        self.assertLessEqual(len(shorturl), MAX_SHORTURL_LENGTH)
        self.assertEqual(longurl.decode()[4:],
                         redis_mock.get(shorturl).decode())

    def test_anInvalidUrl_submitted_anErrorIsRaised(self, redis_mock):
        invalid_url = b'http://something'
        env = {
            'wsgi.input': io.BytesIO(invalid_url),
            'CONTENT_LENGTH': len(invalid_url)
        }
        result = generator(env, mocks.mock_start_response)
        errormessage = result[0].decode()
        self.assertEqual(errormessage, 'Invalid URL.')
