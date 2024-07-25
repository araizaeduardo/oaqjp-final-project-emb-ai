from flask import Flask, render_template, request, Response
from EmotionDetection.emotion_detection import emotion_detector
import json

app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=['GET'])
def sent_detection():
    # Obtén el texto a analizar desde los parámetros de la URL
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze:
        return Response(json.dumps({"error": "textToAnalyze parameter is missing"}), mimetype='application/json', status=400)

    emotions = emotion_detector(text_to_analyze)

    result = (f"For the given statement, the system response is 'anger': {emotions['anger']}, "
              f"'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, "
              f"'joy': {emotions['joy']} and 'sadness': {emotions['sadness']}. "
              f"The dominant emotion is {emotions['dominant_emotion']}.")

    response = {
        "response": result
    }

    return Response(json.dumps(response), mimetype='application/json')

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)