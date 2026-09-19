class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sim = {}
        for string in strs:
            key = ''.join(sorted(string))

            if key not in sim:
                sim[key] = []

            sim[key].append(string)
        
        return list(sim.values())
        

        
            
        