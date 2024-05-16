#!/usr/bin/python3

def multiple_returns(sentence):
    """
    multiple_returns - Gives basic information about a sentence

    @sentence: The sentence to be evaluated

    Returns: The length of 'sentence' and it's first character (if any)
    """
    return (len(sentence), sentence[0] if len(sentence) > 0 else None)
