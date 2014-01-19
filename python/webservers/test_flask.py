from flask import Flask
import logging
app = Flask(__name__)

logging.disable(logging.CRITICAL)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)