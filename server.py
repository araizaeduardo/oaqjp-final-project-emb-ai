"""
server.py

This module defines a Flask application for emotion detection. It includes endpoints
for analyzing text and rendering the index page.
"""

import json
from flask import Flask, render_template, request, Response
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=['GET'])
def sent_detection():
    """
    Handles the GET request to analyze text and return detected emotions.

    Retrieves the 'textToAnalyze' parameter from the request and uses the `emotion_detector`
    function to analyze the text. If the 'textToAnalyze' parameter is missing or if the
    `emotion_detector` function returns a dominant emotion as None, an error message is returned.
    Otherwise, a response with the detected emotions is returned.

    Returns:
        Response: A JSON response containing the system response with detected emotions
                  or an error message for invalid input or analysis failure.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze:
        return Response(
            json.dumps({"error": "textToAnalyze parameter is missing"}),
            mimetype='application/json',
            status=400
        )

    emotions = emotion_detector(text_to_analyze)

    # Añade un print para depuración
    print(f"Emotions response: {emotions}")

    if emotions['dominant_emotion'] is None:
        return Response(
            json.dumps({"error": "Invalid text! Please try again!"}),
            mimetype='application/json',
            status=400
        )

    result = (
        f"For the given statement, the system response is 'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, "
        f"'joy': {emotions['joy']} and 'sadness': {emotions['sadness']}. "
        f"The dominant emotion is {emotions['dominant_emotion']}."
    )

    response = {
        "response": result
    }

    return Response(
        json.dumps(response),
        mimetype='application/json'
    )

@app.route("/")
def render_index_page():
    """
    Renders the index page of the application.

    This function handles the route for the root URL and returns
    the HTML template for the index page.

    Returns:
        str: The rendered HTML template for the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
