from unittest import TestCase, mock
import io

from tests import mocks
from simplebitly.generator import generator
from constants import MAX_SHORTURL_LENGTH


@mock.patch('redis.Redis', new_callable=mocks.RedisMock)
class GeneratorTests(TestCase):

    def test_AnyValidUrl_submitted_AShortUrlIsReturned(self, redis_mock):
        longurl = b'url=www.google.com'
        environ = {
            'wsgi.input': io.BytesIO(longurl),
            'CONTENT_LENGTH': len(longurl)
        }
        result = generator(environ, mocks.mock_start_response)
        shorturl = result[0].decode()
        self.assertLessEqual(len(shorturl), MAX_SHORTURL_LENGTH)
        self.assertEqual(longurl, redis_mock.get(shorturl))

    def test_AnInvalidUrl_submitted_AnErrorIsRaised(self, redis_mock):
        invalid_url = b'http://something'
        env = {
            'wsgi.input': io.BytesIO(invalid_url),
            'CONTENT_LENGTH': len(invalid_url)
        }
        result = generator(env, mocks.mock_start_response)
        errormessage = result[0].decode()
        self.assertEqual(errormessage, 'Invalid URL.')

