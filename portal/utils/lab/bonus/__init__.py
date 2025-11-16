"""
Bonus functions subdirectory containing bonus questions from Week 1.

Week 1 Day 1 Bonus:
- bonus1_count_without_stopwords.py
- bonus2_top_5_words_across_strings.py

Week 1 Day 2 Bonus:
- bonus3_count_numbers_frequency.py
- bonus4_has_mixed_case_and_number.py

Week 1 Day 3 Bonus:
- bonus5_extract_emails_and_phones.py
- bonus6_categorize_urls.py
"""

# Week 1 Day 1 Bonus
from .bonus1_count_without_stopwords import bonus1_count_without_stopwords
from .bonus2_top_5_words_across_strings import bonus2_top_5_words_across_strings

# Week 1 Day 2 Bonus
from .bonus3_count_numbers_frequency import bonus3_count_numbers_frequency
from .bonus4_has_mixed_case_and_number import bonus4_has_mixed_case_and_number

# Week 1 Day 3 Bonus
from .bonus5_extract_emails_and_phones import bonus5_extract_emails_and_phones
from .bonus6_categorize_urls import bonus6_categorize_urls

__all__ = [
    'bonus1_count_without_stopwords',
    'bonus2_top_5_words_across_strings',
    'bonus3_count_numbers_frequency',
    'bonus4_has_mixed_case_and_number',
    'bonus5_extract_emails_and_phones',
    'bonus6_categorize_urls',
]
