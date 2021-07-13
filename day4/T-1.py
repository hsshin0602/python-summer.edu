x=int(input())
a=list(map(int, input().split()))
y=int(input())
b=list(map(int, input().split()))
for i in range(y):
    if a.count(b[i])==True:
        print('yes',end=' ')
    else:
        print('no', end=' ')