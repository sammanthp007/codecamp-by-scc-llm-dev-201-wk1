"""
Lab subdirectory containing individual question files for Week 1.

Week 1 Day 1: Dictionaries & Counting
- q1_count_character_frequency.py
- q2_count_word_frequency.py
- q3_top_3_frequent_words.py
- bonus/bonus1_count_without_stopwords.py
- bonus/bonus2_top_5_words_across_strings.py

Week 1 Day 2: Functions & Error Handling
- q4_safe_division.py
- q5_find_maximum.py
- q6_is_palindrome.py
- bonus/bonus3_count_numbers_frequency.py
- bonus/bonus4_has_mixed_case_and_number.py

Week 1 Day 3: Regex & Pattern Recognition
- q7_extract_emails.py
- q8_validate_phone_numbers.py
- q9_extract_dates.py
- bonus/bonus5_extract_emails_and_phones.py
- bonus/bonus6_categorize_urls.py
"""

# Week 1 Day 1
from .q1_count_character_frequency import q1_count_character_frequency
from .q2_count_word_frequency import q2_count_word_frequency
from .q3_top_3_frequent_words import q3_top_3_frequent_words

# Week 1 Day 2
from .q4_safe_division import q4_safe_division
from .q5_find_maximum import q5_find_maximum
from .q6_is_palindrome import q6_is_palindrome

# Week 1 Day 3
from .q7_extract_emails import q7_extract_emails
from .q8_validate_phone_numbers import q8_validate_phone_numbers
from .q9_extract_dates import q9_extract_dates

# Bonus functions from lab/bonus
from .bonus import (
    bonus1_count_without_stopwords,
    bonus2_top_5_words_across_strings,
    bonus3_count_numbers_frequency,
    bonus4_has_mixed_case_and_number,
    bonus5_extract_emails_and_phones,
    bonus6_categorize_urls,
)

__all__ = [
    # W1D1
    'q1_count_character_frequency',
    'q2_count_word_frequency',
    'q3_top_3_frequent_words',
    'bonus1_count_without_stopwords',
    'bonus2_top_5_words_across_strings',
    # W1D2
    'q4_safe_division',
    'q5_find_maximum',
    'q6_is_palindrome',
    'bonus3_count_numbers_frequency',
    'bonus4_has_mixed_case_and_number',
    # W1D3
    'q7_extract_emails',
    'q8_validate_phone_numbers',
    'q9_extract_dates',
    'bonus5_extract_emails_and_phones',
    'bonus6_categorize_urls',
]
