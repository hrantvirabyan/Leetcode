"""
You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much
 as every other number in the array. If it is, 
return the index of the largest element, or return -1 otherwise.

"""
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        sorted_nums = sorted(nums)

        if sorted_nums[-1] >= sorted_nums[-2] * 2:
            return nums.index(sorted_nums[-1])

        return -1
