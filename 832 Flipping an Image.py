"""Can only run in Leetcode"""
"""832. Flipping an Image"""
"""https://leetcode.com/problems/flipping-an-image/"""
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        result = []
        count = 0
        for i in A:
            result.append([])
            for j in i[::-1]:
                if j == 0:
                    result[count].append(1)
                else:
                    result[count].append(0)
            count += 1
        return result
