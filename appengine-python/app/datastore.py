import random
import string

from time import time


DATA_2k = '*' * 2000
from google.appengine.ext import db


class DSTest(db.Model):
    data = db.TextProperty()


def get_test():
    entity = DSTest(data=DATA_2k)
    key = entity.put()
    now = time()
    db.get(key)
    result = time() - now
    db.delete(key)
    return result


def put_test():
    entity = DSTest(data=DATA_2k)
    now = time()
    key = entity.put()
    result = time() - now
    db.delete(key)
    return result


def update_test():
    entity = DSTest(data=DATA_2k)
    key = entity.put()

    @db.transactional
    def _real_update_test(key):
        now = time()
        entity = db.get(key)
        entity.data += '*'
        key = entity.put()
        result = time() - now
        db.delete(key)
        return result

    return _real_update_test(key)


def delete_test():
    entity = DSTest(data=DATA_2k)
    key = entity.put()
    now = time()
    db.delete(key)
    return time() - now


def query_test():
    my_string = ''.join(random.choice(string.ascii_uppercase +
                            string.digits) for x in range(10))
    entity = DSTest(data=my_string)
    key = entity.put()
    now = time()
    DSTest.all().filter('data', my_string).fetch(1)
    result = time() - now
    db.delete(key)
    return result
