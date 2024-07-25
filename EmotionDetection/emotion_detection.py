import requests
import json

def emotion_detector(text_to_analyse):
    """
    Detects emotions in the provided text.

    Sends a request to the emotion analysis service and returns a dictionary with
    the detected emotion results. If the request fails (status code 400),
    returns a dictionary with all values set to None.

    Args:
        text_to_analyse (str): The text to analyze for detecting emotions.

    Returns:
        dict: A dictionary with detected emotion values and the dominant emotion.
              The dictionary keys are 'anger', 'disgust', 'fear', 'joy', 'sadness',
              and 'dominant_emotion'. The values are emotion scores or None if
              the request fails.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    
    # Añade un print para depuración
    print(f"Response status code: {response.status_code}")
    print(f"Response text: {response.text}")
    
    if response.status_code == 400:
        emotions_response = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        return emotions_response

    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    emotions_response = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': max(emotions, key=lambda x: emotions[x])
    }
    return emotions_response
