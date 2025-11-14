inp = input()
lst = inp.split()
n = len(lst)
sum = 0.0
for val in lst:
    sum += float(val)
if((sum/n) < 85):
    print("Dark Image")
elif((sum/n) <= 170):
    print("Normal Image")
else:
    print("Bright Image")