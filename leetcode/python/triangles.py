def triangles(tri):
    if tri is None or len(tri)==0:
        return 0
    if len(tri)==1:
        return tri[0][0]
    s=[0 for i in range(0,len(tri))]
    s[0]=tri[0][0]
    for i in range(1,len(tri)):
        s[i]=s[i-1]+tri[i][i]
        for j in range(i-1,0,-1):
            if s[j]>s[j-1]:
                s[j]=s[j-1]+tri[i][j]
            else:
                s[j]=s[j]+tri[i][j]
        s[0]=s[0]+tri[i][0]

    minum = s[0]

    for i in range(1,len(tri)):
        if s[i]<minum:
            minum=s[i]
    return minum



if __name__ == '__main__':
    tri=[
        [2],
        [3,4],
        [6,5,7],
        [4,1,8,3]
    ]
    print(triangles(tri))