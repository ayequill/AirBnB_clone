#!/usr/env python
""" Entry point """
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(error):
    if error:
        print(error)
    storage.close()
    
@app.errorhandler(404)
def error_page(error):
    """ Custom error json """
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    from os import getenv
    host = getenv('HBNB_API_HOST') or '0.0.0.0'
    port = int(getenv('HBNB_API_PORT')) or 5000
    
    app.run(host=host, port=port, threaded=True)
