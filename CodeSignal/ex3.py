"""
3. Given the string, check if it is a palindrome.

Example

For inputString = "aabaa", the output should be
solution(inputString) = true;
For inputString = "abac", the output should be
solution(inputString) = false;
For inputString = "a", the output should be
solution(inputString) = true
"""

def solution(inputString):
    inputString = inputString.replace(" ", "").lower()
    reversed_inputString = inputString[::-1]
    return inputString == reversed_inputString

inputString = ("a")
print(solution(inputString))