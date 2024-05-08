import math,random

n=3
v=[]

for i in range(n):
    v.append([])
    for j in range(n):
        v[i].append(random.randint(-2,5))
print(v)

def diognal_changer(d):
    for x in range(len(d)):
        for k in range(len(d)):
            if d[x][k]<0:
                d[x][k]=0
            elif d[x][k]:
                d[x][k]=1
    return d

ret=diognal_changer(v)

print(ret)
    