import os
from google.cloud import language_v1

###  Set the environment variable for authentication
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:\\fyp\\indigo-pod-428619-d2-87f3e06bafd9.json"

def analyze_sentiment(text):
    client = language_v1.LanguageServiceClient()

    # The text to analyze
    document = language_v1.Document(content=text, type=language_v1.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment

    print("Text: {}".format(text))
    print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))

if __name__ == "__main__":
    text = "Google Cloud Natural Language API is really great!"
    analyze_sentiment(text)
