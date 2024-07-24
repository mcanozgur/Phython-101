# is (pass by reference) vs == (pass by value)

print(True == 1)     # True
print('' == 1)       # False  string is falsey so falsey is not equalt to True (1).
print('1' == 1)      # False because fist one is string the second is integer.
print([] == 1)       # False becasue empty list is falsey so false. 
print(10 == 10.0)    # True  
print([] == [])      # True  empty array equals to empty array or list. 

# is ---> a keyword. CHECKS if the location in the memory where this value is stored is the same ! 
#All (below) are FALSE
print(True is 1)     
print('' is 1)        
print('1' is 1)      
print([] is 1)        
print(10 is 10.0)     
print([] is [])      

print(True is True)   #TRUE
print('1' is '1')     #TRUE            
print([] is [])       #TRICKY !!!   Empty list  is added in memory somewhere. But whenever we created a new list, it's created in a another location. So these are completely different lists.     
print(10 is 10.0)     #TRUE
print([1,2,3] is [1,2,3]) #FALSE. Firstly, the first list is created in somewhere in the memory. Then, another list is created but in a different location in memory. So these are not the same. 

a = [1,2,3]
b = [1,2,3]
print (a is b)   #FALSE
print(a == b)    #TRUE