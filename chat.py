import google.generativeai as genai
from rateguard import rate_limit
import time

class QAChat:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        self.chat = self.model.start_chat(history=[])

    @rate_limit(rpm=15)  # Enforce 15 requests per minute
    def get_response(self, user_input):
        try:
            response = self.chat.send_message(user_input)
            return response.text
        except Exception as e:
            if "429" in str(e):
                return "Rate limit exceeded. Please wait a moment and try again."
            return f"Error: {str(e)}"