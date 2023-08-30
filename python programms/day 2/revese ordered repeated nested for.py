n=int(input())
for i in range(1,n+1):
    result=''
    for j in range(i):
        result+=str(n+1-i)+" "
    print(result)