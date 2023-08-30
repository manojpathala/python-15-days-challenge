n=input()
n=n.upper()
s=0

for i in n:
    if i=="A":
        s+=1
    elif i=="B":
        s+=10
    elif i=="C":
        s+=100
    elif i=="D":
        s+=1000
    elif i=="E":
        s+=10000
    elif i=="F":
        s+=100000
    elif i=="G":
        s+=1000000
    else:
        None
print(s)
