from api.v1.views import app_views
from flask import jsonify
from models.misc import classes
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """ Returns the status of server """
    return jsonify({
        "status": "OK"
        })

@app_views.route('/stats', methods=['GET'])
def stat():
    """ Returns amount of objects in storage """
    return jsonify({
        k: storage.count(v) for k, v in classes.items()
    })
