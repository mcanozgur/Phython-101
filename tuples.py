# Tuples : 3rd data structure like list.
# Unlike lists = we can not modify them.
# We used () brackets.
# If you dont change your data in structure, then you can choose tuple. 

my_tuple = (1,2,3,4,5)
print(len(my_tuple))     #len function is used for tuples. 
#my_tuple[1] = 'z'

#print(my_tuple)

# Tuple cannot be modified (similar to string).

# In list, we use remove, pop, clear, insert, append, extend, sort, reverse methods.
# In tuples, we cannot use these methods because we cannot modify them.


# We can print the specific item on tuple using [].
# We can use İN keyword --> it check the data is exist or not. It prints True or False.

print(my_tuple[1])          # prints 1st index. 
print(5 in my_tuple)        # it checks 5 is available in tuple. 

# Similar to List, we can duplicate tuple and we can get the new tuple inluding just some items found in previous one.
my_tuple = (1,2,3,4,5)

new_tuple = my_tuple[1:4]   #It forms a new tuple including 1st, 2nd and 3rd item.
print(new_tuple)

#tı duplicate:   No copy method for tuple. 
new1_tuple = my_tuple
print(new1_tuple)


# * other is used for list. *other are also used in tuples. 

x,y,z, *other = (1,2,3,4,5)

print(x)
print(other)


#tuples have only 2 methods: count() and index()
#count: we used in list to count a data in a list. Similar to list, we can use it for tuples.
#index: we used in list and string to find the index of specific item.

my_tuple = (1,2,3,4,5,5,5,5)

print(my_tuple.count(5))    #print 4

print(my_tuple.index(3))    #print 2
