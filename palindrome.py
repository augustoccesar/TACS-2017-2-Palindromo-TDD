import re


def is_palindrome(input_string):
    filtered_string = re.sub("[-\s]", "", input_string).lower()
    return filtered_string == filtered_string[::-1]
