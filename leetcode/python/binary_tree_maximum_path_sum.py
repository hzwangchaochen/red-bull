class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def __init__(self):
        self.max_num=0

    def maxPathSum(self, root):
        if root is None:
            return 0
        self.helper(root)
        return self.max_num

    def helper(self,root):
        if root:
            left=self.helper(root.left)
            right=self.helper(root.right)
            local_max=root.val+left+right
            if local_max>self.max_num:
                self.max_num=local_max
            return (root.val+left) if left>right else (root.val+right)
        else:
            return 0



if __name__ == '__main__':
    solu