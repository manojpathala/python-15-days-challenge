l=["manoj","mahendra","kiran kumar","jagadeesh"]
new_l=[]

for i in l:
    count_of_char=len(i)
    if count_of_char>5:
        new_l+=[i]
print(new_l)