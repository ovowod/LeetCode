from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for st in strs:
            anagrams[str(sorted(st))].append(st)
        return list(anagrams.values())