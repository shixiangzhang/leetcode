from typing import List

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

#recursion
#runtime O(n^2), List Comprehensive part is O(n)
class Solution1:
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

#recursion
#runtime O(n)
class Solution2:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0 # good variable using self
        curMax = root.val
        def countGoodNodesWithMax(root: TreeNode,curMax:int) -> int: #no self in arguments
            if not root:
                return self.res          
            if root.val>=curMax:
                curMax = root.val
                self.res += 1
            countGoodNodesWithMax(root.left,curMax)
            countGoodNodesWithMax(root.right,curMax)
            return self.res
        return countGoodNodesWithMax(root,curMax)


if __name__=='__main__':
    root = TreeNode(val=3, left=TreeNode(val=1,left=TreeNode(val=3)), right=TreeNode(val=4, left=TreeNode(val=1), right=TreeNode(val=5)))
    res = Solution2()
    res.goodNodes(root)
    res.goodNodesList(root)



