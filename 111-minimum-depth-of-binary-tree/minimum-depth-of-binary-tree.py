# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        minD, stack = float('inf'), [[root, 1]]
    
        while stack:
            currentNode, level = stack.pop()
            if currentNode:
                if not currentNode.left and not currentNode.right:
                    minD = min(minD, level)
                else:
                    stack.append([currentNode.left, level + 1])
                    stack.append([currentNode.right, level + 1])
        
        return minD if root is not None else 0