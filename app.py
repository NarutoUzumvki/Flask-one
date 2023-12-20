from flask import Flask, request, jsonify

from db_operations import *

app = Flask(__name__)

@app.route('/')
def greet():
    return 'Hello-Highness!'

@app.route('/v1/insert', methods=['POST'])
def post():
    try:
        name = request.json['name']
        age = request.json['age']
        phone = request.json['phone']
        department = request.json['department']
        insert((name, age, phone, department))
        return f"Employee {name} added ", 200

    except Exception as error :
        return f"Could not add Employee {name} because, {error}", 400


@app.route('/v1/retrieve/<int:id>', methods=['GET'])
def get(id):
    try:
        data = retrieve(id)
        if data :
            return jsonify(data), 200
        else:
            return f"Could not Find Employee", 404

    except Exception as error:
        return f"Could not Retrieve Employee Details because, {error}", 400


@app.route('/v1/update/<int:id>', methods=['PUT'])
def put(id):
    try:
        name = request.json['name']
        age = request.json['age']
        phone = request.json['phone']
        department = request.json['department']
        update((name, age, phone, department, id))
        return f"Employee {name}'s details updated Successfully", 200
        
    except Exception as error:
        return f"Could not Update Employee Details, because {error}", 400


@app.route('/v1/remove/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        remove(id)
        return f"Employee Details for id:{id} Removed Sucessfully", 200
    except Exception as error:
        return f"Could not remove Employee because, {error}", 400


if __name__ == "__main__" :
    app.run(debug = True)