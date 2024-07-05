import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Make the request
    response = requests.post(url, json=input_json, headers=headers)
    print("Status Code:", response.status_code)  # Print the status code
    print("Response Text:", response.text)  # Print the raw response text

    # Process the response
    if response.status_code == 200:
        result = response.json().get('text', 'No text found in response')  # Safely get the text attribute
        return result
    else:
        return "Error: Unable to process the emotion detection. Status Code: {}".format(response.status_code)

# Example usage:
# test_text = "Good"
# print(emotion_detector(test_text))



