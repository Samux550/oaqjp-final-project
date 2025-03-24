import requests

def emotion_detector(text_to_analyse):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    data = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:

        response_json = response.json() #the output is a dictionary
        emotions_json = response_json['emotionPredictions'][0]['emotion']

        anger_score = emotions_json['anger']
        disgust_score = emotions_json['disgust']
        fear_score = emotions_json['fear']
        joy_score = emotions_json['joy']
        sadness_score = emotions_json['sadness']
        
        dominant_emotion= max(emotions_json, key = emotions_json.get)
        return {
            'anger:': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
            }
        

    else:
        print(f"Error {response.status_code}: {response.text}")
    