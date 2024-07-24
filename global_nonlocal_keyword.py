# global keyword

a = 10
def confusion(b):
    print(b)
    a = 90
confusion(300)        #as expected, 300 is printed.  

#example: 

#total = 0

#def count():
   #total += 1
   #return total

#print(count())          #cannot access local variable total. çalışmaz.

#example: 
total = 0

def count(total):
   total += 1
   return total

print(count(total))     #it prints 1.

#example
def count():
    total = 0
    total += 1          #total was 0, then 1 is increased and it becomes 1.
    return total        #1 is returned when function is called.

print(count())   

#example
def count():
    total = 0
    total += 1          #total was 0, then 1 is increased and it becomes 1.
    return total
count()                      
count()
count()
print(count())       #1 is printed since total is always 0 when function is called.

#GLOBAL KEYWORDS    --> variable is UPDATED.

total = 0
def count():
    global total      #accessing variables outside of the function, we can use global kywords.
    total += 1       
    return total
count()                #when count() function is called, total will be 1.            
count()                #when count() function is called, total will be 2 because with global total, total was taken as 1. 
count()                #when count() function is called, total will be 3 because with global total, total was taken as 2. 
print(count())         #when count() function is called, total will be 4 because with global total, total was taken as 3. 

# exercise:

total = 0

def count(total):
    total += 1             
    return total

count(total)                #total 1              
count(total)                #total 1
count(total)                #total 1
print(count(total))         #total 1


#exercise: instead of global keywords;

total = 0

def count(total):               #update etmesi için global keyword yerine fonksiyon içerine vazıp burdan update ettirirsin!!!!
    total += 1       
    return total
           
print(count(count(count((total)))))  
                         #total was 0, then total becomes 1. 
                 #count(1) will return 2.
           #count(2) will return 3.
      #count(3) will return 4. 


#nonlocal keyword:

def outer():
    x = 'local'
    def inner():
        nonlocal x             #not in local --> parent x is modified with new one. Here, new x  = 'nonlocal'
        x = 'nonlocal'
        print('inner:', x)     #inner, nonlocal yazar.

    inner()                    #call inner function here.
    print('outer:', x)         #outer, nonlocal --> because outer is also modified from local to nonlocal. 
outer()                        

#NONLOCAL keyword:

def outer():
    x = 'local'
    def inner():
        # nonlocal x           #if we do not write nonlocal x here, then parent x stay same. so parent x = local.
        x = 'nonlocal'
        print('inner:', x)     #inner, nonlocal yazar.

    inner()                    #call inner function here.
    print('outer:', x)         #outer, local --> beucase parent is not modified.

outer()    #we call the outer function


# when we use NONLOCAL KEYWORD -->  we write new thing for the known variable. 
# new memory area is not produced. The available memory region is used.
# BUT, when we do not use nonlocal keyword --> the new memeory area is formed and this variable is stored here.
# when programmes become larger and larger, the memory can be problem. So we can use this nonlocal kywrds.

# when a function is done, the phyton interpreter destroys all this memory. 
# once we finish the outer function, I cannot call print x value. Because x is in the function.
# when we call  a function, we also call the garbage collector. 
#remember, it we want to print a varibale which is stored in a function, this variable cannot be printed.


