class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,k in enumerate(nums): 
            diff = target - k
            if diff in seen: 
                return [seen[diff], i]
            seen[k] = i

        