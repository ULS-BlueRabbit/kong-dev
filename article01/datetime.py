# -*- coding:utf-8 -*-

import wsgiref.simple_server
import datetime

PORT = 8000

def api_clock(environ, start_response):
    status  = "200 OK"
    headers = [
        ("Content-type", "text/plain; charset=utf-8"),
    ]
    start_response(status, headers)
    return [datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")]

server = wsgiref.simple_server.make_server("", PORT, api_clock)
print("Started on port %d" % PORT)

server.serve_forever()