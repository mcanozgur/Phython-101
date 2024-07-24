#Dictionaries  -- a data type.  
# written using curly brackets {}
# dict. is an UNORDERED key value pair.
# includes many distinct type of data. 
# key is name of variable, value is the data of variable.

# data in dictionary --> get using the key name. print(dictionary['key name'])
#if key name is present in the dictionary, value is is found and printed.

# !! In the list, if you want to learn a data in list. print(listname[0]) --> index O is found and printed.

dictionary = {
    'a' : 1,      #a = key, 1 is a value
    'b' : 2,      #b = key, 2 is a value of key b. 
    'x' : 3


}

print(dictionary['b'])   #find key b, and if it exists, grab me the value. 

#Inside dictionary,values can be a integer, string, LIST, boolean (True, False)

dictionary = {
    'a' : [1,2,3,4,5],      
    'b' : 'hello',
    'x' : True


}

print(dictionary['a'][1])   #find key a, and print the first item on this list. (It is similar to matrix. We used two brackets, first bracket refers to subarray, the second on the item on this subarray)

#The list can be avaliable in a dictionary or a dictionary can be available in a list.

my_list = [                            #this is a list, but it includes 2 distint dictionaries.
{
    'a' : [1,2,3,4,5],          #the value can be list
    'b' : 'hello',              #the value can be string
    'x' : True                  #the value can be boolean
},

{
    'a' : [1,2,3,4,5],      
    'b' : 'hello',
    'x' : True
}
]

print(my_list[0]['a'][2])   #find index 0 in list.. this is the first dicionary.
                            #find 'a' key in this dictionary.
                            #find the 2nd index in this a list. 
                            #it print 3.