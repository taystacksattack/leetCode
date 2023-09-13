# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        '''
        sum, stack = 0 , [[root, 0]]

        while stack:
            currentNode, currentSum = stack.pop()
            if currentSum == targetSum and not currentNode.left and not currentNode.right : 
                return true

            stack.append([currentNode.left, currentSum + currentNode.val])
            stack.append([currentNode.right, currentSum + currentNode.val])
            
        return false
            

        '''
        if not root: return False
        sum, stack = 0 , [[root, 0]]

        while stack:
            currentNode, currentSum = stack.pop()
            print("here go that current sum", currentSum)

            if currentNode.left: stack.append([currentNode.left, currentSum + currentNode.val])
            if currentNode.right: stack.append([currentNode.right, currentSum + currentNode.val])
            if (currentNode.val + currentSum) == targetSum and not currentNode.left and not currentNode.right : 
                return True
            
        return False