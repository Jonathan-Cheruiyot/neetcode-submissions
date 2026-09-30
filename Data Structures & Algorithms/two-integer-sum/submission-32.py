class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # I need to find the missing number that helps me get to target
        # I can create a hashmap to store the positon and values of the array
        # the hashmap can help me look into each location and find the missing value
        # Ex: [0,2],[1,7],[2,11],[3,15]
        # If I find my missing number and it has seen the missing numbers, you take that pairs position and return it 
        # if there is no numbers that match up tp the array, return none

        seen = {}
        for i,x in enumerate(nums):
            need = target - x 
            if need in seen:
                return [seen[need],i]
            seen[x] = i
        return None