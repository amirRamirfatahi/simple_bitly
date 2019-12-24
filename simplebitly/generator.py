"""
generator.py is one of the two entry points of our application.
It takes a POST request with any given valid url as request data and returns a
shorter url pointing to the original url provided by the user.
"""

import redis

from utils import isvalidurl, generate_random_shorturl
from constants import MAX_LONGURL_LENGTH, URL_TIMETOLIVE

redis = redis.Redis(host='localhost', port='6379')


def generator(environ, start_response):
    content_length = int(environ.get('CONTENT_LENGTH', MAX_LONGURL_LENGTH))
    request_body = environ.get('wsgi.input').read(content_length)
    request_body = request_body.decode()
    longurl = request_body[4:]
    if not isvalidurl(longurl):
        start_response('400', [('Content-Type', 'text/plain')])
        return [b'Invalid URL.']
    shorturl = setup_shorturl(longurl)
    start_response(
        '201',
        [('Content-Type', 'text/plain'), ('Content-Length', len(shorturl))]
    )
    return [shorturl.encode()]


def setup_shorturl(url):
    result = 0
    while result == 0:
        shorturl = generate_random_shorturl()
        result = redis.setnx(shorturl, url)
    redis.expire(shorturl, URL_TIMETOLIVE)
    return shorturl



