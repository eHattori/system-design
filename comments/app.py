from flask import Flask, request
from pymongo import MongoClient
import os
import redis
import json
import time


app = Flask(__name__)
redis = redis.from_url(os.getenv("REDIS_URI", ""))
publisher = redis.pubsub()
subscriber = publisher.subscribe("new_comments")

@app.route('/comments', methods=['POST'])
def post():
    if request.is_json:
        comment = request.get_json()
        redis.publish("new_comments", json.dumps(comment))
    return '', 201

if __name__ == "__main__":
    client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017"))
    comments = client.mydatabase.commets
    print("Init Worker")
    while True: 
        time.sleep(1)
        comment = publisher.get_message()
        print("Waiting...")
        if comment is not None:
            print(f"Comment received: {comment}")
            comments.insert_one(comment)
   
