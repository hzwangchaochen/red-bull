class Solution(object):
    def partition_labels(self, S):
        res = []
        if S is None:
            return []
        num=0
        for index,letter in enumerate(S):
            if S.rfind(letter)>num:
                num=S.rfind(letter)
            if index==num:
                sub_res=0
                if len(res)>0:
                    for i in res:
                        sub_res+=i
                res.append(num+1-sub_res)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.partition_labels("ababcbacadefegdehijhklij"))
