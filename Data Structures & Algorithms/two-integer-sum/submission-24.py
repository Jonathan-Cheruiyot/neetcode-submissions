class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       #I need to find the two numbers in the array that combine to the target number
       #the numbers position cannot be the same in the array
       #the output will be the positions of the two numbers that add up to target
        seen = {}
        for i, num in enumerate(nums):
            fnum = target - nums[i]
            if fnum in seen:
                j = seen[fnum]
                return [j,i]
            else: 
                seen[num] = i
        
        return []