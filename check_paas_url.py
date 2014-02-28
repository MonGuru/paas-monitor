#!/usr/bin/env python

import sys

import requests


def check(host, uri, warn, critical):
    request = requests.get('http://%s%s' % (host, uri))
    if not request.status_code == 200:
        print "Error: http://%s/%s received %s code" % (host, uri,
                request.status_code)
        sys.exit(-1)
    try:
        output = request.json()
    except ValueError:
        msg = "- error trying to check - got invalid response"
        msg = "CRITICAL %s" % msg
        exit_code = 2
        return exit_code, msg

    response_time = output['time']
    check_name = output['check_name']
    msg = "- %s in %s second" % (check_name, response_time)
    if response_time >= float(critical):
        msg = "CRITICAL %s" % msg
        exit_code = 2
    elif response_time >= float(warn):
        msg = "WARNING %s" % msg
        exit_code = 1
    else:
        exit_code = 0
        msg = "OK %s" % msg

    return exit_code, msg


if __name__ == '__main__':

    try:
        host = sys.argv[1]
        uri = sys.argv[2]
        warn = float(sys.argv[3])
        critical = float(sys.argv[4])
    except IndexError:
        print "Usage: check_paas_by_url host uri warn critical"
        print "Ex: check_paas_by_url python-monitor.appspot.com /memcache/get 0.008 0.01"
        sys.exit(-1)
    exit_code, output_msg = check(host, uri, warn, critical)
    print output_msg
    sys.exit(exit_code)
