# coding: utf-8

import logging
import json
import traceback
from time import time

from webapp2 import RequestHandler

import memcache
import datastore
import environment

class BaseView(RequestHandler):
    def get(self):

        self.response.headers["Cache-Control"] = "no-cache"
        self.response.headers["Content-Type"] = "application/json"
        try:
            return self._get()
        except Exception, e:
            logging.error('Can not do it: %s %s' % (str(e),
                traceback.format_exc()))
            return self.response.out.write('')


class MemcacheGet(BaseView):
    def _get(self):
        response = {}
        response['check_name'] = 'memcache_get_test'
        response['time'] = memcache.get_test()
        return self.response.out.write(json.dumps(response))


class MemcacheSet(BaseView):
    def _get(self):
        response = {}
        response['check_name'] = 'memcache_set_test'
        response['time'] = memcache.set_test()
        return self.response.out.write(json.dumps(response))


class MemcacheGetMulti(BaseView):
    def _get(self):
        response = {}
        response['check_name'] = 'memcache_get_multi_test'
        response['time'] = memcache.get_multi_test()
        return self.response.out.write(json.dumps(response))


class MemcacheSetMulti(BaseView):
    def _get(self):
        response = {}
        response['check_name'] = 'memcache_set_multi_test'
        response['time'] = memcache.set_multi_test()
        return self.response.out.write(json.dumps(response))


class MemcacheDeleteMulti(BaseView):
    def _get(self):
        response = {}
        response['check_name'] = 'memcache_delete_multi_test'
        response['time'] = memcache.delete_multi_test()
        return self.response.out.write(json.dumps(response))



class DataStoreGet(BaseView):
    def _get(self):
        response = {}
        response['check_name'] = 'datastore_get_test'
        response['time'] = datastore.get_test()
        return self.response.out.write(json.dumps(response))


class DataStorePut(BaseView):
    def _get(self):
        response = {}
        response['check_name'] = 'datastore_put_test'
        response['time'] = datastore.put_test()
        return self.response.out.write(json.dumps(response))


class DataStoreUpdate(BaseView):
    def _get(self):
        response = {}
        response['check_name'] = 'datastore_update_test'
        response['time'] = datastore.update_test()
        return self.response.out.write(json.dumps(response))


class DataStoreDelete(BaseView):
    def _get(self):
        response = {}
        response['check_name'] = 'datastore_delete_test'
        response['time'] = datastore.delete_test()
        return self.response.out.write(json.dumps(response))


class DataStoreQuery(BaseView):
    def _get(self):
        response = {}
        response['check_name'] = 'datastore_query_test'
        response['time'] = datastore.query_test()
        return self.response.out.write(json.dumps(response))

class DynamicGet(BaseView):
    def _get(self):
        response = {}
        response['check_name'] = 'dynamic_get_test'
        data = environment.dynamic_get_test()
        return self.response.out.write(data)

class CpuFibonacci(BaseView):
    def _get(self):
        response = {}
        response['check_name'] = 'cpu_fibonacci_test'
        now = time()
        environment.cpu_fibonacci_test()
        response['time'] = time() - now
        return self.response.out.write(json.dumps(response))

class TaskAddOne(BaseView):
    def _get(self):
        response = {}
        response['check_name'] = 'task_add_one_test'
        response['time'] = tasks.add_one()
        return self.response.out.write(json.dumps(response))
