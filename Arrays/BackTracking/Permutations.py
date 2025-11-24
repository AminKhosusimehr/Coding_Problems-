# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backTrack(path, remaining):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(remaining)):
                path.append(remaining[i])
                new_remaining = remaining[:i] + remaining[i + 1:]
                backTrack(path, new_remaining)
                path.pop()

        result = []
        backTrack([], nums)
        return result