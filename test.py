f = open('que.txt', 'r')
lis=[] 
for line in f:
    lis.append(line)
lis = [line.rstrip() for line in lis]
print (lis)