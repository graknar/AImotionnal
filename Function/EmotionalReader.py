from transformers import pipeline

def classify_emotion(text):
    classifier = pipeline("text-classification", model="cardiffnlp/twitter-roberta-large-emotion-latest")
    result = classifier(text)
    return result

def get_emotions(model):
    result = classify_emotion(model)
    emotions = [item['label'] for item in result]
    percentages = [item['score'] * 100 for item in result]
    return emotions, percentages