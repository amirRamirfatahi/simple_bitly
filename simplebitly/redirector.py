"""
redirector.py is one of the two entry points of our application.
It takes a POST request with the previously provided shorturl from generator
and redirects to the original url
"""

import redis

from constants import MAX_LONGURL_LENGTH

redis = redis.Redis(host='localhost', port='6379')


def redirector(environ, start_response):
    path = environ.get('PATH_INFO', '/')
    originalurl = redis.get(path[1:])
    if originalurl:
        start_response(
            '302',
            [('Location', originalurl.decode())]
        )
        return [b'OK.']
    else:
        start_response('404', [])
        return [b'Not Found.']

