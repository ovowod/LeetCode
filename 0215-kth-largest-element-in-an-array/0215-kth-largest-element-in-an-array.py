import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pri_nums = []
        for n in nums:
            heapq.heappush(pri_nums, -n)

        for _ in range(k):
            a = heapq.heappop(pri_nums)
        return -a
