# defaultdict creates a hash table, and uses the alphabetized strings as keys
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # start by sorting the letters in each string


        groups = defaultdict(list)
            # everytime you create a new key for the groups dict, it makes the default value a blank array
        for s in  strs:
            key = ''.join(sorted(s))  #creates the sorted key by sorting the string, then joining it to the empty string
            groups[key].append(s)

        return groups.values() #just spits out the values of the object you've created - nb that it is invoked

