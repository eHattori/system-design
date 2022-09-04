
from . import db, cache, get_from_cache
import json


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    value = db.Column(db.Float)
    tax = db.Column(db.Float)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "value": self.value,
            "tax": self.tax
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    @staticmethod
    def get_all():
        cache_users = get_from_cache(f"products:*:*")
        return Product.query.all() if cache_users == [] else cache_users

    def create(self):
        db.session.add(self)
        db.session.commit()
        cache.set(f'products:{self.id}:{self.description}', json.dumps(self.to_dict()))
