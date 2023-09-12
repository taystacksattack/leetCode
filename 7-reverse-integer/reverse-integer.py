class Solution:
    def reverse(self, x: int) -> int:
        # if x > 2**31 -1 or x <= -2**31: return 0
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        # print(2**31)

        if x < INT_MIN or x > INT_MAX:
            return 0
        
        res = str(x)
        if res[0] == "-":
            # ("-" + res[1:-1:-1])
            reversed_x = int("-" + res[:0:-1])
        else:
            reversed_x = int(res[::-1])
        
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
        else: return reversed_x
        