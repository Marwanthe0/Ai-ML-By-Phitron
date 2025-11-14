inp = input()
lst = inp.split()
lst = [int(x) for x in lst]
if(lst[0] >= lst[1]):
    print("ON")
else:
    print("OFF")