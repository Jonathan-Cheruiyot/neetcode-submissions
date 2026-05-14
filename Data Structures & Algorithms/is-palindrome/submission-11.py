class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().strip() # used to get the strings lowercase and strip spacing
        left = 0 #left pointer
        right = len(s) -1 #right pointer 
        while left <= right: #if left pointer is less than or equal to the right pointer 
            if not s[left].isalnum(): # if the left sided character is not a numeric character
                                      # increment by 1 and use the continue to the top of the while loop
                left += 1
                continue
            if not s[right].isalnum(): # if the right sided character is not a numeric character
                                      # decrement by 1 use the continue to the top of the while loop
                right -= 1
                continue
            if s[left] != s[right]:    # check if the left character is not equal to the right character
                                        # return false if it the characters don't match.
                return False
            left += 1
            right -= 1
        return True

        