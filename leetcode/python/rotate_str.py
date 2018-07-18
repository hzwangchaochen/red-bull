class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def reverse(self, str, s, e):
        i = s; j = e
        while i < j:
            str[i], str[j] = str[j], str[i]
            i += 1
            j -= 1
    def rotateString(self, str, offset):
        # write your code here
        length = len(str)
        if str:
            while offset >= length:
                offset %= length
            if offset:
                self.reverse(str, 0, length - 1)
                self.reverse(str, 0, offset - 1)
                self.reverse(str, offset, length - 1)

if __name__ == '__main__':
    solution=Solution()
    test_str="abcdefg"
    test_str=[i for i in test_str]
    print(test_str)
    solution.rotateString(test_str,3)
    print(test_str)
