"""
4. Given an array of integers, find the pair of adjacent elements
that has the largest product and return that product.

Example
For inputArray = [3, 6, -2, -5, 7, 3], the output should be
solution(inputArray) = 21.

7 and 3 produce the largest product.
"""

def solution(array):
    largestProduct = array[0] * array[1]
    for i in range(1, len (array) - 1):
        product = (array[i] * array[i + 1])
        if product > largestProduct:
            largestProduct = product
    return largestProduct
        
array = [3, 6, -2, -5, 7, 3]
largestProduct = solution(array)
print(largestProduct)