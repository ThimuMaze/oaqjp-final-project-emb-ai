import requests
import json

url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def find_dominant_emotion(dict):
    val_list = dict.values()
    max_val = max(val_list)
    print(max_val)
    dominant = ""
    for key , value in dict.items():
        if value == max_val:
            dominant = key
            break
    return dominant


def emotion_detector(text_to_analyze):
    json_obj = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url , json=json_obj , headers = header)
    response_json = json.loads(response.text)
    anger = response_json['emotionPredictions'][0]['emotion']['anger']
    disgust = response_json['emotionPredictions'][0]['emotion']['disgust']
    fear = response_json['emotionPredictions'][0]['emotion']['fear']
    joy = response_json['emotionPredictions'][0]['emotion']['joy']
    sadness = response_json['emotionPredictions'][0]['emotion']['sadness']
    response_dict = {"anger" : anger , "disgust" : disgust, "fear":fear , "joy":joy,"sadness":sadness}
    dominant_val = find_dominant_emotion(response_dict)
    response_dict["dominant_emotion"] = dominant_val
    return response_dict