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
        right = len(nums)-1
        # Variables made sure theres no end of array errors 
        while left < right:
            # gets the midpoint of the array
            mid = (left + right) // 2
            # if the num is smaller than to the point on its right, you move right to the bigger spot the check sizes again
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            #if not, you set the right side as the mid point and check one more time before returning the finalized answer 
            else:
                right = mid 
        return left
