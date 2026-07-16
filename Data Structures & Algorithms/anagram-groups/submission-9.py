class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #My understanding of this question is to get an array of strings
        #And organize it by the strings that have the exact same characters, even if it is different order
        #You will probably need a new dict to store the sorted final array
        # you will need to have a way to slice each individual word, reorganize the letters from a to z 
        # and then use a loop that enumerates with the original word and the sorted word, 
        # and then check if the sorted word matches any other word in the dict
        # if it does match, we will add the original word to the dict and move on until the array is empty
        # if it doesnt match, we will add it as a new sublist in the dict. 

        sorted_words = {}
        for word in strs: 
            check = "".join(sorted(word))
            if check in sorted_words:
                sorted_words[check].append(word)
            else:
                sorted_words[check] = [word]
        return list(sorted_words.values())

        