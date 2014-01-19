import tornado.web
import tornado.wsgi

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

application = tornado.wsgi.WSGIApplication([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    from gevent.wsgi import WSGIServer
    http_server = WSGIServer(('', 7000), application, log=None)
    http_server.serve_forever()