n = int(input())
count = 0
for i in range(n):
    str = input()
    if(str == "YES"):
        count += 1
    else:
        count -= 1
if(count >= 0):
    print("ACCEPT")
else:
    print("REJECT")
