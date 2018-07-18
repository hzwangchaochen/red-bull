class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse_linked_list(self,root):
        dummy_node=None
        while root:
            next = root.next
            root.next = dummy_node
            dummy_node = root
            root = next
        return dummy_node

if __name__ == '__main__':
    solution = Solution()
    node=ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6,None)))))
    new_node=solution.reverse_linked_list(node)
    while new_node:
        print(new_node.val)
        new_node=new_node.next

