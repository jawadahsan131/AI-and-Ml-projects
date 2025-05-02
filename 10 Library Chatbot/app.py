from flask import Flask, render_template, request, jsonify
import backend  # Import chatbot functions from backend.py
from backend import *
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = backend.get_chat_response(user_input)  # Pass user_input, not chatbot_app()
    return jsonify(response=response)

if __name__ == "__main__":
    app.run(debug=True)