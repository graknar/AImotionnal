from transformers import pipeline

def get_emotions(text):
    def classify_emotion(text):
        classifier = pipeline("text-classification", model="cardiffnlp/twitter-roberta-large-emotion-latest")
        result = classifier(text)
        return result
    result = classify_emotion(text)
    emotions = [item['label'] for item in result]
    percentages = [item['score'] * 100 for item in result]
    return emotions, percentages