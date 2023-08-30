m=int(input("enter starting number:"))
n=int(input("enter ending number:"))
for number in range(m,n):
    if number>1:
        for i in range(2,number):
            if number%i==0:
                break
        else:
            print(number)

