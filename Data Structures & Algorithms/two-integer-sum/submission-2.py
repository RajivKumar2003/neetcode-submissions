class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        guy = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in guy:
                return [guy[diff],i]
            guy[n] = i


        
        