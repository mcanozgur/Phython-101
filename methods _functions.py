#methods and functions

#functions 
#list(), tuple(), set(), print(), max(), min(), input(), dict() are exist as function in phyton.
#we can also write and define new functions to do sonething.

# methods are used with dots. w/dot --> we access all methods.
# we learnt some methods in list(remove, clear, pop, extend, insert, append, index, sort, reverse, count), tuple(index, count), dictionary(get,pop,clear), set(difference, add, discard, clear)

print('hellooo'.capitalize())   # capatalize is a methods for strings. (upper, lower, index, find, replace -- other methods in strings)


#methods are used for strings, dictionary, lists, sets, tuples.

#there is unique thing ---> DOC STRINGS to understand the role of function

def test(a):
    '''
    Info: This function tests and prints parameter a    
    '''                                                 #we can define function role. When we call this function, the role of function will be observed (same w/ functions used in phyton)
    print('a')

test('melike')

# docs string is written into ''' .  

# HELP(function_name) --> also print the role of function.

help(test)

#fonksiyon ismi.__doc__ yazarak yine fonksiyonun ne yaptığını yazdırabiliriz.

print(test.__doc__)   #this __doc__ method also write the doc string in console. 

