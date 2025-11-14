key = ["ai","model","data","learn","train","neural"]
inp = input()
lst = inp.split()
count = 0
for val in lst:
    if val.lower() in key:
        count += 1
if(count >= 2):
    print("AI Detected")
else:
    print("Not AI Related")

