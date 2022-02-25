from prisma import Prisma
from flask import Flask, request
from flask_restful import Api, Resource
import json
import multiprocessing
from base64 import b64encode

def gen_OWNERID():
    print(multiprocessing.cpu_count())

gen_OWNERID()

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
            return {"file": str(file.deb)}
    
    def post(self, name):
        content = request.json
        try:
            prisma.file.create(data={
                'deb': content["deb"],
                'ownerID': content["ownerID"],
                'name': name,
                'private': content["private"]
            })
            return {"done": "File added"}
        except Exception as e:
            return {"error": f"Error occured, {e}"}

api.add_resource(File, '/deb/<name>')

if __name__ == '__main__':
    app.run(port=4563, host='0.0.0.0')