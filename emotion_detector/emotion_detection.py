import requests

url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def emotion_detector(text_to_analyze):
    json = {"raw_document": {"text": text_to_analyze}}
    response_text = requests.post(url , json=json , headers = header)
    return response_text