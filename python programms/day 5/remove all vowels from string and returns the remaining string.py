string=input("enter the string:")
string=string.lower()

vowels=["e",]
resultant_string=''
for j in range(len(string)):
    if string[j] not in vowels:
        resultant_string+=string[j]
print(resultant_string)