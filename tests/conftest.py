import os
import string

import pytest


@pytest.fixture
def urandommock():
    backup = os.urandom
    os.urandom = lambda c: string.ascii_letters.encode()[:c]
    yield
    os.unrandom = backup


@pytest.fixture
def redismock():
    from simplebitly import db

    class RedisMock:
        maindict: dict

        def __init__(self):
            self.maindict = dict()

        def get(self, key: str):
            return self.maindict.get(key, '').encode()

        def set(self, key: str, value):
            self.maindict[key] = value

        def setnx(self, key: str, value):
            if not self.maindict.get(key):
                self.set(key, value)
                return 1
            return 0

        def expire(self, key: str, seconds: int):
            pass

    dummy = RedisMock()
    backup = db.redis
    db.redis = dummy
    yield dummy
    db.redis = backup

