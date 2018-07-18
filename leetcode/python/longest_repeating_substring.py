class Solution:
    """
    @param str: The input string
    @param k: The repeated times
    @return: The answer
    """
    def longestRepeatingSubsequenceII(self, str, k):
        # Write your code here
        substr_list=[]
        if str=="":
            return 0
        if k==1:
            return len(str)
        for i in range(len(str)):
            substr_list.append(str[i:])
        substr_list.sort()
        common_str_dict={}
        for i in range(len(substr_list)-1):
            self.get_common_prefix(substr_list[i],substr_list[i+1],common_str_dict)
        sorted_common_str_list =  sorted(common_str_dict.items(),key=lambda item:item[1]["length"],reverse=True)
        for sorted_common_str in sorted_common_str_list:
            if sorted_common_str[1]["times"]>=k:
                return sorted_common_str[1]["length"]
        return 0
    def get_common_prefix(self,str1,str2,common_str_dict):
        min_len = len(str1) if len(str1)<len(str2) else len(str2)
        for i in range(min_len):
            if str1[i]!=str2[i]:
                return
            else:
                if str1[:i+1] in common_str_dict:
                    common_str_dict[str1[:i+1]]["times"]+=1
                else:
                    common_str_dict[str1[:i+1]]={"times":2,"length":i+1}






if __name__ == '__main__':
    solution = Solution()
    print(solution.longestRepeatingSubsequenceII("aaa",3))


