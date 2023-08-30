m=int(input("enter the starting number:"))
n=int(input("enter the ending number:"))
for number in range(m+1,n):
    if number>1:
        for i in range(2,number):
            if number%i==0:
                break
        else:
            print(number)    