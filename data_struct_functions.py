# map(), filter, zip and reduce functions --> useful and common functions
# MAP -->  simplfy the code. 
# map, filter, zip : 
# map or filter or zip(functions (means the action, what we want to do), dataset)

# map(action, [1,2,3]) 
     #a function
              #a dataset
                         
# --> action is what we gonna take action. [1,2,3] --> the dataset to take action

#if our aim is to multiply the all data in a list. Then;
# we can use the for loop, and multipy the each item on list uisng for loop.
# Instead of for loop; we can use MAP FUNCTION to apply any function for all data in a list, set, tuple, etc.

def multiple(li):
    new = []
    for item in li:
        new.append(item*2)
    return new

map(multiple, [1,2,3])            #this will not print anything because there is no any print inside function. Therefore, we need to print this function. 

print(map(multiple, [1,2,3]))     #map object at ****. Prints the storage area in memory.
print(multiple([1,2,3]))          #it print the output of function

# Instead of FOR LOOP; we can use MAP FUNCTION. 

def multiple(item):
    return item*2

print(list(map(multiple, [1,2,3])))  #we call the multiple function using map. 
               #multiple function for a list will  be done
           #map will supply the function for each item in list
      #a list will be formed 
#list will be printed

# w/o FOR LOOP, we can apply the same function for each item using MAP FUNCTION.

my_list = [0,2,3]

def multiple(item):
    return item*2       #no side effect in this function

print(list(map(multiple, my_list))) #prints 0,4,6
print(my_list)     #it will print normal my_list 0,2,3
 
# exercise: 
# you have usernames in a list, and you yant to make the all letters capatalize.
# w/o for loop, we just write a function incluidng what we want to do. 
# here, our aim is to make all letters capatalize. So, we need to used upper() method.
# item.upper() will be used in a function. Then, then we use map function for this function.

user_list = ['melike', 'güven', 'özgür', 'hüseyin']

def cap_user(item):
    return item.upper()

print(list(map(cap_user, user_list)))

# FILTER (): we can filter some of our results. 
# just give the correct results in the function.

my_list = [0,2,3,5,6,7,8,9]

def check_odd(item):
    return item % 2 != 0 

print(list(filter(check_odd, my_list)))   #filter ile sadece true döncenleri vericek.
                  # function will be done for my_list dataset
           #just correct results will be filtered
      #list will be formed
#list will be printed

#exercise
#find the data with starts w/ 'g' letter in a list

user_list = ['melike', 'güven', 'özgür', 'hüseyin', 'gözde', 'gizem', 'goven']

def cap_user(item):
    if item [0] == 'g':
        return item
    
print(list(filter(cap_user,user_list)))  #just correct things will be printed.

print(list(map(cap_user, user_list)))    #in that condiditon: melike, hüseyin will be printed as none. 

#ZIP --> to zip two lists, tuple, etc.

y =[1, 2, 3]       #list
z = [10,20,30]     #list

print(list(zip(y, z)))   #it zips the first item of first list to the first item of second list. 
                         #(1,10), (2,20),(3,30)

#example: 
a = (1,2,3)    #tuple
b = ['a', 'b', 'c'] #list

print(list(zip(a, b)))    #zip list and tuple. 


#example:
a = (1,2,3)    #tuple
b = ['a', 'b', 'c'] #list
c = (3,4,5)    #tuple

print(list(zip(a, b, c))) #(1,'a',3), (2,'b',4), (3,'c',5)


#REDUCE  (function, dataset, value of initial)
#reduce is found is functools so tihs return() function should be imported.
#to reduce a list or accumulate a list --< reduce() function can be used.
#it can be used to sum all data in a list.

from functools import reduce   

my_list = [1,2,3,4,5,6]

def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulator, my_list, 0))   #0 = acc



