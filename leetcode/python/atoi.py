import re
def atoi(str):
    i = int(str)
    if i>2147483647:
        return 2147483647
    if i<-2147483648:
        return -2147483648
    return i

print(atoi("123123123123123"))