from typing import Counter

# ref: https://www.delftstack.com/howto/python/python-anagram/
# https://www.datacamp.com/tutorial/case-conversion-python
def is_anagram(first_string, second_string):
    first_lower_string = first_string.lower()
    second_lower_string = second_string.lower()

    if len(first_string) != len(second_string):
        return False
    
    count_first_string = {}
    count_second_string = {}

    for letter in first_lower_string:
        if letter not in count_first_string.keys():
            count_first_string[letter] = 1
        else:
            count_first_string[letter] += 1
        
    for letter in second_lower_string:
        if letter not in count_second_string.keys():
            count_second_string[letter] = 1
        else:
            count_second_string[letter] += 1
    
    return True if count_first_string == count_second_string else False
