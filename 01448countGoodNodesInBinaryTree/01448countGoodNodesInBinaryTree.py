from typing import List

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

#recursion
#runtime o(n)
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = len(self.goodNodesList(root))
        return res
    def goodNodesList(self,root:TreeNode) -> List[int]:
        if not root:
            return []
        curRootVal = root.val
        leftList = self.goodNodesList(root.left)
        rightList = self.goodNodesList(root.right)
        leftList1 = [x for x in leftList if x >= curRootVal]
        rightList1 = [x for x in rightList if x >= curRootVal]
        res = leftList1 + rightList1 + [curRootVal]
        return res


if __name__=='__main__':
    root = TreeNode(val=3, left=TreeNode(val=1,left=TreeNode(val=3)), right=TreeNode(val=4, left=TreeNode(val=1), right=TreeNode(val=5)))
    res = Solution()
    res.goodNodes(root)
    res.goodNodesList(root)



