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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

#iteration
#runtime o(n)
#space O(h) h is height of the tree, worst o(n), average o(logn)
#space O(h), you can imagine the stack length you only need h, becasue when it pop, it reduce the length, when tree depth increase, it increase the length.
class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = []
        res = []
        cur = root
        #find the most left leaves first
        #then check if have right for current node
        #if have right tree, then go to that tree most left leaves
        #if don't have right tree, then pop new one and save
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()    
            res.append(cur.val) 
            cur = cur.right   
        return res

if __name__=='__main__':
    root = TreeNode(val=1, left=None, right=TreeNode(val=2, left=TreeNode(val=3, left=None, right=None), right=None))
    res1 = Solution1()
    res1.inorderTraversal(root)
    res2 = Solution2()
    res2.inorderTraversal(root)



