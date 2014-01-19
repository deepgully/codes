from flask import Flask
import logging
app = Flask(__name__)

logging.disable(logging.CRITICAL)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    from gevent.wsgi import WSGIServer
    http_server = WSGIServer(('', 7000), app, log=None)
    http_server.serve_forever()