import numpy as np
import math

def simple_sentiment_predict(text):

    text = text.lower()

    positive_words = ["happy","love","great","good","awesome"]
    negative_words = ["sad","bad","angry","hate","terrible"]

    pos_score = sum(word in text for word in positive_words)
    neg_score = sum(word in text for word in negative_words)

    score = pos_score - neg_score

    if score > 0:
        return "positive"
    elif score < 0:
        return "negative"
    else:
        return "neutral"