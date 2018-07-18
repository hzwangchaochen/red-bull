import heapq
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge_k_lists(self, lists):
        heap=[]
        for list_node in lists:
            if list_node:
                heap.append((list_node.val,list_node))
        heapq.heapify(heap)
        dummy=ListNode(-1)
        res_node=dummy
        while heap:
            pop=heapq.heappop(heap)
            res_node.next=ListNode(pop[0])
            res_node=res_node.next
            if pop[1].next:
                heapq.heappush(heap,(pop[1].next.val,pop[1].next))
        return dummy.next

if __name__ == '__main__':
    list_node1=ListNode(1,ListNode(2,ListNode(5)))
    list_node2=ListNode(2,ListNode(4,ListNode(6)))
    lists=[list_node1,list_node2]
    soluition=Solution()
    res=soluition.merge_k_lists(lists)
    while res:
        print(res.val)
        res=res.next





