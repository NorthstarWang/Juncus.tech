import BLL.Logarithm
import BLL.Tool
from app import *


@app.route('/calculator/Earthquake', methods=['POST', 'GET'])
@compress.compressed()
def calc_earthquake():
    return render_template('calculator/Earthquake.html')


@app.route('/calculator/Decibel', methods=['POST', 'GET'])
@compress.compressed()
def calc_decibel():
    return render_template('calculator/Decibel.html')


@app.route('/tool/Form', methods=['POST', 'GET'])
@compress.compressed()
def tool_form():
    return render_template('tool/Form.html')


