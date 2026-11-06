class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check if have the same characters and length
        # sort the anagram and check if it matches
        # if it does, return true, if not, return false 
        str1 = sorted(s)
        str2 = sorted(t)
        if str1 == str2:
            return True
        else:
            return False
        