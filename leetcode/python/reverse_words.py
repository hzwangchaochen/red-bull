class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        # write your code here
        if s is None:
            return None
        len_s=len(s)
        if len_s<2:
            return s

        arr_s=[i for i in s.split(" ")]
        self.reverse_arr(arr_s)
        return " ".join(arr_s)

    def reverse_arr(self,arr):
        len_arr=len(arr)
        for i in range(0,len_arr/2):
            arr[i],arr[len_arr-1-i]=arr[len_arr-1-i],arr[i]