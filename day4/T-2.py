n,x=map(int, input().split())
a=list(map(int,input().split()))
if x in a:
    print(a.count(x))
else:
    print('-1')

# count함수의 시간복잡도는 O(n)
# 처음 2의 인덱스와 초과되는 값의 인덱스값을 뺀 값이 그 수의 개수