n=int(input("Enter the input:"))
flag=False
if n==1:
    print("number is not a prime")
if n>=2:
    for i in range(2,n):
        if n%i==0:
            flag=True
            break
    if flag :
        print("number is not a prime")
    else:
        print("number is a prime")