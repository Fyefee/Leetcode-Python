"""Can only run in Leetcode"""
"""https://leetcode.com/problems/unique-number-of-occurrences/"""
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        result = []
        for i in set(arr):
            if arr.count(i) in result:
                return False
            result.append(arr.count(i))
        return True
