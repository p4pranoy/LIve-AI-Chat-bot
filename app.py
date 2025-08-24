from flask import Flask, request, jsonify, render_template
from chat import QAChat
import os

app = Flask(__name__)

# Replace with your Gemini API key or use environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyBMoN9D7UUm4LYljEZG-K-HMLvb8hvunf0")
chatbot = QAChat(GEMINI_API_KEY)

@app.route('/')
def index():
    return render_template('Chat_With_Us.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'response': 'Please provide a message.'}), 400
    response = chatbot.get_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)