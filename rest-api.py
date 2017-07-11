#!/usr/bin/python
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------------------------
# Tiisc Firts REST API with Python and Flask Framework
# Author: Oscar Hernandez Diaz
# Email: oscar.hernandez@tiisc.com
# Startup: Tiisc
# Web: tiisc.com
# Date: 07-11-2017
# Documentation consulted:
# Book: What You Need to Know about Python by Pierluigi Riti
# THANK YOU!!!
# ----------------------------------------------------------------------------------------------
from flask import Flask, jsonify

app = Flask(__name__)

tiisc = [
    {
        'id': 1,
        'title': 'Learn Python',
        'description': 'Learn Python',
        'done': True
    },
    {
        'id': 2,
        'title': 'Learn Flask',
        'description': 'Learn Flask',
        'done': True
    },
    {
        'id': 3,
        'title': 'Turn and Tiisc',
        'description': 'Tiisc wants to work with Turn',
        'done': True
    },
    {
        'id': 4,
        'title': 'Learn RESTful APIS',
        'description': 'Tiisc already started studying about the RESTful APIs',
        'done': True
    }
]

@app.route('/python_api_rest/tiisc', methods=['GET'])

def get_list():
    return jsonify({'tiisc': tiisc})

if __name__ == '__main__':
    app.run(debug=True)