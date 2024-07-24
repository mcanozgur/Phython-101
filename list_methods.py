#List Methods: 

# len is a function. We used in str. It is used for the length of the string (character number in a list)
# len function is also used in List to determine the number of data inside the list. 

basket = [1,2,3,4,5]

print(len(basket))   # Data number will be printed. 5. 

# ADDING METHODS in LISTS: 
# append(a). --> to extend the list. a --> new data to add at the end of list.
# insert (a,b) a--> refers to which index in the list. b --> refers to new data to add into list.
# extend (a, b, c, etc.) --> to extend the list w/new data.
# NOTE! some methods --> not return. Look at the example below. 

# print(basket.append(100)) # NOT work. It prints NONE. It means this method --> not return. 

basket.append(100)  # we add 100 into the basket list frstly. 
print(basket)       # we print basket list. 

#insert()
basket = [1,2,3,4,5]

basket.insert(4,100) #4 --> index, 100 --> new data to be insert.  
                     #REMEMBER! in str --> we write the methods--> print(string_example.(capatalize, upper, lower, find, index, replace,etc.)

print(basket)

a_list = ['a', 'b', 'c', 'd']
a_list.insert(1, 'x')   # we will add 'x' in the 1st index. 
print(a_list)

#extend()

basket = [1,2,3,4,5]

basket.extend([70, 100]) 

print(basket)

# REMOVING Methods 
# pop() --> removes the data at the end of the list. pop() -- it removes the just 1 data at the end of list.  
# pop(index) --> number refers to index.
# remove(data) --> same w/ pop. The required data is removed from the list.
# clear --> to clear all data in a list.

basket.pop() # we add the 70, and 100. w/pop()-- we remove 100. 
print(basket)

basket.pop(1) #1st index -- it refers to 2, 2 will be removed. 
print(basket)

#remove(data is written here to remove it)

basket.remove(4)   # it removes 4 as data. 
print(basket)

a_list.remove('b') # it is written data that will be removed. 
print(a_list)


#clear: removes whatever in the list. 

basket.clear()
print(basket)


#index(data) --> print the index of the data in list.

basket = ['a', 'b', 'c', 'd', 'e']

print(basket.index('d'))

# keywords in phyton:
# in keyword is used to understand whether a data is exist or not. 

print('x' in basket)    #false 

print('i' in 'pencil')   #true

#count(data) --> count the data in list. 

print(basket.count('d'))  #1 because there is only 1 'd' data in list. 

#sort() --> sort the list.  

basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']

print(basket.sort())    #It print NONE --> not return. The same thing was also observed in clear, remove, append, insert, extend, etc. 

basket.sort()
print(basket)

#sort() is a method. But there is a function to sort data in list.  
# SORTED is a function.
 
basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']

print(sorted(basket))   #same role with sort() method. 
print(basket)           #Here, not-sorted data will be printed. Because the data is not changed. 

basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']

basket.sort()           

print(sorted(basket))   #it will print sorted data.
print(basket)           #it will print sorted data. In 105. line, we sort the list using sort() method, then we print it. 

# COPY LIST
# a_list = new_list 
# a_list = new_list[:]
# a_list = new_list.copy() 

basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']

new_basket = basket.copy()    # copy() method and [:] have the same roles. 
new_basket = basket[:]
new_basket.sort()            
print(new_basket)

# REVERSE() Method
# to reverse the list. 

basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']

basket.reverse()
print(basket)

#Instead of reverse() method --> reverse can be done w/ [::-1]

basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']

basket.sort()       #sorting
basket.reverse()    #after sorting, the reverse was done.
print(basket[::-1]) #again reverse 
print(basket)       #print sorted data. 


# RANGE Function
# if you want to do a lists from a range to range, ranfe function can be used.

print(range(1,100))       #NOT WORK. We write a list firstly.
print(list(range(1,100))) #it creates a new list from 0 to 100.

print(list(range(100)))   #it created a new list, but it starts from 0.
       

#list unpacking 

a, b, c, d = [1, 2, 3, 4]
print(a)
print(b)
print(c)

# *other in  along list 

a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a, b, c)   #it
print(*other)    #it prints all data except 1,2,3,9
print(d)         #it prints 9

#NONE: some mthods print NONE when methods are written into print. NOT RETURN
#Therefore,  firstly, method should be written in a line, then it can be printed.

weapons = None   #It means no any weapon.

print(weapons)   #It prints None, because no weapons. 


#join is a string method 

sentence = '\n'
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'melike']) #we join the gaps with join method.
#new_sentence = '\n' .join(['hi', 'my', 'name', 'is', 'melike']).  the same thing.
print(new_sentence)    