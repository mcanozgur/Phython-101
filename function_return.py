#return

# a function do one thing very well.
# a function should return something. 
# some functions may not have return, but to make readible --> we need to add return.


def sum(num1, num2):
    num1 + num2 

print(sum(4,5))   #we call the function --> but inside function no print. So we need to print this function here. 

#Some methods give NONE. In that condition we write the method firstly, then we print it. (remeber methods in list; remove, append, extend, etc. These methods --> NOT RETURN
#In lists, pop method--> RETURN  print(x.pop()) --> not write NONE

def sum(num1, num2):
    return num1 + num2 #when return comes, it means EXIT. 

print(sum(4,5))

#functions can make one more than 1 task. print hii -is 1st task, sum is 2nd function.

def sum(num1, num2):
    print('hiii')       #when we call this function --> it will print Hii
    num1 + num2         #Not return, so the sum of num1 and num2 will not be printed

print(sum(4,5))         #it print hiii. and None

##
def sum(num1, num2):
    return num1 + num2

total = sum (10,5)         # for total sum function will be done, and return as 15. 
print(sum(10,total))       # again sum function is called. 
print(sum(10, sum(10,15))) # 35.

def sum(num1, num2):                 # we define a sum funtion 
    def another_func(num1, num2):    # then we define another function. 
        return num1 + num2           
    # return another_func(num1, num2) #when we add this return then sum func. will work.

total = sum(10, 20)

print(total)                        # it will print None because we should return another function to call sum function 

##
def sum(num1, num2):                 # we define a sum funtion 
    def another_func(num3, num4):    # then we define another function. 
        return num3 + num4
    a = another_func(21, 22)
    print(a)                         # it will print 43, 44. 
    return a + 1

total = sum(10, 20)

print(total) 

    