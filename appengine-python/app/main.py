
import webapp2


import settings
from views import *

urls = (
    ('/memcache/get', MemcacheGet),
    ('/memcache/set', MemcacheSet),
    ('/memcache/get_multi', MemcacheGetMulti),
    ('/memcache/set_multi', MemcacheSetMulti),
    ('/memcache/delete_multi', MemcacheDeleteMulti),
    ('/datastore/get', DataStoreGet),
    ('/datastore/put', DataStorePut),
    ('/datastore/update', DataStoreUpdate),
    ('/datastore/delete', DataStoreDelete),
    ('/datastore/query', DataStoreQuery),
    ('/environment/dynamicget', DynamicGet),
    ('/environment/cpufibonacci', CpuFibonacci),
    #('/images/', Images),
    #('/urlfetch/', Urlfetch),
    #('/users/', Users),
)


app = webapp2.WSGIApplication(urls, debug=settings.DEBUG)
