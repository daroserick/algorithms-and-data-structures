# Receive an array of numbers and return the largest value

from typing import List

def find_maximum(numbers: List[int]) -> int:
    return max(numbers)

user_input = input('Write the numbers separated by space: ')
numbers = list(map(int, user_input.strip().split()))
maximum = find_maximum(numbers)
print(maximum)