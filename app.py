from flask import Flask, render_template
from flask_compress import Compress
from flask_squeeze import Squeeze
from flask_socketio import SocketIO

app = Flask(__name__)
app.config["COMPRESS_REGISTER"] = False  # disable default compression of all eligible requests
squeeze = Squeeze()
squeeze.init_app(app)
compress = Compress()
compress.init_app(app)
socketio = SocketIO()
socketio.init_app(app)

import BLL


@app.route('/')
@compress.compressed()
def index():
    return render_template("index.html")


@app.errorhandler(404)
@app.errorhandler(500)
@compress.compressed()
def not_found(e):
    return render_template("error/error.html")


if __name__ == '__main__':
    app.run(debug=False)
