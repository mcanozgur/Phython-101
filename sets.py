# sets: is a data type. 
# Unordered collections of unique objects. No repeated item!
# {} is used to form a set.

my_set = {1,2,3,4,5}

print(my_set)


#In set, if there are repeated items, 'it only returns the unique sets or unique items' no duplicates ! 

a_set = {1,2,3,4,5,5,6,6,6}

print(a_set)  #it prints {1,2,3,4,5,6}

#In tuples, there are only 2 methos: index and count since they cannot be changed.
#In list, there are many many methods: to remove, pop, remove, clear; to add, insert, extend, append; to reverse reverse; to sort sort; index


#In sets; 
#Adding --> add(data) metod. 
#If you add the same thing that exist in the set, then it will not be added. It prints the previous tuple. 

my_set = {1,2,3,4,5}

my_set.add(100)  
my_set.add(5)     #5 is not added beacuse 5 is already exist. 
print(my_set)

# In sets:
# removing; 
# remove(required data) -- same w/list.
# discard(required data)

my_set = {1,2,3,4,5,6}
my_set.discard(5)   #it removes 5.
print(my_set)

my_set.remove(6)    #it removes 6.
print(my_set)

# clear --> clear all set.

a_set = {10,20,30,40,50}
a_set.remove(10)
print(a_set)

a_set.clear()
print(a_set)

#copy()

b_set = a_set.copy()
print(b_set)

my_set = {1,2,3,4,5,6,7}

my_set.copy()

print(my_set)   

# TASK : you have a list including repeating things. You want to create and return a list or a collection that has only unique items.
# you can convert the list to set using SET FUNCTION
# you can also use list function to convert the set using list function.
 
my_list = [1,2,3,4,5,5,5,6,6,6]

print(set(my_list))

# In list, dictionary, string, we can use [0:4] to find and print specific data.
# BUT, IN SET, WE CANNOT USE [NUMBER:NUMBER].  

my_set = {1,2,3,4,5,5,5,6,6}

# print(my_set[0])   #NOT WORKING

# in keyword: we used in list, dictionary, etc.

my_set = {1,2,3,4,5,5,5,6,6}

print(2 in my_set)   #true 

# len function is used for sets. 
# len is also used for list, strings and tuples. 

my_set = {1,2,3,4,5,5,5,6,6}

print(len(my_set))   #6 is printed. 

# set can be changed to list.

my_set = {1,2,3,4,5,6,7}

print(list(my_set))    #listeye çevrilmiş halini [1,2,3,...] diye yazar. 

# other methods in sets (for adding add; for removing remove and clear; for copy cop())
# difference. --> to find differences

my_set = {1,2,3,4,5,6}
your_set = {4,5,6,7,8,9,10}

print(my_set.difference(your_set)) # find the different items in my_set. 1,2,3
print(your_set.difference(my_set)) # find the different items in your_set.


#difference_update : remove all elements from another set 
my_set = {1,2,3,4,5,6}
your_set = {4,5,6,7,8,9,10}

my_set.difference_update(your_set)   #mysetteki difference'i update edip myseti değiştiriyor.
print(my_set)

#intersection #isdisjoint #issubset
my_set = {4,5,6}
your_set = {4,5,6,7,8,9,10}

print(my_set.intersection(your_set)) # shared items are printed. my_set & your_set do the same thing.
print(my_set.isdisjoint(your_set))   # isdisjoint . the shared values are available so FALSE. 
print(my_set.issubset(your_set))     # issubset.  TRUE 
print(my_set.union(your_set))        # unioun my_set and your_set. 
print(my_set.issuperset(your_set))   # my_set includes all elements in your_set? FALSE
print(your_set.issuperset(my_set))   # your_set includes all elements in my_set ? TRUE