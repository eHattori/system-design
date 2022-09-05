from flask import request
from .models import Product
from . import create_app, cache, get_from_cache, tax_service
import json

app = create_app()

@app.route('/products')
def get():
    return {"products": Product.get_all()}, 200

@app.route('/products', methods=['POST'])
def post():
    if request.is_json:
        new_product = Product(**request.get_json()) #type: ignore
        price_calculated = tax_service.get_calculated_price(new_product.value)
        new_product.value = price_calculated.price
        new_product.tax = price_calculated.price
        new_product.create()

    return '', 201
