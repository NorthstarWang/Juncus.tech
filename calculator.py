import math
from flask import Flask, render_template, request

from app import app


@app.route('/Calculator/<string:subject>/<string:file>')
def calculator(subject, file):
    path = "calculator/" + subject + "/" + file
    return render_template(path)


@app.route('/Api/MHF4U/Earthquake/Intensity', methods=['POST'])
def earthquake_intensity_calculation():
    M1 = float(request.form['magnitude1'])
    M2 = float(request.form['magnitude2'])
    decimal = int(request.form['decimal'])
    if 0 <= M1 <= 10 and 0 <= M2 <= 10:
        difference = M1-M2
        text = 'Earthquake 1 is ' + str(round(math.pow(10, difference), decimal)) + ' times as intense as earthquake 2.'
        return text
    else:
        return str('Please type in correct value range from 0 to 10!')


@app.route('/Api/MHF4U/Earthquake/Energy', methods=['POST'])
def earthquake_energy_calculation():
    ME = str(request.form['ME'])
    if ME == 'energy':
        E = float(request.form['energy'])
        U = str(request.form['unit'])
        if U == 'J':
            mag = round((math.log10(E)-4.8)/1.5,1)
            if mag < 0:
                return 'This level of energy is not able to produce a standard earthquake on richter scale.'
            else:
                return str(E) + ' Joules is equivalent to magnitude of ' + str(mag)
        elif U == 'KJ':
            mag = round((math.log10(1000*E) - 4.8) / 1.5, 1)
            if mag < 0:
                return 'This level of energy is not able to produce a standard earthquake on richter scale.'
            else:
                return str(E) + ' KJ is equivalent to magnitude of ' + str(mag)
        elif U == 'MJ':
            mag = round((math.log10(1000000*E) - 4.8) / 1.5, 1)
            if mag < 0:
                return 'This level of energy is not able to produce a standard earthquake on richter scale.'
            else:
                return str(E) + ' MJ is equivalent to magnitude of ' + str(mag)
        elif U == 'GJ':
            mag = round((math.log10(1000000000 * E) - 4.8) / 1.5, 1)
            if mag < 0:
                return 'This level of energy is not able to produce a standard earthquake on richter scale.'
            else:
                return str(E) + ' GJ is equivalent to magnitude of ' + str(mag)
        elif U == 'TJ':
            mag = round((math.log10(1000000000000 * E) - 4.8) / 1.5, 1)
            if mag < 0:
                return 'This level of energy is not able to produce a standard earthquake on richter scale.'
            else:
                return str(E) + ' TJ is equivalent to magnitude of ' + str(mag)
        elif U == 'PJ':
            mag = round((math.log10(1000000000000000 * E) - 4.8) / 1.5, 1)
            if mag < 0:
                return 'This level of energy is not able to produce a standard earthquake on richter scale.'
            else:
                return str(E) + ' PJ is equivalent to magnitude of ' + str(mag)
        elif U == 'EJ':
            mag = round((math.log10(1000000000000000000 * E) - 4.8) / 1.5, 1)
            if mag < 0:
                return 'This level of energy is not able to produce a standard earthquake on richter scale.'
            else:
                return str(E) + ' EJ is equivalent to magnitude of ' + str(mag)
    elif ME == 'magnitude':
        M = float(request.form['magnitude'])
        E = round(pow(10,(4.8+1.5*M)),6)
        return "The magnitude will produce " + '{:.6e}'.format(E) + " Joules of energy."

