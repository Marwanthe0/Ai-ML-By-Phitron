inp = input()
lst = inp.split()
a,b = 0,0
for val in lst:
    if(val == 'A'):
        a += 1
    else:
        b +=1
n = a + b
if((a/n) > 0.7 or (a/n) < 0.3):
    print("Biased Model")
else:
    print("Fair Model")