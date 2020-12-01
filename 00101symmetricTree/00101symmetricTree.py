#refer https://github.com/MisterBooo/LeetCodeAnimation/blob/master/0101-Symmetric-Tree/Article/0101-Symmetric-Tree.md

from typing import List

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

#recursion
#runtime o(n)
#space O(n)
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isSym(root.left, root.right)

    def isSym(self, l:TreeNode,r:TreeNode) -> bool:
        if (not l) and (not r):
            return True
        if (not l) or (not r):
            return False
        res = (l.val == r.val) and self.isSym(l.left, r.right) and self.isSym(l.right,r.left)
        return res



if __name__=='__main__':
    root = TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=3, left=None, right=None), right=TreeNode(val=4, left=None, right=None)), right=TreeNode(val=2, left=TreeNode(val=4, left=None, right=None), right=TreeNode(val=3, left=None, right=None)))
    res = Solution()
    res.isSymmetric(root)





