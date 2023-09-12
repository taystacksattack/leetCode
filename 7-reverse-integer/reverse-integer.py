class Solution:
    def reverse(self, x: int) -> int:
        # if x > 2**31 -1 or x <= -2**31: return 0

        # print(2**31)

        
        res = str(x)
        if res[0] == "-":
            # ("-" + res[1:-1:-1])
            reversed_x = int("-" + res[:0:-1])
        else:
            reversed_x = int(res[::-1])
        
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
        else: return reversed_x
        