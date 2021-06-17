"""
IE Titanic utils.
"""

__version__ = "0.1.0"  # semver.org (semantic versioning)

import re
import pytest

#def tokenize(text, lower=False):
 #   if lower:
  #      text = text.lower()
   # return text.split()
    
def tokenize(text, lower=False, remove_punctuation=False, remove_stopwords=False):
    if text == "":
        raise ValueError("Cannot tokenize empty sentence")
    else:
        if lower:
            text = text.lower()
        if remove_punctuation:
            text = re.sub("[.,!]", "", text)
        if remove_stopwords:
            stopwords = ["a", "the", "or", "and"]
            words = text.split()
            non_stop_words = [w for w in words if not w in stopwords]
            text = " ".join(non_stop_words)    
        return text.split()


if __name__ == "__main__":
    print(tokenize("Hello world"))
