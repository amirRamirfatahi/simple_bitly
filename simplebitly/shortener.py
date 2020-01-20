"""
shortener.py is one of the two entry points of our application.
It takes a POST request with any given valid url as request data and returns a
shorter url pointing to the original url provided by the user.
"""
import os
import re
import struct
import json

import redis
from hashids import Hashids


URL_PATTERN=re.compile(
    r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}' \
    r'\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)'
)


URL_TIMETOLIVE = 48 * 3600


redis = redis.Redis(host='localhost', port='6379')
hashids = Hashids()


def getfreshid():
    randomint, = struct.unpack('L', os.urandom(8))
    return hashids.encode(randomint)


def store(url):
    while True:
        freshid = getfreshid()
        if redis.setnx(freshid, url):
            break

    redis.expire(freshid, URL_TIMETOLIVE)
    return freshid


def app(environ, start_response):
    request_body = json.load(environ.get('wsgi.input', ''))
    longurl = request_body.get('url', '')

    if not URL_PATTERN.match(longurl):
        start_response('400 Bad Request', [('Content-Type', 'text/plain')])
        return [b'Invalid URL.']

    shorturl = store(longurl)
    start_response(
        '201 Created',
        [('Content-Type', 'text/plain'),
         ('Content-Length', str(len(shorturl)))]
    )
    return [shorturl.encode()]

