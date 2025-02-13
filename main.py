import openai
from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

# 🔹 Replace this with your OpenAI API Key
OPENAI_API_KEY = "your-api-key-here"
openai.api_key = OPENAI_API_KEY

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    if not user_input:
        return jsonify({"error": "Message is required"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a legal information assistant. You provide general legal knowledge but do not give legal advice."},
                {"role": "user", "content": user_input}
            ]
        )

        bot_message = response["choices"][0]["message"]["content"]
        return jsonify({"response": bot_m
