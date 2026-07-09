class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # search the array to return the numbers that equal the target number
        # need to search
        prevSeen = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevSeen:
                return [prevSeen[diff], i]
            prevSeen[n] = i