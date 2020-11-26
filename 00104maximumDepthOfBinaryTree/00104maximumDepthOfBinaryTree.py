#refer https://github.com/MisterBooo/LeetCodeAnimation/blob/master/0104-Maximum-Depth-Of-Binary-Tree/Article/0104-Maximum-Depth-Of-Binary-Tree.md
#时间复杂度：O(n), 我们每个结点只访问一次，因此时间复杂度为 O(N)
#空间复杂度：
#最坏情况下，树是完全不平衡的，例如每个结点只剩下左子结点，递归将会被调用 N 次（树的高度），因此保持调用栈的存储将是 O(N)。
#最好情况下（树是完全平衡的），树的高度将是 log(N)。因此，在这种情况下的空间复杂度将是 O(log(N))


from typing import List

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


#recursion
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = max(self.maxDepth(root.left), self.maxDepth(root.right))+1
        return res


if __name__=='__main__':
    root = TreeNode(val=3, left=TreeNode(val=9, left=None, right=None), right=TreeNode(val=20, left=TreeNode(val=15, left=None, right=None), right=TreeNode(val=7, left=None, right=None)))
    res1 = Solution()
    res1.maxDepth(root)



