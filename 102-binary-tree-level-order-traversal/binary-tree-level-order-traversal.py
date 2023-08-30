# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = deque()
        queue.append(root)
        
        while queue:
            queueLen = len(queue)
            level = []
            for i in range(queueLen):
                ele = queue.popleft()
                if ele:
                    level.append(ele.val)
                    if ele.left: queue.append(ele.left)
                    if ele.right: queue.append(ele.right)
            if level:
                result.append(level)
        return result
            