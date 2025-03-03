import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        response_json = response.json()

        # Extract emotions
        emotions = response_json.get("emotionPredictions", [])[0].get("emotion", {})

        # Find the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)

        # Format output dictionary
        formatted_output = {
            "anger": emotions.get("anger", 0),
            "disgust": emotions.get("disgust", 0),
            "fear": emotions.get("fear", 0),
            "joy": emotions.get("joy", 0),
            "sadness": emotions.get("sadness", 0),
            "dominant_emotion": dominant_emotion
        }

        return formatted_output
    else:
        return {"error": f"Request failed with status {response.status_code}"}

# Example Usage:
if __name__ == "__main__":
    test_text = "I am so happy I am doing this."
    result = emotion_detector(test_text)
    print(result)