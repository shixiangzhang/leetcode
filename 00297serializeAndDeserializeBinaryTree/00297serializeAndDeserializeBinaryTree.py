#refer https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

#Time O(N)
#Space O(N)
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def serialize_recur(root,string):
            if root is None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = serialize_recur(root.left,string)
                string = serialize_recur(root.right,string)
            return string
        return serialize_recur(root,'')
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def deserialize_recur(l):
            if l[0] == 'None':
                l.pop(0)
                return None
            root = TreeNode(l[0])
            l.pop(0)
            root.left =  deserialize_recur(l)
            root.right = deserialize_recur(l)
            return root
        
        dataList = data.split(',')
        root = deserialize_recur(dataList)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))



if __name__=='__main__':
    root = TreeNode(val=3, left=TreeNode(val=5, left=TreeNode(val=6, left=None, right=None), right=TreeNode(val=2, left=TreeNode(7), right=TreeNode(4))), right=TreeNode(val=1, left=TreeNode(0), right=TreeNode(8)))
    res = Codec()
    res1 = res.serialize(root)
    res2 = res.deserialize(res1)




