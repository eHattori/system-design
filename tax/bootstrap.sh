#!/bin/sh
sleep 2
pip install --upgrade pip
pip install -r requirements.txt
python tax_server.py
