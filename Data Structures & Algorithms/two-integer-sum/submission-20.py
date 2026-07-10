class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevSeen = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevSeen:
                return [prevSeen[diff], i]
            prevSeen[n] = i