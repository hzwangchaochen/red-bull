import heapq
class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        if A is None or len(A)==0:
            return None
        heapq.heapify(A)
        for i in range(len(A)-k):
            heapq.heappop(A)
        return heapq.heappop(A)

if __name__ == '__main__':
    solution = Solution()
    print(solution.kthLargestElement(1,[5,4,3,2,1]))
