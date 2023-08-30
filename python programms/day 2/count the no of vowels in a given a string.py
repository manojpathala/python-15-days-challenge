string=input("enter the string:")
string=string.lower()
count=0
for i in string:
    if i=="a" or i=="e" or i=="o" or i=="u":
        count+=1
print("no of vowels:",count)
