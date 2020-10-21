from flask import Flask, render_template
import BLL

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.errorhandler(404)
@app.errorhandler(500)
def not_found(e):
    return render_template("error/error.html")


if __name__ == '__main__':
    app.run()
