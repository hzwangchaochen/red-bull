class Solution(object):
    def customSortString(self, S, T):
        sort_letter = {}
        for index, letter in enumerate(S):
            sort_letter[letter] = index
        str_array = [T[i] for i in range(0, len(T))]

        len_t = len(str_array)
        for i in range(1, len_t):
            if str_array[i] not in sort_letter:
                continue
            #if sort_letter[str_array[i - 1]] > sort_letter[str_array[i]]:
            tmp = str_array[i]
            # j=i
            # while j>0 and sort_letter[str_array[j-1]]>sort_letter[tmp]:
            #     str_array[j]=str_array[j-1]
            #     j-=1
            # str_array[j]=tmp
            for j in range(i, -1, -1):
                if j == 0:
                    str_array[j] = tmp
                    break
                if str_array[j - 1] not in sort_letter or sort_letter[str_array[j - 1]] > sort_letter[tmp]:
                    str_array[j] = str_array[j - 1]
                else:
                    str_array[j] = tmp
                    break
        return ''.join(str_array[i] for i in range(0,len(str_array)))


if __name__ == '__main__':
    solution = Solution()
    print(solution.customSortString("cad", "abcd"))
