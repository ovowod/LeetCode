class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indices = {}
        for i, v in enumerate(numbers):
            diff = target - v
            if diff in indices:
                return [indices[diff] + 1, i + 1]
            indices[v] = i

        