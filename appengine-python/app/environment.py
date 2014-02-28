from time import time

from google.appengine.api import memcache


DATA_100k = '*' * 100000

def dynamic_get_test():
    return DATA_100K


def cpu_fibonacci_test(n=25):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return cpu_fibonacci_test(n-1) + cpu_fibonacci_test(n-2)
