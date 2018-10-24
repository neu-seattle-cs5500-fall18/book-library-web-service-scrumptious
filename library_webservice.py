#!/usr/bin/env python3

from flask import Flask
#from apis import blueprint as api1
from apis import api

app = Flask(__name__)
#app.register_blueprint(api1)
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
