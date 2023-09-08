class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # split, then sort, then check if they're equal
        sSorted = sorted(list(s))
        tSorted = sorted(list(t))
    
        return sSorted == tSorted