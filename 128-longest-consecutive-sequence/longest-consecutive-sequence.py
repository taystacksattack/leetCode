class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) #converts array into set in o(n) time and removes duplicates

        longest = 0

        # find starting numbers
            # numbers that do not have a consecutive number preceding
        # keep track of length of sequence (what we want to return at the end)
        # compare current sequence with longest sequence length

        for n in num_set:
            current_length = 1
            preceding_val = n-1
            
            if preceding_val not in num_set:
                curr_val = n
                
                while curr_val + 1 in num_set:
                    current_length += 1
                    curr_val += 1

                # if current_length > longest: longest = current_length
                longest = max(current_length, longest)

        return longest
            




