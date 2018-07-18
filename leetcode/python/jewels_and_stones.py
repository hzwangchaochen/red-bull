def num_jewels_in_stones(J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """
    res=0
    for letter in S:
        if letter in J:
            res+=1
    return res

