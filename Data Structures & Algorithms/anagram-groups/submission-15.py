class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #The goal of this question is to have a dict that stores all words that match in sorted form
        #First step is to make the word sorted out
        # Then you check if the word is in the dict
        # If the word is seen in the dict, you append the unsorted word into it
        # if it isnt seen, you make a new sorted anagram to store it
        # Lastly, you print out the values of the final list. 

        wds = {}
        for word in strs:
            wrd = "".join(sorted(word))
            if wrd in wds:
                wds[wrd].append(word)
            else:
                wds[wrd] = [word]
        return list(wds.values())

       

