n=int(input())
for i in range(1,n+1):
    result=''
    for j in range(i,0,-1):
        result+=str(j)+" "
    print(result)