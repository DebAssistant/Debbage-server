from prisma import Prisma
from flask import Flask
from flask_restful import Api, Resource
import json

prisma = Prisma()
app = Flask(__name__)
api = Api(app)

@app.before_first_request
def startup():
    prisma.connect()

class File(Resource):
    def get(self, name):
        file = prisma.file.find_first(where={'name': name})
        if file == None:
            return {"error": "Not Found"}
        else:
            return {"file": file.deb}

api.add_resource(File, '/deb/<name>')

if __name__ == '__main__':
    app.run(port=4563, host='0.0.0.0')