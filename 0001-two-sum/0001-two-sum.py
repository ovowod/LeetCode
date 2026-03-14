class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, v in enumerate(nums):
            indices[v] = i
        
        for i in range(len(nums)):
            if target - nums[i] in indices and i != indices[target-nums[i]]:
                return [i, indices[target-nums[i]]]
                
            