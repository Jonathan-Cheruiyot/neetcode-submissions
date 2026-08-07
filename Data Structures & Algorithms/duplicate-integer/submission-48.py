class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      # get the integer of arrays
      # If the arrays have more thna one value in the array, end the loop and return true
      # If not, then return false at the end
      # best way to go about it would be using a hashmap to store previous numbers 
      # You can use the array to crosscheck the hashmap to see if it is seen in the hashmap
      hashset = set()
      for num in nums:
        if num in hashset:
            return True
        else:
            hashset.add(num)
      return False