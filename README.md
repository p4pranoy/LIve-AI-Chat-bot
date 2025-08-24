Here is a README file for your GitHub repository.

# Python Chatbot Powered by Google Gemini

This project is a simple, yet elegant, web-based chatbot built with **Python**, **Flask**, and the **Google Gemini API**. It provides a clean and modern user interface for real-time conversations.

## Features

  * **Gemini-powered chat:** Uses the Google Gemini 1.5 Flash model for fast and relevant responses.
  * **Rate limiting:** Prevents abuse and manages API usage efficiently with a built-in rate limiter.
  * **Intuitive UI:** A clean, single-page HTML design with a modern dark theme for a pleasant user experience.
  * **Scalable backend:** The Flask application provides a robust and simple API endpoint for handling chat requests.

-----

## Files in the repository

  * `app.py`: The main Flask application that handles web requests and interacts with the chatbot logic.
  * `chat.py`: Contains the core chatbot logic, including the class for connecting to the Gemini API and handling chat history.
  * `Chat_With_Us.html`: The frontend HTML file that provides the user interface for the chatbot.
  * `requirements.txt`: (Not provided, but recommended) A file listing the Python dependencies needed to run the project.

-----

## How to Set Up and Run

### Prerequisites

  * Python 3.7+
  * A Google Gemini API Key

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2.  **Install dependencies:**
    This project requires `flask`, `google-generativeai`, and `rateguard`. You can install them using pip:

    ```bash
    pip install Flask google-generativeai rateguard
    ```

3.  **Set up your Gemini API Key:**
    The application looks for the API key in a file called `.env` or as an environment variable named `GEMINI_API_KEY`. The `app.py` file also contains a placeholder API key for testing. For security, it's best to use environment variables.

      * **Option 1: Environment Variable (Recommended)**
        ```bash
        export GEMINI_API_KEY="YOUR_API_KEY_HERE"
        ```
      * **Option 2: Direct in `app.py` (Not recommended for production)**
        You can replace the placeholder key `AIzaSyBMoN9D7UUm4LYljEZG-K-HMLvb8hvunf0` directly in `app.py` with your own key.

### Running the application

After setting up your API key, you can run the Flask server:

```bash
python app.py
```

The server will start at `http://127.0.0.1:5000`. Open this URL in your web browser to start chatting\!

-----

## Code Structure

### `chat.py`

This file defines the `QAChat` class, which handles all interactions with the Gemini API. The `get_response` method uses the `@rate_limit` decorator from the `rateguard` library to ensure you don't exceed the API's request limits, preventing errors.

### `app.py`

This is the heart of the web server. It sets up a simple Flask application with two main routes:

  * `/`: Serves the `Chat_With_Us.html` file, which is the main chat interface.
  * `/chat`: A POST endpoint that receives user messages, passes them to the `QAChat` instance, and returns the bot's response in JSON format.

### `Chat_With_Us.html`

This is a single-page HTML file with CSS for styling and JavaScript for handling the chat logic. The JavaScript code listens for user input, sends messages to the `/chat` endpoint using `fetch`, and dynamically updates the chat window with both user and bot messages.
