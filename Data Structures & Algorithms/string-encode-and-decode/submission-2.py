class Solution:

    def encode(self, strs: List[str]) -> str: 
        # In order to encode the string, you have to count the length of the string
        # And give it a delimiter in order to separate the values when they are in one line
        # Using the delimiter, I am currently checking for each word in the original list, 
        # Counting the length of the word, and putting the "#" in front of it to help in the future wth decoding 
        # You add the string to the empty string we made in the beginning, and you use that string for decoding

        res = ""
        
        for s in strs: 
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        # The goal with decoding is to upack the long string and get the words to be in an array
        # I used two pointers to help traverse the array, the left pointer to be a bookmark for the digits
        # The right will iterate one by one until it hits an "#"
        # Once it hits an "#", the digits between the right and left node is taken
        # Once the digits are taken, the left node moves the length of those digits + 1 in order to get the full word that needs to be decoded 
        # The next step is to take and store the words between the right and left pointer and put it in arr 
        # Move the right node to be equal with the left node, and then repeat the process 
        # Print out the final list when it is done
        
        left = 0 
        arr = []
        while left < len(s):
            right = left
            while s[right] != "#":
                right += 1
                
            length = int(s[left:right])
            start = right + 1
            end = start + length 
            arr.append(s[start:end])
            
            left = end
        return arr