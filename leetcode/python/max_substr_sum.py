def max_substr_sum(s):
    max_sum=0
    for i in range(0,len(s)):
        sub_sum=0
        for j in range(i,len(s)):
            sub_sum+=s[j]
            if sub_sum<0:
                sub_sum=0
            if max_sum<sub_sum:
                max_sum=sub_sum
    print(max_sum)

max_substr_sum([-2,11,-4,13,-5,-2])


