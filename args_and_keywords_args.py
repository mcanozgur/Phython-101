# arguments and keywords arguments

#arguments are used when we call the function.
#parameters: we used to define function.

#def super_func(args):         
  #  return sum(args)

#print(super_func(1,2,3,4,5))      #error: 1 parameter is defined, but we write 5 arguments.  

# w/ one parameter, we can write more than one arguments using *. (remember * from the lists, *others refers to more than 1 data in lists)

def super_func(*args):         
    return sum (args)

print(super_func(1,2,3,4,5))

def super_func(*args):
    print(args)         #it will print all args           
    return sum(args)    #it will return sum.

print(super_func(1,2,3,4,5))   # it prints (1,2,3,4,5) and 15

#if we want to write all args w/o () --> then we write print(*args) 

def super_func(*args):
    print(*args)              
    return sum(args)

print(super_func(1,2,3,4,5))    #1 2 3 4 5 and 15

# w/ a single * --> we can write more than 1 argument.
# w/ two ** --> we can write more than one keyword argument.

def super_func(*args, **kwargs):
    print(kwargs)       # written keyword arguments will be printed when we call this function.
    total = 0
    for items in kwargs.values():   #items keyword arguments will be sum. 
        total = total + items                     
    return sum(args) + total        #then, sum of args and keyword args values will be collected and returned.

print(super_func(1,2,3,4,5, num1=5, num2=2)) 

# Order of parameters: 
# parameters, *args, default parameters, **kwargs

def super_func(name, *args, m='melike', **kwargs):
    print(kwargs) 
    print(m)
    total = 0
    for items in kwargs.values():
        total = total + items                     
    return sum(args) + total 

print(super_func('Guvo', 1,2,3,4,5,  m = 'ahmet', num1=5, num2=2)) #guvo falan yazmadı 


#exercise: find the largest even number in list.

def highest_even(*numbers_oflist):
    evens =[]
    for item in numbers_oflist:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)

print(highest_even(10,2,3,4,8,11))
