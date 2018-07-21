#stdin
import sys
# counter = 1
# while True:
#     line = sys.stdin.readline()
#     if not line:
#         break
#     print("%s:%s" % (counter,line))
#     counter += 1
#
# #stdout
# for i in range(3):
#     sys.stdout.write('Dive in')
#
# #stderr
# for i in range(3):
#     sys.stderr.write('Dive in')
#
# #redirection
# saveout = sys.stdout
# fsock = open('out.log', 'w')
# sys.stdout = fsock
# print('This message will be logged instead of displayed')
# sys.stdout = saveout
# fsock.close()

#
f=open('test.txt','a+')
a='123'
print(a, file=f)
f.close()