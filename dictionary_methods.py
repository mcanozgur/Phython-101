#data structures : LISTS & DICTIONARIES. There are also tuple, set, etc.
#dictionary is not ordered. UNoredrd key and value pair.
#lists is ordered. It includes the related data.
#dictionaries have more (kind of) information than lists. A list can be also stored in a dictionary. A dictionary can also be stored in a list.
 

dictionary = {
    'weapons' : [1,2,3,4],
    'greeting' : 'hello',
    'is_magic' :  True
}

print(dictionary['weapons'])    #print [1,2,3,4]
print(dictionary['is_magic'])   #print True

# KEYS IN DICTIONARY    
# keys in the dictironaries should be immutable, not change!!. 
# Each key is stored in a memory, and should not be CHANGED.
# as we learnt previously, a string cannot be changed! But A LIST CAN BE CHANGED. 
# A list can not be a  key name. ex: [1,2,3] = value cannot be a list name.
# A string (ex: 'my_data' can be a key name)
# A value (ex: 123 can be a key value) 
# True or false  can be a key value --> these are not changed. 
# Keys are generally a string that determine the value. 
# Specific and different key for each value.

dictionary = {
    123 : [1, 2, 3, 4],
    True : 'hello'
    #[100] : True      # the key is a list, so it is mutable, so it causes error.
}

#print(dictionary([100]))

# GET Method
# get.(key name) --> get the value of required key.

user = {
    'basket' : [1,2,3,4],
    'greet' : 'hello'

}
print(user.get('age'))      #None --> becuae no age key.

print(user.get('age', 55))  # if age does not exist on the dic., print 55 as a default value.


# Dict Function
# dictionary can be formed using dict. function.


user2 = dict(name = 'Melike', 
             age  = '35', 
             surname = 'can')

print(user2)    #it will produce a dictionary. It print a dictionary including key and value pair inside curly brackets {}

# Methods in Dictionary
# keys()    
# values() 
# items()

user = { 
 'basket' : [1,2,3],
 'greet' : 'hello',
 'age' : 20 
}


print(user.keys())    #it prints all keys in user dic. 
print(user.values())  #it prints all values in user dic.
print(user.items())   #it prints all key and values in user dic.

# in a keyword in LIST
# In dictionary, we can use the in dict as keyword. It prints True or False.
# get(key_name) method print the values in key name. 
# in keyword only checks whether this key or value is avaliable in dict or not.

print('basket' in user)     # it check whether basket key name is available or not. 
print(user.get('basket'))   # it prints the basket list. [1,2,3]
print(user['basket'])       # it prints the basket list. [1,2,3]

print('age' in user.keys())         #it prints true  
print('hello' in user.values())     #it prints true


# Clear() Mehod  (it is also used in list)
# clear the dict. 

user.clear()
print(user)

# Copy() is a method (it is also used in list)
# to copy the dictionary 

user = { 
 'basket' : [1,2,3],
 'greet' : 'hello', 
 'age' : 20
}

user2 = user.copy()  

print(user2)

#pop() (it is also used in list)
# to remove a key value pair in a dict.
# pop(key_name)--> the written key name and its value is removed.
# popitem() --> it removes any key and pair.  
# In list, pop() --> removes the last item in list. 
# In list, pop(index) --> removes the data at specific index in list. 

print(user.pop('basket'))   #basket and its value is removed.

#print(user.popitem())    #ay item (key and value pair) is removed.

#update Metod
#update('key_name', new updated value) 
#to update a value in dictionary

user.update({'age',  55})  #yaşı 55e çevirdi.
print(user) 