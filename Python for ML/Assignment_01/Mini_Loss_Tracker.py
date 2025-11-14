n = int(input())
target = float(input())
sum = 0.0
for i in range(n):
    x = float(input())
    sum += x
if((sum / n) <= target):
    print("PASS")
else:
    print("RETRY")