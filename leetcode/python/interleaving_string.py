def interleaving_string(s1,s2,s3):
    len_s1=len(s1)
    len_s2=len(s2)
    len_s3=len(s3)
    res_matrix=[[False for i in range(0,len_s1+1)] for j in range(0,len_s2+1)]
    if (len_s1+len_s2) != len_s3:
        return False
    if (len_s1==0 and s2!=s3) or (len_s2==0 and s1!=s3):
        return False
    res_matrix[0][0]=True
    for i in range(1,len_s1+1):
        if s1[i-1]!=s3[i-1]:
            break
        else:
            res_matrix[0][i]=True
    for j in range(1,len_s2+1):
        if s2[j-1]!=s3[j-1]:
            break
        else:
            res_matrix[j][0]=True
    for i in range(1,len_s2+1):
        for j in range(1,len_s1+1):
            if res_matrix[i-1][j] and s2[i-1]==s3[i-1+j]:
                res_matrix[i][j]=True
            elif res_matrix[i][j-1] and s1[j-1]==s3[j-1+i]:
                res_matrix[i][j]=True
    return res_matrix[len_s2][len_s1]

if __name__ == '__main__':
    print(interleaving_string("aabcc","dbbca","aadbbbaccc"))