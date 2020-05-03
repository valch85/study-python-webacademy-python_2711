# !/usr/bin/env python3
import logging
from functools import wraps

def logs(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        logger = logging.getLogger()
        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        logger.debug(func.__name__ + " function was called")
        logger.info('So should this')
        logger.warning('And this, too')
        return func(*args, **kwargs)
    return with_logging

@logs
def summ(x):
    return x + x


print(summ(3))


#f = open(LOG_FILENAME, 'rt')
#try:
#    body = f.read()
#finally:
#    f.close()
#
#print('FILE:')
#print(body)