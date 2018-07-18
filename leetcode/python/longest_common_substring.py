class Solution(object):
    def longest_common_substring(self,a,b):
        len_a=len(a)
        len_b=len(b)
        if len_a==0 or len_b==0:
            return 0
        d=[[0 for i in range(0,len_b+1)] for j in range(0,len_a+1)]
        max_len=0
        for i in range(0,len_a+1):
            for j in range(0,len_b+1):
                if i==0 or j==0:
                    d[i][j]=0
                else:
                    d[i][j]=d[i-1][j-1]+1 if a[i-1]==b[j-1] else 0
                max_len =  d[i][j] if d[i][j]>max_len else max_len
        return max_len


if __name__ == '__main__':
    solution = Solution()
    a = "ABCD"
    b = "EDCA"
    max_len=solution.longest_common_substring(a,b)
    print(max_len)