class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)

        for i in nums:
            res[i] += 1
        
        return sorted(res, key=res.get, reverse=True)[:k]
        
        


        