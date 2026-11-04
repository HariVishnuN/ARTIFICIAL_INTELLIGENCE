import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download necessary lexicons
nltk.download('vader_lexicon', quiet=True)

sia = SentimentIntensityAnalyzer()

sentences = [
    "Machine Learning is absolutely fantastic and I love coding!",
    "This was a terrible experience and the algorithm failed completely.",
    "The dataset contains rows and columns of numeric data."
]

for sentence in sentences:
    scores = sia.polarity_scores(sentence)
    compound = scores['compound']
    
    if compound >= 0.05:
        sentiment = "Positive"
    elif compound <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
        
    print(f"Sentence: '{sentence}' -> Sentiment: {sentiment} (Score: {compound})")
