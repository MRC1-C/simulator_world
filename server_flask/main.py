import codecs
from flask import Flask
import uuid
import gridfs
import matplotlib as plt
import pymongo
from flask import jsonify
from flask_cors import CORS


client = pymongo.MongoClient('mongodb+srv://CJ:1234@cluster0.uuqiy.mongodb.net/?retryWrites=true&w=majority')
db = client.test_database
gridfs_fs = gridfs.GridFS(db)
app = Flask(__name__)
CORS(app)


@app.route("/create_population", methods=['GET'])
def create_population():
    return str(uuid.uuid4())

@app.route("/get_images", methods=['GET'])
def get_images():
    img = gridfs_fs.get_last_version(filename= 140340396186192)
    base64_data = codecs.encode(img.read(), 'base64')
    image = base64_data.decode('utf-8')
    print(type(image))
    return jsonify({"image": image}),200