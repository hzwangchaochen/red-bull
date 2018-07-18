class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# def construct_maximum_binarytree(nums):
#     """
#     :type nums: List[int]
#     :rtype: TreeNode
#     """
#     pass

def construct_maximum_binarytree(nums,left,right):
    if left>right:
        return None
    mid=left
    max=0
    for i in range(left,right+1):
        if nums[i]>max:
            max=nums[i]
            mid=i
    tree_node=TreeNode(max)
    tree_node.left=construct_maximum_binarytree(nums,left,mid-1)
    tree_node.right=construct_maximum_binarytree(nums,mid+1,right)
    return tree_node

if __name__ == '__main__':
    nums=[3,2,1,6,0,5]
    tree_node=construct_maximum_binarytree(nums,0,5)
    print(tree_node.left.right.right.val)

