def recursion(n):
    if n==0:
        return 1
    return n*recursion(n-1)
n=int(input("enter the input:"))
result=recursion(n)
print(result)