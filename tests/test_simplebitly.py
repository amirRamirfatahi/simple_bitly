from unittest import TestCase, mock
import io

from tests import mocks
from simplebitly import generator, redirector
from constants import MAX_SHORTURL_LENGTH


mocked_redis = mocks.RedisMock()


def get_mocked_redis():
    return mocked_redis


@mock.patch('simplebitly.generator.redis', new_callable=get_mocked_redis)
@mock.patch('simplebitly.redirector.redis', new_callable=get_mocked_redis)
class SimplebitlyTests(TestCase):
    def setUp(self):
        pass

    def test_anyValidURL_submittedToGenerator_redirectedByRedirector(self,
                                                                     mg_redis,
                                                                     mr_redis):
        longurl = b'url=https://www.google.com'
        environ = {
            'wsgi.input': io.BytesIO(longurl),
            'CONTENT_LENGTH': len(longurl)
        }
        result = generator.generator(environ, mocks.mock_start_response)
        shorturl = result[0].decode()
        self.assertLessEqual(len(shorturl), MAX_SHORTURL_LENGTH)
        environ = {
            'PATH_INFO': f'/{shorturl}'
        }
        response = redirector.redirector(environ, mocks.mock_start_response)
        response = response[0].decode()
        self.assertEqual(response, 'OK.')
        self.assertEqual(longurl.decode()[4:], mg_redis.get(shorturl).decode())

