class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix(self, strs):
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        new_strs=sorted(strs)
        print(new_strs)
        a=new_strs[0]
        b=new_strs[-1]
        min_len=len(a) if len(a)<len(b) else len(b)
        res=""
        if min_len>0:
            for i in range(0,min_len):
                if a[i]==b[i]:
                    res+=a[i]
                else:
                    return res
        return res

    # write your code here

if __name__ == '__main__':
    solution=Solution()
    print(solution.longestCommonPrefix(["A","A"]))