import re


class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def ugly_num(self, index):
        ugly_num_list = [1]
        next_index = 1
        multipy_2 = 0
        multipy_3 = 0
        multipy_5 = 0
        while next_index < index:
            next_ugly_num = self.min(ugly_num_list[multipy_2] * 2, ugly_num_list[multipy_3] * 3, ugly_num_list[multipy_5] * 5)
            ugly_num_list.append(next_ugly_num)
            next_index += 1
            if next_ugly_num==ugly_num_list[multipy_2] * 2:
                multipy_2 += 1
            if next_ugly_num==ugly_num_list[multipy_3] * 3:
                multipy_3 += 1
            if next_ugly_num==ugly_num_list[multipy_5] * 5:
                multipy_5 += 1
        return ugly_num_list

    def min(self,a,b,c):
        min2 = a if a<b else b
        return min2 if min2<c else c

if __name__ == '__main__':
    solution = Solution()
    print(solution.ugly_num(20))
