class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse_between(self, head, m, n):
        dummy=ListNode(-1)
        dummy.next=head
        cur=dummy
        for i in range(1,m):
            cur=cur.next
        pre=cur
        cur=cur.next
        for j in range(m,n):
            tmp=cur.next
            cur.next=tmp.next
            tmp.next=pre.next
            pre.next=tmp
        return dummy.next


if __name__ == '__main__':
    solution = Solution()
    node=ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    new_node=solution.reverse_between(node,1,2)
    while new_node:
        print(new_node.val)
        new_node=new_node.next


