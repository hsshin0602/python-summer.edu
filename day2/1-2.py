n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(len(a)):
    for j in range(i+1,n):
        if a[i] < a[j]:
            b.append(j)
            break
print(b)
#인덱스를 굳이 따로 선언할 필요없이 for문으로 돌리면
#i 자체가 인덱스로써의 역할을 함
'''
ind=[]
b=[]
for i in a:
    ind.append(a.index(i))
i=-1
for j in a:
    i+=1
    for k in range(1,n):
        if j < a[k] and ind[k] >i:
            b.append(ind[k])
            break
print(b)
'''
