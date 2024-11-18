#json:
#{
# "id": 123,
# "name": "Arabika"
# "price": "100.25"
# }
import csv

from bottle import response
from flask import Flask, request, abort, jsonify
from flask_restful import Api, Resource
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()
USER_DATA = {
    "Username": "password"
}

#HTTP Basic
@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password

class endpoint(Resource):
    @auth.login_required
    def get(self):
        return jsonify({"status":True})

api.add_resource(endpoint,"/endpoint")

# GET handling
@app.route('/items', methods=['GET'])
def get_handler():
    #if 'Content-Type' not in request.headers:
    #   abort(400,"Content-Type is not specified")
    #if request.headers['Content-Type'] != "application/json":
    #    abort(400)
    ###
    response_data = read_catalog()

    print(response_data)
    return response_data

# POST handling
@app.route('/items', methods=['POST'])
def post_handler():
    # Application "Content-Type: application/json", if no -> return 400
    if request.headers['Content-Type'] != "application/json":
        abort(400)



    #JSON structure validation -> fits, no "id" field in it
    print(request.json['name'])
    print(request.json['price'])

    print(type(request.json['name']))
    print(type(request.json['price']))

    if save_data(request.json):
        return "Catalog entry was recorded",201


    return "ok",200

def read_catalog():
    #file = open("catalog.txt", 'r')
    response_list = []
    #for row in file.readline():
    #  print(row.split(","))
    #   #response_dict['id'] = row.split(',')[0]
    #   # response_dict['name'] = row.split(',')[1]
    #   # response_dict['price'] = row.split(',')[2]
    #
    #file_content = file.read()
    #file.close()
    with open("catalog.txt") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        print(reader)
        for item in reader:
            print(item)
            response_dict = {}
            response_dict['id'] = item[0]
            response_dict['name'] = item[1]
            response_dict['price'] = item[2]
            response_list.append(response_dict)
    return response_list

def save_data(post_data):
    # Data store logic
    file = open("catalog.txt", 'a')
    data_to_write = "1," + post_data['name'] + "," + str(post_data['price']) + "\n"
    file.write(data_to_write)
    file.close()
    return True


if __name__ == '__main__':
     app.run(debug=True)
     app.run(port=5000, debug=True)

