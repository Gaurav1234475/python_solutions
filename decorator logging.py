import logging

logger = logging.getLogger(__name__)
def logging_decorator(fn):
    def func(*a, **kw):
        logger.info('%s(%s, %s)', fn, a, kw)
        return fn(*a, **kw)
    return func