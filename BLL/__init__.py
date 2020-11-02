from app import app
from flask import render_template


@app.route('/Calculator/<string:subject>/<string:filename>')
def calculator(subject, filename):
    path = "calculator/" + subject + "/" + filename
    return render_template(path)
