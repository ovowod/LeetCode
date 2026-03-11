class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def permutations(ls):    
            if len(ls) == len(nums):
                result.append(ls.copy()) 
                return

            for i in range(len(nums)):
                if nums[i] in ls:
                    continue
                ls.append(nums[i])
                permutations(ls)
                ls.pop()
        
        permutations([])
        return result