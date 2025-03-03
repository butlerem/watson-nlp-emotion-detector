"""
Flask API for Emotion Detection.

This API processes text input and returns emotion analysis.
"""

import sys
import os

from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))  # Ensure module is recognized

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def detect_emotion():
    """
    Handles GET and POST requests for emotion detection.
    - GET: Returns a message instructing to use POST.
    - POST: Processes text input and returns emotion analysis.
    """
    if request.method == 'GET':
        return jsonify({"message": "Use a POST request with a JSON body to analyze emotions."})

    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Invalid input. Please provide a text field."}), 400

    text = data["text"]
    response = emotion_detector(text)

    if response["dominant_emotion"] is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400
    formatted_response = (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']}, and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return jsonify({"response": formatted_response})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
