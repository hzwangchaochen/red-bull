def quick_sort(a,left,right,kth):
    if left==right:
        return a[left]
    if left<right:
        k = a[left]
        l=left
        r=right
        while left<right:
            while a[right]>=k and left<right:
                right-=1
            if left<right:
                a[left]=a[right]
                left+=1
            while a[left]<=k and left<right:
                left+=1
            if left<right:
                a[right]=a[left]
                right-=1
        a[left]=k
        if left==kth:
            return a[left]
        elif left>kth:
            return quick_sort(a,l,left-1,kth)
        else:
            return quick_sort(a,left+1,r,kth)

if __name__ == '__main__':
    a=[5,1,4,3,2]
    print(quick_sort(a,0,len(a)-1,4))

