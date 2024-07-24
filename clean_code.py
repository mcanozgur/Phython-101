#clean code 

def is_even (num):
    if num % 2 == 0:
        return ('True')
    elif num % 2 != 0:       #actually, it is not necessary.
        return ('False')
    
print(is_even(50))


#to make more clean code: there are only 2 stiation, so intead of elif, we can use else

def is_even (num):
    if num % 2 == 0:
        return ('True')
    else:
        return ('False')
    
print(is_even(50))

# to wirte more clean code, we may not use else.

def is_even (num):
    if num % 2 == 0:
        return ('True')       #if it is correct, the it will return true, but it is not correst, the it will skip this line and follow the next line. so return false.
    return ('False')
    
print(is_even(51))

# to make more clean:

def is_even (num):
    if num % 2 == 0:
        return ('True')
    
print(is_even(51))           #51 is not even, so it will return None, because we did not define the false condition. 


