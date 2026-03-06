class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        a = [b for b in s.split('0') if b]
        if len(a) == 1:
            return True
        return False
