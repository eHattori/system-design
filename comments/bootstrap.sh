#!/bin/sh
sleep 2
export FLASK_APP=./app.py
export FLASK_DEBUG=true
pip install --upgrade pip
pip install -r requirements.txt
flask run -h 0.0.0.0 
