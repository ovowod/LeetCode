class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        tel = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def recurse(s, digits, idx):
            if len(s) == len(digits):
                res.append(''.join(s))
                return s
            
            for digit in digits[idx]:
                for t in tel[digit]:
                    s.append(t)
                    recurse(s, digits, idx + 1)
                    s.pop()
        
        recurse([], digits, 0)
        return res