# Augmented Assignment Operator

# instead of many variable in a code, you can use the same variable name. But each time assigned thing on the same variable will be changed !
# the same variable name is used to avoid taking up memory space. 

some_value = int(input('what is the smallest even number'))   #it should changed to integer. 

some_value = some_value * 2    # 0 will be new int for the some_value. 
 
some_value *= 3                # this is the same w/ * . you can write --> some_value = some_value * 3                

print (some_value)        

print ('the squared number of 2 is' + str(some_value))  # we find INTEGER, but we want to write a string, so we need to change this integer to string using str() functions.   

