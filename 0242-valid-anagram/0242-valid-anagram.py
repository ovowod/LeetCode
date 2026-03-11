from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagrams = defaultdict(int)
        for a in s:
            anagrams[a] += 1
        
        for b in t:
            anagrams[b] -= 1
            if anagrams[b] == 0: del anagrams[b]
        
        return not anagrams