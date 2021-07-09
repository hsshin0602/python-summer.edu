n=int(input())
a=list(map(int,input().split()))
b=[]
cnt=0
for i in range(n+1):
    b.append(a.count(i))
print(b)
for j in range(1,len(b)):
    try:
        if b[j]//j!=0:
            cnt=cnt+(b[j]//j)
            b[j+1]+=b[j]%j
    except ZeroDivisionError:
        pass
print(cnt)
#시간 복잡도는 O(n)