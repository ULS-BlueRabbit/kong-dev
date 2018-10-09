# -*- coding:utf-8 -*-
import wsgiref.simple_server
import uuid

PORT = 8000
ALLOWED_METHOD_LIST = ['GET']
ALLOWED_PATH = '/macaddress'

def get_macaddress():
    return uuid.uuid1().hex[-12:]

def api(environ, start_response):
    method  = environ['REQUEST_METHOD']
    path    = environ['PATH_INFO']
    headers = [('Content-Type', 'text/plain; charset=utf-8')]
    body    = ''
    if method not in ALLOWED_METHOD_LIST:
        status  = '400 Bad Request'
    elif path != ALLOWED_PATH:
        status  = '404 Not Found'
    else:
        status  = '200 OK'
        body    = get_macaddress()
    start_response(status, headers)
    return [body]

def main():
    httpd = wsgiref.simple_server.make_server('', PORT, api)
    print("Micro Service on port %s" % PORT)
    httpd.serve_forever()

if __name__ == '__main__':
    main()