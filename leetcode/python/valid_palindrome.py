import re
class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        pattern=r"[0-9a-zA-Z]"
        re_pattern=re.compile(pattern)
        len_s=len(s)
        if len_s=="":
            return True
        left, right = 0, len_s-1
        while left<=right:
            while left<len_s and re_pattern.match(s[left]) is None:
                left+=1
            while right>=0 and re_pattern.match(s[right]) is None:
                right-=1
            if left<=right:
                if s[left].lower()!=s[right].lower():
                    return False
            left+=1
            right-=1
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(" "))
