class TreeNode:
    def __init__(self, val,left=None,right=None):
        self.val = val
        self.left, self.right = left, right


class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """

    def levelOrder(self, root):
        if root is None:
            return []
        queue = [root]
        res = []
        while len(queue) > 0:
            tmp = []
            tmp_queue = []
            for node in queue:
                tmp.append(node.val)
                if node.left:
                    tmp_queue.append(node.left)
                if node.right:
                    tmp_queue.append(node.right)
            res.insert(0,tmp)
            queue = tmp_queue
        return res

if __name__ == '__main__':
    solution=Solution()
    root=TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
    print(solution.levelOrder(root))

