from flask import Flask, request

my_app = Flask(__name__)


@my_app.route("/", methods=["GET"])
def hello():
    return "Hello world!"


@my_app.route("/postman", methods=["POST"])
def mirror_data():
    print("here")
    data = request.get_json()
    print(data)
    return data


my_app.run()