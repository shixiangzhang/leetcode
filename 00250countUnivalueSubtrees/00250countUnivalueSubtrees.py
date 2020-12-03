#refer https://leetcode.com/problems/count-univalue-subtrees/solution/

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

#recursion
#runtime o(n)
#space O(H)
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.count = 0
        self.isUni(root)
        return self.count

    def isUni(self, root: TreeNode) -> bool:
        res = True
        if (root.left):
            res = self.isUni(root.left) and (root.val == (root.left).val) # a and b, if a is false, then will not calculate b, so self.isUni must be first
            #res = (root.val == (root.left).val) and self.isUni(root.left)
        if (root.right):
            res =  self.isUni(root.right) and (root.val == (root.right).val) and res
            #res =  (root.val == (root.right).val) and res and self.isUni(root.right)
        if res:
            self.count += 1
        return res



if __name__=='__main__':
    root = TreeNode(val=5, left=TreeNode(val=1, left=TreeNode(val=5, left=None, right=None), right=TreeNode(val=5, left=None, right=None)), right=TreeNode(val=5, left=None, right=TreeNode(val=5, left=None, right=None)))
    res = Solution()
    res.countUnivalSubtrees(root)





