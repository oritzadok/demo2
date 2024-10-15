import os
from flask import Flask, jsonify, request
import pyodbc

app = Flask(__name__)

@app.route('/')
def handle():
  print('Request received')

  data = { 
    "Modules" : 15, 
    "Subject" : "bla"
  } 
  
  return jsonify(data)


if __name__ == '__main__':
   app.run()
