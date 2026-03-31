from flask import Flask, render_template, request
from dotenv import load_dotenv 
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

load_dotenv()

uri = os.getenv("MONGO_URI")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.demo

collection = db['flask-assessment']

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/submit', methods = ['POST'])

def submit():

    try:
        form_data = dict(request.form)

        collection.insert_one(form_data)

        return render_template('submit.html')

    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return f"Database Error: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)