# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    #recursive solution with a bottom-up approach (or leaf to root approach)
    def isBalanced(self, root):
        #helper function for the recursion
        def dfs(root):
            #base case (if there is no root, it is balanced and has a height of 1)
            if not root: return [True, 0]
            #starting the recursion function (takes the left and right child of each node)
            left, right = dfs(root.left), dfs(root.right)
            #checks if it is balance by taking the difference between subtrees
            #a "balanced binary tree" is when the leaf nodes have a max diff in height of 1
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]
