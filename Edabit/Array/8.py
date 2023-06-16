"""
Given a list of integers representing the color of each sock, determine how many pairs of socks with matching colors there are. For example, there are 7 socks with colors [1, 2, 1, 2, 1, 3, 2]. There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.

Create a function that returns an integer representing the number of matching pairs of socks that are available.

Examples
sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]) ➞ 3

sock_merchant([50, 20, 30, 90, 30, 20, 50, 20, 90]) ➞ 4

sock_merchant([]) ➞ 0
Notes
N/A
"""

def sock_merchant(socks):
    sock_counts = {}
    for sock in socks:
        if sock in sock_counts:
            sock_counts[sock] += 1
        else:
            sock_counts[sock] = 1
    
    pair_counts = []
    for count in sock_counts.values():
        pair_counts.append(count // 2)
    
    return sum(pair_counts)

print(sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]))  # Output: 3
print(sock_merchant([50, 20, 30, 90, 30, 20, 50, 20, 90]))  # Output: 4
print(sock_merchant([]))  # Output: 0
