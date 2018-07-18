class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_k_lists(self, lists):
        n = len(lists)
        if n == 0:
            return None
        while n>1:
            k = (n+1) / 2
            for i in range(0, n/2):
                lists[i] = self.merge_two_lists(lists[i], lists[i+k])

    @staticmethod
    def merge_two_lists(node1, node2):
        if node1 is None:
            return node2
        if node2 is None:
            return node1
        dummy_node=ListNode(0)
        node=dummy_node
        while node1 is not None and node2 is not None:
            if node1.val > node2.val:
                node.next=node1
                node1=node1.next
            else:
                node.next=node2
                node2=node2.next
            node=node.next
        if node1.next is None:
            node.next=node2
        if node2.next is None:
            node.next=node1
        return dummy_node.next







