class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)): #원소 자기자신, 순서 바뀌면 같은 것 제외
                if nums[i] + nums[j] == target:
                    return [i, j]
        