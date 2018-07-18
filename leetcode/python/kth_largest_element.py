class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        if A is None or len(A)==0:
            return None
        return self.find_kth(A,0,len(A)-1,len(A)-k)
    def find_kth(self,A,left,right,k):
        if left==right:
            return A[left]
        if left<right:
            l=left
            r=right
            tmp=A[l]
            while l<r:
                while A[r]>=tmp and r>l:
                    r-=1
                if r>l:
                    A[l]=A[r]
                    l+=1
                while A[l]<=tmp and r>l:
                    l+=1
                if r>l:
                    A[r]=A[l]
                    r-=1
            A[l]=tmp
            if l==k:
                return A[l]
            elif l>k:
                return self.find_kth(A,left,l-1,k)
            else:
                return self.find_kth(A,l+1,right,k)