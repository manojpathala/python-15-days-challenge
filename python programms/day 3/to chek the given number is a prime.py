n=int(input("enter the number:"))
flag=False
if n==1:
    print(n,"is not a prime")
elif n>1:
    for i in range(2,n):
        if n%i==0:
            flag=True
            break
    if flag:
        print(n,"is not a prime")
    else:
        print(n,"is a prime")

