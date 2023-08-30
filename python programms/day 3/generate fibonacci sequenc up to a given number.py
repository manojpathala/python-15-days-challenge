nth_term=int(input("enter the nth term:"))
n1,n2=0,1
print("fibonacci series are:",n1,n2,end=" ")
for i in range(2,nth_term):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")

print()