from ie_utils import tokenize

@pytest.mark.parametrize("sentence, expected_tokens", [
    ("This is a sentence", ["This", "is", "a", "sentence"]),
    ("Another sentence", ["Another", "sentence"]),
])

def test_tokenize_returns_expected_list(sentence, expected_tokens): 
    tokens = tokenize(sentence)
    
    assert tokens == expected_tokens
    
def test_tokenize_lower_returns_lowercase_tokens(): 
    sentence = "This is a sentence"
    expected_tokens = ["this", "is", "a", "sentence"]
    
    tokens = tokenize(sentence, lower=True)
    
    assert tokens == expected_tokens
    
def test_tokenize_remove_stopwords_returns__tokens():
    sentence = "This is a sentence"
    expected_tokens = ["This", "is", "sentence"]
    
    tokens = tokenize(sentence, remove_stopwords=True)

    assert tokens == expected_tokens

def test_tokenize_remove_punctuation_returns__tokens():
    sentence = "This is a sentence."
    expected_tokens = ["This", "is", "a", "sentence"]
    tokens = tokenize(sentence, remove_punctuation=True)

    assert tokens == expected_tokens

def test_empty_string():
    sentence = " "
    tokens = tokenize(sentence)
    with pytest.raises(ValueError) as exc_info:
        if tokens == []:
            raise ValueError("Cannot tokenize empty sentence")
    assert exc_info.type is ValueError
    
def test_tokenize_parameters_returns__tokens():
    sentence = "This is a sentence."
    expected_tokens = ["this", "is", "sentence"]
    tokens = tokenize(sentence, remove_punctuation=True, remove_stopwords = True, lower = True)

    assert tokens == expected_tokens