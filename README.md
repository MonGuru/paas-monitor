

Alternative way to monitor PaaS provider such as Google AppEngine,
Heroku, Meteor and others.

The idea is to provide an interface to already working apps on these
providers with your favorite monitoring software.

Take a look at [mongu.ru nagios](http://paas.mongu.ru/cgi-bin/nagios3/status.cgi?host=all) to see an example of an AppEngine app using it.


The way it works is really simple:

The "module" should be plugable to any app, and provide a set of URLs so
the monitoring software can GET it and parses the result.

The output for the GET should as bellow:

{
    'check_name': '*the_name_of_the_test*',
    'time': float_seconds_that_took_to_run,
}

Something like this:
{
    'check_name': 'memcache_get_test',
    'time': 0.00445985794067,
}


check_paas_url.py is nagios plugin that can be used to consume the
module output.

Ex. 
check_paas_by_url python-monitor.appspot.com /memcache/get 0.008 0.01
