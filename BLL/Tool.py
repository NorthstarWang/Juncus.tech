import json

import requests
import html5lib

from bs4 import BeautifulSoup

from flask import request, jsonify

from app import app, socketio
from flask_socketio import emit, disconnect


def generateFormData(data, curr, total):
    curr += 1
    remain = total-curr
    form_data = {}
    for question in data:
        new_entry = question['entry'][:-9]
        if question['type'] == 'radio':
            for index, num in enumerate(question['number']):
                if num != 0:
                    question['number'][index] -= 1
                    form_data[new_entry] = question['options'][index]
                    break
                else:
                    continue
        elif question['type'] == 'checkbox':
            available_options = 0
            remain_total = 0
            for num in question['number']:
                if num != 0:
                    available_options += 1
                    remain_total += num
            if remain == remain_total:
                for index, num in enumerate(question['number']):
                    if num != 0:
                        question['number'][index] -= 1
                        form_data[new_entry] = question['options'][index]
                        break
                    else:
                        continue
            elif remain > remain_total + available_options:
                options = []
                for index, num in enumerate(question['number']):
                    if num != 0:
                        question['number'][index] -= 1
                        options.append(question['options'][index])
                form_data[new_entry] = options
            else:
                remain -= remain_total
                options = []
                for index, num in enumerate(question['number']):
                    if num != 0 and remain != 0:
                        question['number'][index] -= 1
                        remain -= 1
                        options.append(question['options'][index])
                    elif remain == 0:
                        break
                form_data[new_entry] = options
    return [form_data, data]


def analyse_types(string):
    if string.find("Checkbox") != -1:
        return "checkbox"
    elif string.find("Radio") != -1 or string.find("Scale") != -1:
        return "radio"


def generate_form_info_viewform(string, types, entry):
    info_array = json.loads(list_decode(string))
    unsorted_options = info_array[4][0][1]
    sorted_options = []
    initial_option_num = []
    for opts in unsorted_options:
        if opts[0]:
            sorted_options.append(opts[0])
            initial_option_num.append(0)
    form_section = {
        "type": types,
        "entry": entry,
        "title": info_array[1],
        "options": sorted_options,
        "number": initial_option_num,
        "status": 0,
    }
    return form_section


def list_decode(string):
    string = string[4:-1]
    index = string.rfind(']')
    new_str = string[:index + 1]
    return new_str


@app.route('/Api/tool/Form/Get', methods=['Get', 'Post'])
def get_form():
    url = str(request.form['url'])
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
               'Accept - Language': 'zh - CN, zh;q = 0.8, en - US;q = 0.5, en;q = 0.3',
               }
    if url[-8:] == "viewform" and url.find('docs.google.com/forms/d/') != -1:
        response = requests.get(url, headers=headers).text
        soup = BeautifulSoup(response, 'html5lib')
        total_list = []
        status = True
        for segment in soup.find_all("div", "freebirdFormviewerViewNumberedItemContainer"):
            try:
                info_list = segment.find(attrs={"class": "m2"})['data-params']
                tag = analyse_types(segment.contents[0].contents[0].contents[1]['class'][-1])
                entry = segment.contents[0].contents[0].contents[1].find('input')['name']
            except[BaseException]:
                status = False
                break
            else:
                total_list.append(generate_form_info_viewform(info_list, tag, entry))
        if status:
            return jsonify({"valid": True, "list": total_list})
        else:
            return jsonify({"valid": False})
    else:
        return jsonify({"valid": False})


@socketio.on('submit_connect')
def submit_form(array):
    questions = array['data']['questions']
    url = array['data']['url']
    url = url[:-8]+'formResponse'
    total = array['data']['total']
    emit('message', 'Processing...\nPlease do not close this window until submissions are done.')
    for curr_num in range(int(total)):
        try:
            data = generateFormData(questions, curr_num, int(total))
            questions = data[1]
            requests.post(url, data=data[0])
            emit('message', 'Submitting ' + str(curr_num + 1) + ' form')
        except:
            emit('message', 'Failure on ' + str(curr_num + 1) + ' form')
            continue
    emit('message', 'Submissions are Done!')
    disconnect()
