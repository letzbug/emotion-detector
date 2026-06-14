import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    headers = {
        "Content-Type": "application/json"
    }
    
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code != 200:
        return {"error": f"Request failed with status {response.status_code}"}
    
    result = response.json()
    
    emotions = result['emotionPredictions'][0]['emotion']
    
    emotion_scores = {
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disgust', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
        'sadness': emotions.get('sadness', 0),
        'dominant_emotion': max(emotions, key=emotions.get)
    }
    
    return emotion_scores


if __name__ == "__main__":
    text = "I am really happy about this new project!"
    print(emotion_detector(text))
