import heapq


class Solution:

    def heap_sort(self, a):
        if a is None or len(a)<=1:
            return a
        heapq.heapify(a)
        print(a)
        a.pop()
        print(a)
        print(heapq.heappop(a))
        return a

if __name__ == '__main__':
    a=[2,3,1,6,4]
    solution = Solution()
    solution.heap_sort(a)

