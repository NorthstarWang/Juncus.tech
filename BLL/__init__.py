from app import *
from flask import render_template


@app.route('/Earthquake', methods=['POST', 'GET'])
def calc_earthquake():
    return render_template('calculator/Earthquake.html')


@app.route('/Decibel', methods=['POST', 'GET'])
def calc_decibel():
    return render_template('calculator/Decibel.html')
