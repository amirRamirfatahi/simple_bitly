class RedisMock:
    maindict: dict

    def __init__(self):
        self.maindict = dict()

    def get(self, key: str):
        return self.maindict.get(key)

    def set(self, key: str, value):
        self.maindict[key] = value

    def setnx(self, key: str, value):
        if not self.maindict.get(key):
            self.set(key, value)
            return 1
        return 0

    def expire(self, key: str, seconds: int):
        pass


def mock_start_response(status, headers):
    pass

