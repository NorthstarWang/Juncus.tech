import string

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/Calculator/<string:subject>/<string:file>')
def calculator(subject, file):
    path = "calculator/" + subject + "/" + file
    return render_template(path)


@app.errorhandler(404)
@app.errorhandler(500)
def not_found(e):
    return render_template("error/error.html")


if __name__ == '__main__':
    app.run()
