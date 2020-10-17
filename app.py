import string
import math
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/Calculator/<string:subject>/<string:file>')
def calculator(subject, file):
    path = "calculator/" + subject + "/" + file
    return render_template(path)


@app.route('/Api/MHF4U/Earthquake/Intensity', methods=['POST'])
def intensityCalculation1():
    M1 = float(request.form['magnitude1'])
    M2 = float(request.form['magnitude2'])
    decimal = int(request.form['decimal'])
    if 0 <= M1 <= 10 and 0 <= M2 <= 10:
        difference = M1-M2
        text = 'Earthquake 1 is ' + str(round(math.pow(10, difference), decimal)) + ' times as intense as earthquake 2.'
        return text
    else:
        return str('Please type in correct value range from 0 to 10!')


@app.errorhandler(404)
@app.errorhandler(500)
def not_found(e):
    return render_template("error/error.html")


if __name__ == '__main__':
    app.run()
