inp = input()
lst = inp.split()
lst = [float(x) for x in lst]
norm = (lst[0] - lst[1])/(lst[2] - lst[1])
print(f"{norm:.2f}")