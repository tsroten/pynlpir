"""Utility functions for PyNLPIR unit tests."""

import functools
from threading import Thread


def timeout(timeout):
    """Executes a function call or times out after *timeout* seconds.

    Inspired by: http://stackoverflow.com/a/21861599.

    Example:
    func = timeout(timeout=1)(open)
    try:
        func('test.txt')
    except RuntimeError:
        print('open() timed out.')
    """
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = [RuntimeError('function {0} timeout'.format(func.__name__))]

            def newFunc():
                try:
                    res[0] = func(*args, **kwargs)
                except RuntimeError as e:
                    res[0] = e

            t = Thread(target=newFunc)
            t.daemon = True
            try:
                t.start()
                t.join(timeout)
            except Exception as je:
                print('Error starting thread')
                raise je
            ret = res[0]
            if isinstance(ret, BaseException):
                raise ret
            return ret
        return wrapper
    return deco
