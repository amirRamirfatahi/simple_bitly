import os
import re
import struct
import json

from hashids import Hashids
from yhttp import Application, text, statuses

from . import db


URL_PATTERN=re.compile(
    r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}' \
    r'\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)'
)


URL_TIMETOLIVE = 48 * 3600
hashids = Hashids()
app = Application()


def getfreshid():
    randomint, = struct.unpack('L', os.urandom(8))
    return hashids.encode(randomint)


def store(url):
    while True:
        freshid = getfreshid()
        if db.redis.setnx(freshid, url):
            break

    db.redis.expire(freshid, URL_TIMETOLIVE)
    return freshid


@app.route()
@text
def post(req):
    longurl = req.form['url']
    if not URL_PATTERN.match(longurl):
        raise statuses.badrequest()

    shorturl = store(longurl)
    req.response.status = '201 Created'
    return shorturl

