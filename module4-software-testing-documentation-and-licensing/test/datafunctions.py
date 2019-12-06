import string
import numpy as np

def increment(x):
    return(x + 1)

def min_max_scaler(x):
    """Returns numpy array with original values scaled"""
    return (x - x.min()) / (x.max() - x.min())

def strip_punctuation(text):
    exclude = string.punctuation
    return ''.join(s for s in text if s not in exclude)

def bag_of_words(text):
    text = strip_punctuation(text)
    words = set(text.split(' '))
    return words
