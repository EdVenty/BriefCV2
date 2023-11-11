from enum import Enum

class ComparisonFunctionResult:
    first = 0
    second = 1
    
    
def _comparison_function_min(first, second):
    return ComparisonFunctionResult.first is first < second

def _comparison_function_max(first, second):
    return ComparisonFunctionResult.first is first > second

def search_with_key( __iterable, key, comp_func):
    goal_pair = None
    for i in __iterable:
        i_key = key(i)
        if goal_pair is None:
            goal_pair = (i, i_key)
        elif comp_func(goal_pair[1], i_key) == ComparisonFunctionResult.second:
            goal_pair = (i, i_key)
    return goal_pair

def min_with_key( __iterable, key):
    return search_with_key(__iterable, key, _comparison_function_min)

def max_with_key( __iterable, key):
    return search_with_key(__iterable, key, _comparison_function_max)

def min_key( __iterable, key):
    return search_with_key(__iterable, key, _comparison_function_min)[1]

def max_key( __iterable, key):
    return search_with_key(__iterable, key, _comparison_function_max)[1]