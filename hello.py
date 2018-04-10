#!/usr/bin/env pytyhon3
# -*- coding:utf-8 -*-

def application(environ, start_response):
    start_response('200 OK', [('content-Type','text/html')])
    body = '<h1>Hello, %s</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]