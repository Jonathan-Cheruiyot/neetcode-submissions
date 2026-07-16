class Solution:

    def encode(self, strs: List[str]) -> str: 
        res = ""
        
        for s in strs: 
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        
        # "5/hello5/world14/ssncabsabsds"
             
        # Goes through res, checks for each number + # to recogize each word
        #Left pointer will follow the right, and will only opdate as it sees any number
        # Once you hit the first delimiter with right pointer, you take the complete number from left pointer
        # And you will add a one to it and move the left pointer that length
        # once left pointer has moved, you will print out what is in between the right and left pointer
        # You then move the right pointer to be one ahead of the left pointer and then iterate through the loop until you find another delimiter with the right pointer
        # return the separated list once res is fully looked over 
        
        left = 0 
        arr = []
        while left < len(s):
            right = left
            while s[right] != "#":
                right += 1
                
            length = int(s[left:right])
            
            arr.append(s[right + 1 : right + 1 + length])
            
            left = right + 1 + length
        return arr