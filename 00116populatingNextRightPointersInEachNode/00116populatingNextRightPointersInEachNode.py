#refer https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

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
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        curLvlLeftMost = root
        while curLvlLeftMost.left:
            head = curLvlLeftMost
            while head:
                #connection 1
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            curLvlLeftMost = curLvlLeftMost.left
        return root



if __name__=='__main__':
    root = Node(val=1, left=Node(val=2, left=Node(val=4, left=None, right=None), right=Node(val=5, left=None, right=None)), right=Node(val=3, left=Node(val=6, left=None, right=None), right=Node(val=7, left=None, right=None)))
    res = Solution()
    test=res.connect(root)





