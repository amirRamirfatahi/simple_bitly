"""
redirector.py is one of the two entry points of our application.
It takes a POST request with the previously provided shorturl from generator
and redirects to the original url
"""

from . import db


def app(environ, start_response):
    path = environ.get('PATH_INFO', '/')
    originalurl = db.redis.get(path[1:])
    if originalurl:
        start_response(
            '302 Found',
            [('Location', originalurl.decode())]
        )
        return [b'OK.']
    else:
        start_response('404 Not Found', [])
        return [b'Not Found.']
