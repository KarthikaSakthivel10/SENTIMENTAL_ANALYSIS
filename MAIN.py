from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"

text_to_analyze = input()
result = analyze_sentiment(text_to_analyze)
print(f"The sentiment of the text is: {result}")
