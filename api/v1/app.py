#!/usr/bin/python3
"""app.py file"""
from models import storage
from flask import Flask, Blueprint, jsonify
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def app_teardown(error):
    """
    Method that calls storage.close
    """
    storage.close()

if __name__ == '__main__':
    """
    Setting host and port
    """
    host = os.getenv("HBNB_API_HOST", default='0.0.0.0')
    ports = int(os.getenv("HBNB_API_PORT", default=5000))
    app.run(host=hosts, port=ports, threaded=True)
