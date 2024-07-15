a=10
#in the above the variabel a=10 is global variabel
def ftn():
    a=9
    print(a)
    #in this inside the function a=9 is a local  variable
ftn()
print(a)
# lets write another function to channge local variable which is inside is changed to global variable using a keyword as global
a=11

def func():
    
    global a 
    
    print(a)
    b=3
    #here b is printed as a local variable
    print(b)

    print(a,b)
    #changing global variables values with assign a new value using globals as keyword
    globals()['a']=10
    print(a,b)
func()
print(a)