#!/usr/bin/python3
""" Flask framework for rest API"""


from flask  import Flask, jsonify
from models import storage
from os import getenv
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)
#app.url_map.strict_slashes = False

@app.teardown_appcontext
def teardown(self):
    """Handles appcontext"""
    storage.close()

@app.errorhandler(404)
def page_not_found(error):
    """Returns a render template"""
    return jsonify(error='Not found'), 404

if __name__ == "__main__":
    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
