class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        get rid of non-alpha values
        make sure they're all same case

        return adjusted string == adjusted string reversed
        '''
        dj_str = ""

        for val in s:
            if val.isalpha() or val.isnumeric():
                dj_str += val.upper()
        
        print(dj_str)
        # if len(dj_str) <= 1: return False             
        return dj_str == dj_str[::-1]
        