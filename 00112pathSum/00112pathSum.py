#refer https://leetcode.com/problems/path-sum/solution/

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

#recursion
#runtime o(n)
#space O(h), best case O(log(N)) with balance tree, worst case O(N)
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        targetSum = sum - root.val
        if (not root.left) and (not root.right) and (targetSum == 0):
            return True
        return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum)

if __name__=='__main__':
    root = TreeNode(val=5, left=TreeNode(val=4, left=TreeNode(val=11, left=TreeNode(val=7, left=None, right=None), right=TreeNode(val=2, left=None, right=None)), right=None), right=TreeNode(val=8, left=TreeNode(val=13, left=None, right=None), right=TreeNode(val=4, left=None, right=TreeNode(val=1, left=None, right=None))))
    res = Solution()
    res.hasPathSum(root,22)





