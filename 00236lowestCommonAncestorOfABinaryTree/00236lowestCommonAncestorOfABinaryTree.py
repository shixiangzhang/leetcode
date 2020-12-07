#refer https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

#Mark==2 is special
#Time O(N)
#Space O(N)
class Solution:
    #def __init__(self):
        # Variable to store LCA node.
    #    self.ans = None
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = root
        def checkMarks(cur):
            nonlocal ans
            if not cur:
                return False
            m = (cur==p) or (cur==q)
            l = checkMarks(cur.left)
            r = checkMarks(cur.right)
            if m+l+r>=2:
                ans = cur
            return m or l or r
        checkMarks(root)
        return ans



if __name__=='__main__':
    root = TreeNode(val=3, left=TreeNode(val=5, left=TreeNode(val=6, left=None, right=None), right=TreeNode(val=2, left=TreeNode(7), right=TreeNode(4))), right=TreeNode(val=1, left=TreeNode(0), right=TreeNode(8)))
    res = Solution()
    test=res.lowestCommonAncestor(root,TreeNode(val=5, left=TreeNode(val=6, left=None, right=None), right=TreeNode(val=2, left=TreeNode(7), right=TreeNode(4))),TreeNode(8))





