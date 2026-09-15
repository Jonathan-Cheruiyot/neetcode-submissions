class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #First thing to do is search the array
        #You can enumerate the array to check each position and check 
        seen = {}
        for i,x in enumerate(nums):
            need = target - x 
            if need in seen:
                return [seen[need],i]
            seen[x] = i
        return None