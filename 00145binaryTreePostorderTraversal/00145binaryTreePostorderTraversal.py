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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

#iteration
#runtime o(n)
#space O(h) h is height of the tree, worst o(n), average o(logn)
#space O(h), you can imagine the stack length you only need h, becasue when it pop, it reduce the length, when tree depth increase, it increase the length.
class Solution2:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = []
        res = []
        cur = root
        #find the most right leaves first
        #then check if have left for current node
        #if have left tree, then save and go to that tree most right leaves
        #if don't have left tree, then pop new one
        #at the end reverse the list
        while stack or cur:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right
            cur = stack.pop()
            cur = cur.left   
        return res[::-1]

#iteration
#runtime o(n)
#space O(h) h is height of the tree, worst o(n), average o(logn)
#space O(h), you can imagine the stack length you only need h, becasue when it pop, it reduce the length, when tree depth increase, it increase the length.
class Solution3:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
    
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right) 
        return res[::-1]


if __name__=='__main__':
    root = TreeNode(val=1, left=None, right=TreeNode(val=2, left=TreeNode(val=3, left=None, right=None), right=None))
    res1 = Solution1()
    res1.postorderTraversal(root)
    res2 = Solution2()
    res2.postorderTraversal(root)
    res3 = Solution3()
    res3.postorderTraversal(root)


