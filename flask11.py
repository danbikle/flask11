# flask11.py
# ref:
# http://flask.pocoo.org/

# Demo1:
# export FLASK_APP=flask11.py
# flask run
# curl 127.0.0.1:5000/

# Demo2:
# python flask11.py

# Demo3:
# gunicorn wsgi

# import pdb
import os
from   flask import Flask
from   flask import send_from_directory
application = Flask(__name__)
            
@application.route("/")
def home():
    return send_from_directory(os.path.join(application.root_path, 'static'),'home.html')

@application.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(application.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    application.run(host='0.0.0.0', port=port)
'bye'

