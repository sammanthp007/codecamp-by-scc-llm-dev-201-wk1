"""
Django views for the Code Camp Utilities Portal.
Provides REST API endpoints and web interface for all week 1 utility functions.
"""

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

# Import utility functions from portal/utils/lab
from portal.utils.lab import (
    q1_count_character_frequency,
    q2_count_word_frequency,
    q3_top_3_frequent_words,
    bonus1_count_without_stopwords,
    bonus2_top_5_words_across_strings,
    q4_safe_division,
    q5_find_maximum,
    q6_is_palindrome,
    bonus3_count_numbers_frequency,
    bonus4_has_mixed_case_and_number,
    q7_extract_emails,
    q8_validate_phone_numbers,
    q9_extract_dates,
    bonus5_extract_emails_and_phones,
    bonus6_categorize_urls
)

# Import utility functions from portal/utils/assignment
from portal.utils.assignment import (
    q1_sentence_word_lengths,
    q2_common_elements_in_lists,
    q3_count_unique_characters,
    q4_safe_factorial,
    q5_reverse_words,
    q6_validate_password,
    q7_extract_hashtags,
    q8_remove_duplicates,
    q9_sum_numbers_in_text,
    q10_find_anagrams
)


def home(request):
    """Home page with tabbed interface for testing utility functions."""
    return render(request, 'portal/home.html')


# ============================================================================
# Week 1 Day 1 - Dictionaries & Counting APIs
# ============================================================================

@csrf_exempt
@require_http_methods(["POST"])
def api_w1d1_count_character_frequency(request):
    """API: Count character frequency in text."""
    try:
        data = json.loads(request.body)
        text = data.get('text', '')
        result = q1_count_character_frequency(text)
        return JsonResponse({
            'success': True,
            'input': text,
            'result': result
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def api_w1d1_count_word_frequency(request):
    """API: Count word frequency in paragraph."""
    try:
        data = json.loads(request.body)
        paragraph = data.get('text', '')
        result = q2_count_word_frequency(paragraph)
        return JsonResponse({
            'success': True,
            'input': paragraph,
            'result': result
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def api_w1d1_top_3_frequent_words(request):
    """API: Get top 3 most frequent words."""
    try:
        data = json.loads(request.body)
        text = data.get('text', '')
        result = q3_top_3_frequent_words(text)
        return JsonResponse({
            'success': True,
            'input': text,
            'result': result
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def api_w1d1_count_without_stopwords(request):
    """API: Count words excluding stopwords."""
    try:
        data = json.loads(request.body)
        text = data.get('text', '')
        stopwords = data.get('stopwords', None)
        result = bonus1_count_without_stopwords(text, stopwords)
        return JsonResponse({
            'success': True,
            'input': text,
            'stopwords': stopwords,
            'result': result
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def api_w1d1_top_5_words_across_strings(request):
    """API: Get top 5 words across multiple strings."""
    try:
        data = json.loads(request.body)
        string_list = data.get('string_list', [])
        result = bonus2_top_5_words_across_strings(string_list)
        return JsonResponse({
            'success': True,
            'input': string_list,
            'result': result
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


# ============================================================================
# Week 1 Day 2 - Functions & Error Handling APIs
# ============================================================================

@csrf_exempt
@require_http_methods(["POST"])
def api_w1d2_safe_division(request):
    """API: Perform safe division."""
    try:
        data = json.loads(request.body)
        numerator = data.get('numerator')
        denominator = data.get('denominator')
        result = q4_safe_division(numerator, denominator)
        return JsonResponse({
            'success': True,
            'input': {'numerator': numerator, 'denominator': denominator},
            'result': result
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def api_w1d2_find_maximum(request):
    """API: Find maximum value in list."""
    try:
        data = json.loads(request.body)
        numbers = data.get('numbers', [])
        result = q5_find_maximum(numbers)
        return JsonResponse({
            'success': True,
            'input': numbers,
            'result': result
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def api_w1d2_is_palindrome(request):
    """API: Check if text is palindrome."""
    try:
        data = json.loads(request.body)
        text = data.get('text', '')
        result = q6_is_palindrome(text)
        return JsonResponse({
            'success': True,
            'input': text,
            'result': result
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def api_w1d2_count_numbers_frequency(request):
    """API: Count number frequency in list."""
    try:
        data = json.loads(request.body)
        numbers = data.get('numbers', [])
        result = bonus3_count_numbers_frequency(numbers)
        return JsonResponse({
            'success': True,
            'input': numbers,
            'result': result
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def api_w1d2_has_mixed_case_and_number(request):
    """API: Check if text has mixed case and numbers."""
    try:
        data = json.loads(request.body)
        text = data.get('text', '')
        result = bonus4_has_mixed_case_and_number(text)
        return JsonResponse({
            'success': True,
            'input': text,
            'result': result
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


# ============================================================================
# Week 1 Day 3 - Regex & Pattern Recognition APIs
# ============================================================================

@csrf_exempt
@require_http_methods(["POST"])
def api_w1d3_extract_emails(request):
    """API: Extract email addresses from text."""
    try:
        data = json.loads(request.body)
        text = data.get('text', '')
        result = q7_extract_emails(text)
        return JsonResponse({
            'success': True,
            'input': text,
            'result': result
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def api_w1d3_validate_phone_numbers(request):
    """API: Extract phone numbers from text."""
    try:
        data = json.loads(request.body)
        text = data.get('text', '')
        result = q8_validate_phone_numbers(text)
        return JsonResponse({
            'success': True,
            'input': text,
            'result': result
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def api_w1d3_extract_dates(request):
    """API: Extract dates from text."""
    try:
        data = json.loads(request.body)
        text = data.get('text', '')
        result = q9_extract_dates(text)
        return JsonResponse({
            'success': True,
            'input': text,
            'result': result
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def api_w1d3_extract_emails_and_phones(request):
    """API: Extract both emails and phone numbers."""
    try:
        data = json.loads(request.body)
        text = data.get('text', '')
        result = bonus5_extract_emails_and_phones(text)
        return JsonResponse({
            'success': True,
            'input': text,
            'result': result
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def api_w1d3_categorize_urls(request):
    """API: Categorize URLs by domain type."""
    try:
        data = json.loads(request.body)
        text = data.get('text', '')
        result = bonus6_categorize_urls(text)
        return JsonResponse({
            'success': True,
            'input': text,
            'result': result
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


# ============================================================================
# Assignment Week 1 - Various Concepts APIs
# ============================================================================

@csrf_exempt
@require_http_methods(["POST"])
def api_assignment_q1_sentence_word_lengths(request):
    """API: Get word lengths mapping from sentence."""
    try:
        data = json.loads(request.body)
        sentence = data.get('sentence', '')
        result = q1_sentence_word_lengths(sentence)
        return JsonResponse({
            'success': True,
            'input': sentence,
            'result': result
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def api_assignment_q2_common_elements_in_lists(request):
    """API: Find common elements between two lists."""
    try:
        data = json.loads(request.body)
        list1 = data.get('list1', [])
        list2 = data.get('list2', [])
        result = q2_common_elements_in_lists(list1, list2)
        return JsonResponse({
            'success': True,
            'input': {'list1': list1, 'list2': list2},
            'result': list(result) if isinstance(result, set) else result
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def api_assignment_q3_count_unique_characters(request):
    """API: Count unique characters in text."""
    try:
        data = json.loads(request.body)
        text = data.get('text', '')
        result = q3_count_unique_characters(text)
        return JsonResponse({
            'success': True,
            'input': text,
            'result': result
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def api_assignment_q4_safe_factorial(request):
    """API: Calculate factorial with error handling."""
    try:
        data = json.loads(request.body)
        n = data.get('n')
        result = q4_safe_factorial(n)
        return JsonResponse({
            'success': True,
            'input': n,
            'result': result
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def api_assignment_q5_reverse_words(request):
    """API: Reverse each word in a sentence."""
    try:
        data = json.loads(request.body)
        sentence = data.get('sentence', '')
        result = q5_reverse_words(sentence)
        return JsonResponse({
            'success': True,
            'input': sentence,
            'result': result
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def api_assignment_q6_validate_password(request):
    """API: Validate password strength."""
    try:
        data = json.loads(request.body)
        password = data.get('password', '')
        result = q6_validate_password(password)
        return JsonResponse({
            'success': True,
            'input': password,
            'result': result
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def api_assignment_q7_extract_hashtags(request):
    """API: Extract hashtags from text."""
    try:
        data = json.loads(request.body)
        text = data.get('text', '')
        result = q7_extract_hashtags(text)
        return JsonResponse({
            'success': True,
            'input': text,
            'result': result
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def api_assignment_q8_remove_duplicates(request):
    """API: Remove duplicates from list while preserving order."""
    try:
        data = json.loads(request.body)
        items = data.get('items', [])
        result = q8_remove_duplicates(items)
        return JsonResponse({
            'success': True,
            'input': items,
            'result': result
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def api_assignment_q9_sum_numbers_in_text(request):
    """API: Sum all numbers found in text."""
    try:
        data = json.loads(request.body)
        text = data.get('text', '')
        result = q9_sum_numbers_in_text(text)
        return JsonResponse({
            'success': True,
            'input': text,
            'result': result
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def api_assignment_q10_find_anagrams(request):
    """API: Find anagrams of a word from a list."""
    try:
        data = json.loads(request.body)
        word = data.get('word', '')
        word_list = data.get('word_list', [])
        result = q10_find_anagrams(word, word_list)
        return JsonResponse({
            'success': True,
            'input': {'word': word, 'word_list': word_list},
            'result': result
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)
