# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # create a set

        # iterate through the list (while current.val != None)
        # if the current.val is in the set, return true
        # otherwise, add current.val. to the set

        # return False

        current = head

        if current == None: return False

        while current and current.next:   
            # if head.next.next == None: return False
            
            current = current.next.next
            head = head.next
          
            if current is head:
                return True

        return False


        ''' [3,2,0,-4]
        1. current = 2, head = 0
        2. current = 0, head = 2
        3. current = -4, head = -4
        '''