class Solution:
    def heap_sort(self,arr):
        arr_len = len(arr)
        for i in range(arr_len//2-1,-1,-1):
            self.adjust_heap(arr,i,arr_len)

        for i in range(arr_len-1,0,-1):
            self.swap(arr,0,i)
            self.adjust_heap(arr,0,i)

    def adjust_heap(self,arr,start_pos,end_pos):
        tmp = arr[start_pos]
        k = start_pos*2+1
        while k<end_pos:
            if k+1<end_pos and arr[k+1]>arr[k]:
                k+=1
            if arr[k] >tmp:
                arr[start_pos] = arr[k]
                start_pos = k
            else:
                break
            k = k*2+1
        arr[start_pos] = tmp

    def swap(self,arr,a,b):
        tmp = arr[a]
        arr[a]=arr[b]
        arr[b] =tmp
if __name__ == '__main__':
    a=[2,5,3,4,1]
    solution =Solution()
    solution.heap_sort(a)
    print(a)
