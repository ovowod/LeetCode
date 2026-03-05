from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        possible = [list(p) for p in list(permutations(nums, len(nums)))]
        return possible