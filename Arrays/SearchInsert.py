# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        first = 0 
        last = len(nums) - 1
        while first <= last :
            mid =(first + last) // 2
            if nums[mid] == target :
                return mid
            elif target > nums[mid] :
                first = mid + 1
            elif target < nums[mid] : 
                last = mid - 1   
        return first               