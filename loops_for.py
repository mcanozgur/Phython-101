#For loops: run the code over and over and over
#in the conditional logic some lines are skipped, not run when 1 condition is supplied. 
#for can be used for string, list, tuple, set, etc.

for item in 'Zero to Mastery':   #string
    print(item)                  #it start w/ firts item, then continue 2nd, 3rd, 4th, ..

for item in [1,2,3,4,5]:   #list   
    print(item)

for item in {1,2,3,4,5}:   #set
    print(item)

for item in (1,2,3,4,5):   #tuple
    print(item)

for item in (1,2,3,4):
    print(item)  #ilk itemi basıcak tekrar for döngüsüne gidicek fakat aşağıda da print var. For'a geri dönmeden önce alt satırları yapıcak 
    print(item)
    print(item)

for item in (1,2,3,4):
    print(item)  #ın the first cycle, 1 will be printed.  Then, second cycle, 2 will be printed
    print(item)                     # 1 will be printed.                      2 will be printed
    print(item)                     # 1 will be printed.                      2 will be printed

print('hi') #when the for loop was completed, hi will be printed.

for item in (1,2,3,4):
    print(item)  #1 will be printed for 3times for the first loop. Then other items will be printed for 3times.
    print(item)
    print(item)
print(item)      #when for loop was completed, the last item will be printed again.

# Two for Loop: 
for item in (1,2,3,4,5):
    for x in ['a', 'b', 'c']:        #outer loop, firstly 1 will be get. and 1 a, 1 b, 1 c will be printed.
        print(item, x)


#ITERABLES: it is an object or a collection that can be itarabled over.
#In for loops, we can use iterable object. 

#iterable can be LIST, DICTIONARY, TUPLE, SET, STRING becuase they can be iterated. 
#iterated -> one by one check each item in the collection.

user ={
    'name' : 'melike',
    'age' : 31,
    'can_swim' : True
}

for item in user:
    print(item)       #all items will be printed in different lines.

user ={
    'name' : 'melike',
    'age' : 31,
    'can_swim' : True
}
# to print keys in for loops: 
for key in user.keys():
    print(key)

# to print values in for loops:
for values in user.values():
    print(values)

# to print items (keys + values) in for loops: 
for items in user.items():
    print(items)

#to make more clear for items including keys and values: 

for key, value in user.items():
    print(key, value)

#In dictionaries, we can use items, keys, values methods, and get method.

print(user.items())       #all items will be printed in the same line. 
print(user.keys())        #all keys will be printed in the same line. 
print(user.values())      #all values will be printed in the same line. 
print(user.get(keys))     #all keys will be printed in the same line. 

# integer is NOT LITERABLE 

#for items in 50:
   #print(items) #error: int is not iterable. 


#exercise: count the sum of items on a list

my_list = [1,2,3,4,5,6,7,8,9,10]

print(my_list.count(2))   #if we write this, it counts only 2 in list. 

counter = 0
for item in my_list: 
    counter = counter + item 

print(counter)            #calculate the sum of values in list.

for item in my_list: 
    counter = 0
    counter = counter + item 

print(counter)        # In each loop, it will take the counter as  0.  In the last cycle, counter will be 0 and last item will be 10, so it will calculate as 10. 