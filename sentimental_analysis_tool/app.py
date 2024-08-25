from textblob import TextBlob
import nltk

# Ensure necessary NLTK data is downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return {
        'polarity': sentiment.polarity,
        'subjectivity': sentiment.subjectivity,
        'sentiment': 'positive' if sentiment.polarity > 0 else 'negative' if sentiment.polarity < 0 else 'neutral'
    }

def main():
    print("Welcome to the Sentiment Analysis Tool!")
    while True:
        text = input("Enter text to analyze (or type 'exit' to quit): ")
        if text.lower() == 'exit':
            break
        result = analyze_sentiment(text)
        print(f"Polarity: {result['polarity']}")
        print(f"Subjectivity: {result['subjectivity']}")
        print(f"Sentiment: {result['sentiment']}\n")

if __name__ == "__main__":
    main()
