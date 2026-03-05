class Solution:
    def minOperations(self, s: str) -> int:
        check1 = '10' * (len(s) // 2)
        check2 = '01' * (len(s) // 2)

        if len(s) % 2 != 0:
            check1 += '1'
            check2 += '0'

        cnt1, cnt2 = 0, 0
        for a, b in zip(check1, s):
            if a == b:
                cnt1 += 1
        
        for a, b in zip(check2, s):
            if a == b:
                cnt2 += 1
        
        return min(cnt1, cnt2)