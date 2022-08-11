class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            m = target - n
            if m in nums[i+1:]:
                return [nums.index(n), nums[i + 1:].index(m) + (i + 1) ]