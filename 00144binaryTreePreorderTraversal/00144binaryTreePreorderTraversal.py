#refer https://www.pythonheidong.com/blog/article/551172/1979efbcbd93d5bff962/

from typing import List

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

#recursion
#runtime o(n)
#space O(h) h is height of the tree, worst o(n), average o(logn)
class Solution1:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

#iteration
#runtime o(n)
#space O(h) h is height of the tree, worst o(n), average o(logn)
class Solution2:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res

if __name__=='__main__':
    root = TreeNode(val=1, left=None, right=TreeNode(val=2, left=TreeNode(val=3, left=None, right=None), right=None))
    res1 = Solution1()
    res1.preorderTraversal(root)
    res2 = Solution2()
    res2.preorderTraversal(root)



