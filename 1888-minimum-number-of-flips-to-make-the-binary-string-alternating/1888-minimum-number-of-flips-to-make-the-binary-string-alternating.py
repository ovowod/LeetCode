class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        ss = s + s
        
        alt1, alt2 = '', ''
        for i in range(len(ss)):
            alt1 += "0" if i % 2 == 0 else "1"
            alt2 += "1" if i % 2 == 0 else "0"
        
        diff1, diff2 = 0, 0
        for i in range(n):
            if ss[i] != alt1[i]:
                diff1 += 1
            if ss[i] != alt2[i]:
                diff2 += 1

        res = min(diff1, diff2)

        for i in range(n):
            # l 처리: 들어오는 값이 오답이였으면 diff 감소
            if ss[i] != alt1[i]:
                diff1 -= 1
            if ss[i] != alt2[i]:
                diff2 -= 1
            
            # r 처리: 들어오는 값이 오답이면 diff 증가
            if ss[i + n] != alt1[i + n]:
                diff1 += 1
            if ss[i + n] != alt2[i + n]:
                diff2 += 1

            res = min(res, diff1, diff2)

        return res 

        
