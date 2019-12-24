from unittest import TestCase, mock
import io

from tests import mocks
from simplebitly.redirector import redirector
from constants import MAX_SHORTURL_LENGTH


@mock.patch('redis.Redis', new_callable=mocks.RedisMock)
class RedirectorTests(TestCase):

    def test_aValidShortURL_submitted_okIsReturned(self, redis_mock):
        shorturl = '/abcdefgh'
        longurl = 'www.google.com'
        environ = {
            'PATH_INFO': shorturl,
        }
        redis_mock.set(shorturl, longurl)
        result = redirector(environ, mocks.mock_start_response)
        response = result[0].decode()
        self.assertEqual(response, 'OK.')


    def test_AnInvalidShortURL_submitted_AnErrorIsReturned(self, redis_mock):
        invalid_url = '/ijkmnopq'
        env = {
            'PATH_INFO': invalid_url
        }
        result = redirector(env, mocks.mock_start_response)
        response = result[0].decode()
        self.assertEqual(response, 'Not Found.')

