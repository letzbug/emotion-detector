from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions

def emotion_detector(text_to_analyze):
    authenticator = IAMAuthenticator('Srs7YNk8MSMKBYrPOuynwfW6UfjQjx0oyQWnDv_Zq4G6')
    
    nlu = NaturalLanguageUnderstandingV1(
        version='2022-04-07',
        authenticator=authenticator
    )
    
    nlu.set_service_url('https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/e69e66a9-4c1d-47c6-8606-ce1c7a076d76')
    
    response = nlu.analyze(
        text=text_to_analyze,
        features=Features(emotion=EmotionOptions(document=True))
    ).get_result()
    
    emotions = response['emotion']['document']['emotion']
    
    result = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': max(emotions, key=emotions.get)
    }
    
    return result


if __name__ == "__main__":
    text = "I am really happy about this new project!"
    print(emotion_detector(text))