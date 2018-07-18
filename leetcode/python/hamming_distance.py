

def hamming_distance(x,y):
    res=0
    for i in range(0,32):
        val=1<<i
        if x<val and y<val:
            break
        print(x&val)
        print(y&val)
        if x&val != y&val:
            res+=1
    print(res)




if __name__ == '__main__':
    hamming_distance(1,4)