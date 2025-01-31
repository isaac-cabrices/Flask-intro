from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
    data = json.load(f)

@app.route('/')
def hello_world():
    return 'Hello, World!'  # return 'Hello World' in response

@app.route('/students')
def get_students():
    result = []
    pref = request.args.get('pref')
    if pref:
        for student in data:
            if student['pref'] == pref:
                result.append(student)
        return jsonify(result)
    return jsonify(data) #returns student data in response

@app.route('/students/<id>')
def get_student(id):
    for student in data:
        if student['id'] == id:
            return jsonify(student)

@app.route('/stats')
def get_stats():
    stats_dict = {}
    for student in data:
        st_pref = student['pref']
        st_prog = student['programme']
        if st_pref in stats_dict:
            stats_dict[st_pref] += 1
        else:
            stats_dict[st_pref] = 1
        if st_prog in stats_dict:
            stats_dict[st_prog] += 1
        else:
            stats_dict[st_prog] = 1
    return jsonify(stats_dict)

app.run(host='0.0.0.0', port=8080, debug=True)
