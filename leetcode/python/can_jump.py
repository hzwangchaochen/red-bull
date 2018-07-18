class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        if A is None or len(A)==0:
            return False
        if A[0]==0:
            return False
        res=[False for i in range(0,len(A))]
        res[0]=True
        for i in range(0,len(A)):
            if res[i]==False:
                return False
            if i+A[i]+1>=len(A):
                return True
            for j in range(i+1,i+A[i]+1):
                res[j]=True
        return res[len(A)-1]

if __name__ == '__main__':
    A = [3,2,1,0,4]
    solution=Solution()
    print(solution.canJump(A))

