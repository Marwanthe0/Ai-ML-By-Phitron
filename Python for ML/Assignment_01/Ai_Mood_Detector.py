str = input()
lst = str.split()
happy = ["happy","joy","smile"]
sad = ["sad","cry","angry"]
flag = True
for val in lst:
    if val.lower() in happy:
        print("Happy Mood")
        flag = false
        break
    elif val.lower() in sad:
        print("Sad Mood")
        flag = false
        break
if(flag):
    print("Neutral Mood")