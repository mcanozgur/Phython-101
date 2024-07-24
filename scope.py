#scope : what variables do I have to access. 

#print(name())   # error. name is not available as a variable. Not defined before. 

#we create a variable if it IS NOT INSIDE OF FUNCTION, it is part of GLOBAL SCOPE, WE CAN ACCESS TO IT.

def some_func():
    total = 100
    return 

some_func()   #it will print 100. 100 is assigned into total variable, and total variable is in the some_func.

#print(total) # this total -- not recognized because total variable is in some_func. so just sone_func can recognize this total variable. 

total = 100
print(total)      # we determine a total variable, now this total can be printed.

# exercise: 
a = 1

def confusion():
    a = 5 
    return a

print(a)              # a  =1 is recognized and so 1 will be printed
print(confusion())    # this will recognized inside function. 
print(confusion)      # it will print the storage area of function in memory.

##

#rules of scopes: 
# 1 --> start w/ local. In a function, firslty, local scope, variable is searched. 
# 2 --> if it is not in the local, is there a parent local scope. If variable is not exist in a function, then parent function is searched. 
# 3 --> if it is not in local parent, then outside function, GLOBAL SCOPE will be searched. 
# 4 --> built in python functions. 

# rule 1 example: 
def confusion():
    b = 2
    return b

print(confusion())     # local variable is available, so it is recognized.  

#rule 2 example:
def parent():
    a = 10
    def confusion():
        return a       # a variable is not available in local function, so parent function is searched. 
    return confusion()        

print(parent())        # print 10. Start w/ local scope, then is there a parent scope. Yes there is a parent scope of parent function.
    
#rule 3 example:
x = 3
def parent():
    def confusion():
        return x        # x is not available in the local and parent functions, so GLOBAL SCOPE is searched. 
    return confusion()  # confusion should be returned to call the def parent(). 

print(parent())         #global scope; 3 is printed.

#example:

total = 57

def new_func():
    return total

print(new_func())     # total is not available in local function, so global scope will be printed if it is available. 


#rule 4 example: 

def parent():
    def confusion():
        return sum           
    return confusion()        

print(parent()) #it prints <built-in function sum> 
