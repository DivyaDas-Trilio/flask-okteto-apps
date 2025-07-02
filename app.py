from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)
mongo_uri = os.getenv("MONGO_URI", "mongodb://mongo:27017/")
client = MongoClient(mongo_uri)
db = client.okteto

@app.route('/')
def hello():
    count = db.visits.count_documents({})
    db.visits.insert_one({})
    return f"Hello from Flask in Okteto! Visits: {count + 1}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

