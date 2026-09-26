class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # return the position of the peak number in the array
        # For example if the number is 5 and its position is 2, return that position
        # You could enumerate the numbers
        # Once you enumerate the numbers, you can have a variable called peak_ele that keeps the position and number [n,v]
        # As you check each position, you will check peak_ele and see if the number at your position is bigger than the one in the array
        # if it is bigger, you will update the position and value of peak_ele, if not, you can leave the code as is
        # once you check all the positions and have found the highest/peak number, you return the position of the highest number from peak_ele
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= nums[mid + 1]:
                left = mid + 1
            else: 
                right = mid
        return left
