# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes
# a string as input and returns the i and j indices that
# correspond to the beginning and end indices of the longest
# palindrome in the string.
#
# Grading Notes:
#
# You will only be marked correct if your function runs
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    if len(text) == 0:
        return (0, 0)

    text = text.lower()
    [start, end] = [0, 0]
    for i in range(len(text) - 1):
        (temp_start, temp_end) = check_palindrome(text, i)
        if(abs(temp_end - temp_start) > abs(end - start)):
            [start, end] = [temp_start, temp_end]

        if(text[i] == text[i + 1]):
            (temp_start, temp_end) = check_palindrome_double(text, i, i + 1)
            if (abs(temp_end - temp_start) > abs(end - start)):
                [start, end] = [temp_start, temp_end]
    return (start, end + 1)

def check_palindrome(text, i):
    '''check how far a palindorme can be extended from position i
    Return start and end indexes of the longest palindrome'''
    start, end = i, i
    while start-1 >= 0 and end+1 < len(text) and text[start-1] == text[end+1]:
        start -= 1
        end += 1
    return (start, end)

def check_palindrome_double(text, i, j):
    '''check how far a palindrome can be extended from posiiton i and j, assume text[i] == text[j]
    Return start and end indexes of the longest palindrome'''
    start, end = i, j
    while start-1 >= 0 and end+1 < len(text) and text[start-1] == text[end+1]:
        start -= 1
        end += 1
    return (start, end)

def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8, 21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'


if __name__ == "__main__":
    print(test())