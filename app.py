from flask import Flask, render_template, request, jsonify, abort
from flask_cors import CORS
from utils import chatbot, message_history
import os
import time

# SETUP

# Read API key from file
with open('api_key.txt', 'r') as file:
    openai_apikey = file.read().strip()

# Export API key to local environment
os.environ['OPENAI_API_KEY'] = openai_apikey

# Create Flask app instance
app = Flask(__name__)
app.config['CACHE_TYPE'] = 'null' # disable if in production environment
CORS(app)

# TODO 1: create home page
@app.route("/")
def home():
    return render_template("home.html")

# TODO 2: style your chat interface
@app.route('/chat/', methods=['GET','POST'])
def chat():
    if request.method == 'GET':
        return render_template("chat.html")

    elif request.method == 'POST' and request.content_type == 'application/json':
        user_message = request.get_json("message")
        print(user_message)
        if not user_message:
            return jsonify({"error": "No message provided"})
        
        # function that makes API call to OpenAI

        response = chatbot(user_message)

        return jsonify({"response": response})
    

@app.route('/predict/', methods=['POST'])
def predict():

    if request.method == 'POST' and request.content_type == 'application/json':
        user_message = request.get_json("message")
        print(user_message)
        if not user_message:
            return jsonify({"error": "No message provided"})
        
        # function that makes API call to OpenAI

        response = chatbot(user_message)
        message_history.pop()

        return jsonify({"response": response})
        

if __name__ == '__main__':
    app.run(debug=True)