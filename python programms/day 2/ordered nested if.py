n=int(input())
for i in range(1,n+1):
    result=""
    for j in range(i):
        result+=str(j+1)+" "
    print(result)