class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appear = {}
        for num in nums:
          if num in appear:
            return True
          appear[num] = True
        return False