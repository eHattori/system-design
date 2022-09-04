import sys
sys.path.append("../tax")

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from tax import TaxClient
import os
import redis
import json

db = SQLAlchemy()
cache = redis.from_url(os.getenv("REDIS_URI", ""))
tax_service = TaxClient()

def get_from_cache(pattern):
    result = []
    for key in cache.keys(pattern):
        obj = cache.get(key.decode("utf-8"))
        result.append(json.loads(obj))

    return result


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    db.init_app(app)
    migrate = Migrate(app, db)

    return app
