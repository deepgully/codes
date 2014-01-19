from eurasia import httpserver


def handler(http):
    http.start_response('200 OK', [('Content-Type', 'text/html')])
    http.write('<html>Hello world</html>')
    http.close()

server = httpserver('0.0.0.0:7000', handler)
server.serve_forever()