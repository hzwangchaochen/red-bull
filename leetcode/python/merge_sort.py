class Solution:
    def merge_sort(self, a, left, right):
        if a is None or len(a) == 0:
            return
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(a, left, mid)
            self.merge_sort(a, mid + 1, right)
            self.merge_two_list(a, left, mid, right)

    def merge_two_list(self, a, left, mid, right):
        tmp = []
        l = left
        r = mid + 1
        while l <= mid and r <= right:
            if a[l] <= a[r]:
                tmp.append(a[l])
                l += 1
            else:
                tmp.append(a[r])
                r += 1
        while l <= mid:
            tmp.append(a[l])
            l += 1
        while r <= right:
            tmp.append(a[r])
            r += 1
        a[left:right + 1] = tmp


if __name__ == '__main__':
    a = [5, 2, 4, 1, 3]
    solution = Solution()
    solution.merge_sort(a, 0, 4)
    print(a)
