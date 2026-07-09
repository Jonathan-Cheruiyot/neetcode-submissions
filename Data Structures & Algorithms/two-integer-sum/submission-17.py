class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # search the array to return the numbers that equal the target number
        # need to search
        for i in range(len(nums)):
            for j in range(i+1, len(nums)): 
                if nums[i] + nums[j] == target: 
                    return [i,j]
        return []