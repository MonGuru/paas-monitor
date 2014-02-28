from time import time

from google.appengine.api import memcache


DATA_10k = '*' * 10000
MULTI_KEYS = []
[MULTI_KEYS.append(str(x)) for x in range(1, 500)]
DATA = {}
for k in MULTI_KEYS:
    DATA[k] = '*'


def get_test():
    memcache.set('memcache_get_test', DATA_10k)
    now = time()
    memcache.get('memcache_get_test')
    result = time() - now
    memcache.delete('memcache_get_test')
    return result


def set_test():
    now = time()
    memcache.set('memcache_set_test', DATA_10k, time=30)
    result = time() - now
    memcache.delete('memcache_set_test')
    return result


def get_multi_test():

    memcache.set_multi(DATA, 30, key_prefix='memcache_get_multi_test')
    now = time()
    memcache.get_multi(MULTI_KEYS, key_prefix='memcache_get_multi_test')
    result = time() - now
    memcache.delete_multi(MULTI_KEYS, key_prefix='memcache_get_multi_test')
    return result


def set_multi_test():
    now = time()
    memcache.set_multi(DATA, 30, key_prefix='memcache_set_multi_test')
    result = time() - now
    memcache.delete_multi(MULTI_KEYS, key_prefix='memcache_set_multi_test')
    return result


def delete_multi_test():
    memcache.set_multi(DATA, 30, key_prefix='memcache_delete_multi_test')
    now = time()
    memcache.delete_multi(MULTI_KEYS, key_prefix='memcache_delete_multi_test')
    return time() - now
