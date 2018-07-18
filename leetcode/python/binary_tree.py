class TreeNode(object):
    def __init__(self, x,left,right):
        self.val = x
        self.left = left
        self.right = right


def pre_traversal(node):
    if node is None:
        return
    pre_traversal(node.left)
    print(node.val)
    pre_traversal(node.right)

if __name__ == '__main__':
    tree_node=TreeNode(5,TreeNode(2,TreeNode(3,None,None),TreeNode(1,None,None)),TreeNode(4,None,None))
    pre_traversal(tree_node)
