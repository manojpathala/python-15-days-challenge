string=input("enter the sentence:")
for i in string:
    if i[0].isupper():
        print("pangram")
        break;
    else:
        print("not a pangram")
        break;