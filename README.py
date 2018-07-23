# 矩阵循环
#!/bin/python3

nd=input().split(" ");
n=int(nd[0])
d=int(nd[1])
a=list(map(int,input().rstrip().split()))
b=[]
for i in range(n):
    b.append(i)

if d%n==0:
    for i in range(n):
        print(a[i],end=' ')
      
else:
    A=d%n;
    for j in range(n):
        B=A+j
        if B>=n:
            b[j]=a[B-n];
        else:
            b[j]=a[B]

    for i in range(n):
        print(b[i],end=' ')
