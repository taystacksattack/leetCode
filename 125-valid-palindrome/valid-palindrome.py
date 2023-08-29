class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        get rid of non-alpha values
        make sure they're all same case

        return adjusted string == adjusted string reversed
        '''
        dj_str = ''

        for char in s:
            if char.isalpha() or char.isnumeric():
                dj_str += char.upper()
        print(dj_str)
        return dj_str == dj_str[::-1]