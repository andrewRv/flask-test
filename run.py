from flask import Flask, json, request
from user import User

app = Flask(__name__)


@app.route('/',  methods=['POST', 'GET'])
def hello_world():
    return 'Test'


@app.route('/save', methods=['POST', 'GET'])
def save():
    data = json.loads(request.data)
    new_user = User(data)
    new_user.save()
    return "User was saved"


@app.route('/delete', methods=['DELETE'])
def delete():
    new_user = User({"name": "Delete user", "age": "99", "address": "L A"})
    new_user.save()
    new_user.delete()
    return "User was deleted"


@app.route('/update', methods=['PUT'])
def put():
    new_user = User({"name": "Update user", "age": "99", "address": "L A"})
    data = json.loads(request.data)
    new_user.save()
    new_user.update(data)
    return "User was updated"


if __name__ == '__main__':
    app.run(debug=True)
