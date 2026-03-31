'''
Create a Flask application with an /api route. 
When this route is accessed, it should return a JSON list. 
The data should be stored in a backend file, read from it, and sent as a response.

'''

from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

def read_backend_file():
    file_path = 'backend_file.json'
    
    # Check if file exists to avoid crashes
    if not os.path.exists(file_path):
        return "Error! Something went wrong when fetching the data"
    
    #open the file in read mode
    with open(file_path, 'r') as file:
        return json.load(file)

@app.route('/api', methods=['GET'])

def read_data():
    data = read_backend_file() 
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
