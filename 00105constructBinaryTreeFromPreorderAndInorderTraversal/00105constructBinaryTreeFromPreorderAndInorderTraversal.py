#refer https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/solution/

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

#runtime o(n)
#space O(n)
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(in_left,in_right):
            if in_left>in_right:
                return None
            val = postorder.pop()
            root = TreeNode(val)
            idx = idxMap[val]
            root.right = helper(idx+1,in_right)
            root.left = helper(in_left,idx-1)
            return root
        idxMap = {val:idx for idx,val in enumerate(inorder)}
        return helper(0,len(inorder)-1)



if __name__=='__main__':
    #root = TreeNode(val=5, left=TreeNode(val=1, left=TreeNode(val=5, left=None, right=None), right=TreeNode(val=5, left=None, right=None)), right=TreeNode(val=5, left=None, right=TreeNode(val=5, left=None, right=None)))
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    res = Solution()
    test=res.buildTree(inorder,postorder)





