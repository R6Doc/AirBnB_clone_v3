#!/usr/bin/python3
"""runs the application API
    """
from flask import Flask, Blueprint, jsonify
from models import storage
from api.v1.views import app_views
import os
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.errorhandler(404)
def page_not_found(error):
    """handles the error page"""
    return (jsonify({"error": "Not found"}), 404)


@app.teardown_appcontext
def closeteardown(exception):
    """close storage"""
    storage.close()

if __name__ == "__main__":
    app.run(
        host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
        port=os.getenv('HBNB_API_PORT', '5000'),
        threaded=True)
