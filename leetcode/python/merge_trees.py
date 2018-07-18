class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1==None and t2==None:
            return None
        t=TreeNode()
        if t1!=None:
            t.val+=t1.val
        if t2!=None:
            t.val+=t2.val
        if t1!=None and t2!=None:
            t.val=t1.val+t2.val
            t.left=self.mergeTrees(t1.left,t2.left)
            t.right=self.mergeTrees(t1.right,t2.right)
        elif t1==None:
            t.val=t2.val
            t.left=self.mergeTrees(None,t2.left)
            t.right=self.mergeTrees(None,t2.right)
        elif t2==None:
            t.val=t1.val
            t.left=self.mergeTrees(t1.left,None)
            t.right=self.mergeTrees(t2.left,None)
        return t
if __name__ == '__main__':
    tree_node=TreeNode(5)
    print(tree_node.left.left)