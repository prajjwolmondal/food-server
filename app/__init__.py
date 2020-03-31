import os

from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config["DEBUG"] = True

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'

    return app