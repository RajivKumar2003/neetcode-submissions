from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            anagramMap[key].append(word)

        return list(anagramMap.values())
        