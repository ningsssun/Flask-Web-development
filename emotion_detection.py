import requests

def emotion_detector(text_to_analyze):
    # Define the URL and headers
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=input_json, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        result = response.json()['text']
        return result
    else:
        return "Error: Unable to process the emotion detection."

test_text = "I feel thrilled and excited!"
print(emotion_detector(test_text))

