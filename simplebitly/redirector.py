from yhttp import Application, statuses

from . import db


app = Application()


@app.route('/(.*)')
def get(req, key):
    originalurl = db.redis.get(key)
    if not originalurl:
        raise statuses.notfound()

    raise statuses.found(originalurl.decode())

