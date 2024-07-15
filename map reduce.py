from functools import reduce

# for exaple lets taking a list then do our required operations
li=[3,5,2,9,6,8,1]
#in the above list we want even numbers list
odd=list(filter(lambda a:a%2!=0,li))
# the lambda is a function to do a simple operation without writing a def keyword fuction
print(odd)
adding=list(map(lambda a:a+2,odd))
#the above mapping is used to add a number to the whole list
print(adding)
#reduce is used to shorten the output to make a operation inside the list
reducing=reduce(lambda a,b:a+b,adding)
print(reducing)