from time import time

from google.appengine.ext import ndb, deffered
from google.appengine.api import taskqueue, memcache


PAYLOAD_10K = '*' * 10000


class TaskModel(ndb.Model):
    inserted = ndb.DateTimeProperty(auto_now_add=True)


def add_one(key_name):
    task = taskqueue.Task(payload=PAYLOAD_10K, url='/task_tests/task_one')
    now = time()
    task.add()
    return time() - now


def add_ten(key_name):
    task = taskqueue.Task(payload=PAYLOAD_10K, url='/task_tests/task_ten')
    now = time()
    task.add()
    return time() - now


def set_executon_latency(timestamp):
    return memcache.set('task_execution_time', time() - timestamp, time=86400)


def execution_latency(key_name):
    deffered.defer(set_executon_latency, time())
    return memcache.get('task_execution_time')
