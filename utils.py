from urllib.parse import urlparse
import random
import time

from constants import CHARSET


def isvalidurl(url):
    try:
        parts = urlparse(url)
        if all([parts.scheme, parts.netloc]):
            return True
    except ValueError:
        pass
    return False


def generate_random_string(length):
    return ''.join(random.choice(CHARSET) for _ in range(length))


def get_date_prefix():
    yearday = time.localtime().tm_yday
    return '{firstchar}{secondchar}'.format(
        firstchar=CHARSET[int(yearday / len(CHARSET))],
        secondchar=CHARSET[int(yearday % len(CHARSET))]
    )


def generate_random_shorturl():
    return '{prefix}{randompart}'.format(
        prefix=get_date_prefix(),
        randompart=generate_random_string(6)
    )

