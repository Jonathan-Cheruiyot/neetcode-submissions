class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Planning: 
        # Look into each position in an array
        # For each number in the array, use a counter variable for each unique number
        # Increment by 1 for each repeating number in the array
        # Output the final array for each number.
        count = {}
        freq = [[] for i in range(len(nums) + 1 )]

        for n in nums: 
            count[n] = 1 + count.get(n,0)
        for n, c in count.items(): 
            freq[c].append(n)

        res = []
        for i in range(len(freq) -1, 0, -1): 
            for n in freq[i]:
                res.append(n)

                if len(res) == k: 
                    return res

        