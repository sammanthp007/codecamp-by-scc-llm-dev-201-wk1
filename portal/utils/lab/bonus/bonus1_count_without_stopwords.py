"""W1D1 Bonus 1 - Count Without Stopwords

Count word frequency while ignoring common stopwords.

Example:
    >>> bonus1_count_without_stopwords("the cat and the dog")
    {'cat': 1, 'dog': 1}
"""


def bonus1_count_without_stopwords(text, stopwords=None):
    """
    Count word frequency while ignoring common stopwords.
    
    Args:
        text (str): The input string to analyze
        stopwords (list): List of stopwords to ignore. Default: ["the","and","a","of"]
        
    Returns:
        dict: A dictionary of word frequencies excluding stopwords
        
    Example:
        >>> bonus1_count_without_stopwords("the cat and the dog")
        {'cat': 1, 'dog': 1}
    """
    if stopwords is None:
        stopwords = ["the", "and", "a", "of"]
    # Your code here
    pass
