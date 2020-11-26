#refer https://www.pythonheidong.com/blog/article/551172/1979efbcbd93d5bff962/

from typing import List

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


#iteration
#runtime o(n)
#space O(n)
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        cur = [root]
        while cur:
            layval = []
            lay = []
            for node in cur:
                layval.append(node.val)
                if node.left: lay.append(node.left)
                if node.right: lay.append(node.right)
            cur = lay
            res.append(layval)
        return res


if __name__=='__main__':
    root = TreeNode(val=3, left=TreeNode(val=9, left=None, right=None), right=TreeNode(val=20, left=TreeNode(val=15, left=None, right=None), right=TreeNode(val=7, left=None, right=None)))
    res1 = Solution()
    res1.levelOrder(root)



