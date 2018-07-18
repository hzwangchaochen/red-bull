def insert_sorting(array):
    if array is None or len(array)==0:
        return array
    for i in range(1,len(array)):
        tmp=array[i]
        for j in range(i,-1,-1):
            if array[j-1]>tmp:
                array[j]=array[j-1]
            else:
                array[j]=tmp
                break
    return array

if __name__ == '__main__':
    print(insert_sorting([1,3,2,5,4]))