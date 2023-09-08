class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # split, then sort, then check if they're equal

        return sorted(list(s)) == sorted(list(t))