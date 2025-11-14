n, m, k = (int(x) for x in input().split())
data = list(map(int, input().split()))
d2 = [0 for i in range(n)]
for i in range(m):
    a, b, c = tuple(map(int, input().split()))
    d2[a - 1] += c;
    if b < n:
       d2[b] -= c;
for i in range(1,n):
    d2[i] += d2[i - 1]
for i in range(n):
    data[i] += d2[i]

data = sorted(data,reverse= True)
# print(data)
qu = list(map(int,input().split()))
for val in qu:
    print(data[val - 1],end = " ")
# 5 9 2 3 10
# 15 19 12 3 10
# 15 22 15 6 13
# 15 22 15 12 19