class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        
        for char in s:
            if char not in close_to_open:
                stack.append(char)
            elif not stack or stack[-1] != close_to_open[char]: #if stack is empty or if the character does not match with whatever at [-1], then we know we can return false
                return False
            else:
                stack.pop()
            
        return len(stack) == 0
