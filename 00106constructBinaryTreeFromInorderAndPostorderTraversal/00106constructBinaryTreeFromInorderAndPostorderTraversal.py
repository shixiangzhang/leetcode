#refer https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

#runtime o(n)
#space O(n)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(in_left,in_right):
            if in_left>in_right:
                return None
            nonlocal preIdx
            val = preorder[preIdx]
            root = TreeNode(val)
            idx = idxMap[val]
            preIdx += 1
            root.left = helper(in_left,idx-1)
            root.right = helper(idx+1,in_right)
            return root
        preIdx = 0
        idxMap = {val:idx for idx,val in enumerate(inorder)}
        return helper(0,len(inorder)-1)



if __name__=='__main__':
    #root = TreeNode(val=5, left=TreeNode(val=1, left=TreeNode(val=5, left=None, right=None), right=TreeNode(val=5, left=None, right=None)), right=TreeNode(val=5, left=None, right=TreeNode(val=5, left=None, right=None)))
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    res = Solution()
    test=res.buildTree(preorder,inorder)





