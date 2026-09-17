class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #the goal is to take the whole list and sort it out into sub lists
        # take each position, and sort it to have the words in that position shown from a-z
        # I can check a second output array to see if the word that is scrambled is in that array
        # if the scrambled word is in the array, you can take the original word and put it into the 
        # at that postion
        # if it isn't in the array, you can create a new postion in the array to store its original word in that array
        # once that is all done, you can display the final output
        words = {}
        for word in strs:
            key = "".join(sorted(word)) #words get sorted and are combined as one string
            if key not in words:
                words[key] = []  #if not in words you make a new postion for it in the words list
            words[key].append(word)

        return list(words.values()) #returns only the values of the words like the output asks