#refer https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

# Definition for a binary tree node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

#runtime o(n)
#space O(1)
class Solution:
    def updateChildNode(self, childNode, prev, leftMost):
        if childNode:
            if prev:
                prev.next = childNode
            else:
                leftMost = childNode
            prev = childNode
        return prev,leftMost
    
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        leftMost = root
        while leftMost:
            cur = leftMost
            prev = None
            leftMost = None
            while cur:
                prev,leftMost = self.updateChildNode(cur.left,prev,leftMost)
                prev,leftMost = self.updateChildNode(cur.right,prev,leftMost)
                cur = cur.next
        return root



if __name__=='__main__':
    root = Node(val=1, left=Node(val=2, left=Node(val=4, left=None, right=None), right=Node(val=5, left=None, right=None)), right=Node(val=3, left=Node(val=6, left=None, right=None), right=Node(val=7, left=None, right=None)))
    res = Solution()
    test=res.connect(root)





