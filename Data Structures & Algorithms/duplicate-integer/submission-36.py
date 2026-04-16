class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() #Creating a set to store each individual number we see
        for n in nums: #searching the list ot see each postion in nums 
            if n in seen: # if seen in nums, return True as there is a duplicate
                return True
            seen.add(n) # add to the hashet if there isnt
        return False # return False if there is no duplicates 
        