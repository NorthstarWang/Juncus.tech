import math

from flask import request

from app import app


@app.route('/Api/tool/Form/Get', methods=['Get', 'Post'])
def get_form():
    return 0
