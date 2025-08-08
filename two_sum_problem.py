"""
You are given an array of numbers and a target sum. Your task is to find the indices of the two numbers that add up to the target.

Example
nums = [2, 7, 11, 15]
target = 9
# Output: [0, 1] (Because 2 + 7 = 9)

"""

from typing import List

def find_indexes(numbers: List, sum: int) -> List:
    hash_map = {value: idx for idx, value in enumerate(numbers)}
    for value, idx in hash_map.items():
        complement = sum - value
        if complement in hash_map:
            return [idx, hash_map[complement]]
        
if __name__ == "__main__":
    print(find_indexes([2, 7, 11, 15], 9))