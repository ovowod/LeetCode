class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(s: str):
            l, r = 0, len(s) - 1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        ans = ''
        for l in range(len(s)):
            for r in range(l, len(s)):
                if is_palindrome(s[l:r+1]):
                    if len(s[l:r+1]) > len(ans):
                        ans = s[l:r+1]
        return ans