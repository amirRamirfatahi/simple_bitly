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
    """
    Generates a 2-length string from the current day of the year.
    e.g. 213th day of year for a charset of lowercase ascii letters excluding
    the lowercase "l"
    int(213 / 25) = 8 ==> charset[8] = i
    int(213 % 25) = 13 ==> charset[13] = n
    so this will return "in" for 213th day of the year
    """
    yearday = time.localtime().tm_yday
    return '{firstchar}{secondchar}'.format(
        firstchar=CHARSET[int(yearday / len(CHARSET))],
        secondchar=CHARSET[int(yearday % len(CHARSET))]
    )


def generate_random_shorturl():
    """
    creates a random 8-length string using the day of the year prefix and a
    randomly generated 6-length string
    """
    return '{prefix}{randompart}'.format(
        prefix=get_date_prefix(),
        randompart=generate_random_string(6)
    )
