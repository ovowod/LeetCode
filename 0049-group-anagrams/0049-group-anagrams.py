from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for st in strs:
            k = [0] * 26
            for s in st:
                k[ord(s) - 97] += 1
            anagrams[str(k)].append(st)
        
        return list(anagrams.values())
