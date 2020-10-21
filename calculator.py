import math
from flask import Flask, render_template, request

from app import app


@app.route('/Calculator/<string:subject>/<string:filename>')
def calculator(subject, filename):
    path = "calculator/" + subject + "/" + filename
    return render_template(path)


@app.route('/Api/MHF4U/Earthquake/Intensity', methods=['POST'])
def earthquake_intensity_calculation():
    M1 = float(request.form['magnitude1'])
    M2 = float(request.form['magnitude2'])
    decimal = int(request.form['decimal'])
    if 0 <= M1 <= 10 and 0 <= M2 <= 10:
        difference = M1 - M2
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
            mag = round((math.log10(E) - 4.8) / 1.5, 1)
            if mag < 0:
                return 'This level of energy is not able to produce a standard earthquake on richter scale.'
            else:
                return str(E) + ' Joules is equivalent to magnitude of ' + str(mag)
        elif U == 'KJ':
            mag = round((math.log10(1000 * E) - 4.8) / 1.5, 1)
            if mag < 0:
                return 'This level of energy is not able to produce a standard earthquake on richter scale.'
            else:
                return str(E) + ' KJ is equivalent to magnitude of ' + str(mag)
        elif U == 'MJ':
            mag = round((math.log10(1000000 * E) - 4.8) / 1.5, 1)
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
        E = round(pow(10, (4.8 + 1.5 * M)), 6)
        return "The magnitude will produce " + '{:.6e}'.format(E) + " Joules of energy."


@app.route('/Api/MHF4U/Decibel/EnergyFlux', methods=['POST'])
def decibel_energy_flux_calculation():
    decibel = float(request.form['decibel'])
    decimal = int(request.form['decimal1'])
    result_round = float(pow(10, decibel / 10) * pow(10, -12))
    result = round(result_round, decimal)
    first = 'The intensity level '
    last = ' in Watts Per Meter Square.'
    if result_round < 0.0001:
        text = 'The sound is too soft to produce an energy flux, try larger decibel!'
        return text
    else:
        text = first + str(decibel) + ' have an intensity of ' + str(result) + last
        return text


@app.route('/Api/MHF4U/Decibel/Intensity', methods=['POST'])
def decibel_intensity_calculation():
    D1 = float(request.form['decibel1'])
    D2 = float(request.form['decibel2'])
    decimal = int(request.form['decimal2'])
    result = round(pow(10, (D1-D2)/10), decimal)
    return 'Decibel 1 has an intensity ' + str(result) + ' times as great as Decibel 2'

