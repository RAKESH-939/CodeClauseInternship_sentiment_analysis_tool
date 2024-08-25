# CodeClauseInternship_sentiment_analysis_tool

## Sentiment Analysis Tool
A simple command-line tool for analyzing the sentiment of a given text using the TextBlob library. This tool provides insights into the polarity and subjectivity of the text and classifies the sentiment as positive, negative, or neutral.

### Features
. Polarity Analysis: Measures how positive or negative the text is.
. Subjectivity Analysis: Measures how subjective or objective the text is.
. Sentiment Classification: Classifies the sentiment as positive, negative, or neutral.

### Example
Run the sentiment analysis tool by executing the app.py script:

Welcome to the Sentiment Analysis Tool!
Enter text to analyze (or type 'exit' to quit): I love this beautiful day!
Polarity: 0.85
Subjectivity: 0.6
Sentiment: positive

To exit the tool, type exit.

### How It Works
The sentiment analysis tool leverages the TextBlob library, which utilizes NLTK for natural language processing. The tool calculates sentiment by:

Polarity: A float within the range [-1.0, 1.0], where negative numbers indicate negative sentiment, and positive numbers indicate positive sentiment.
Subjectivity: A float within the range [0.0, 1.0], where 0.0 is very objective, and 1.0 is very subjective.
Sentiment: A classification based on the polarity score.
Contributing
Contributions are welcome! If you'd like to contribute, please fork the repository, make your changes, and submit a pull request.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Acknowledgments
TextBlob for providing easy-to-use NLP tools.
NLTK for natural language processing support
