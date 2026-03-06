class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        split_0 = sorted(s.split('0'), key=lambda x: -len(x))
        split_1 = sorted(s.split('1'), key=lambda x: -len(x))

        if len(split_0[0]) > len(split_1[0]):
            return True
        return False
                