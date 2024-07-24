#find duplicates

#find the duplicates in a list. 

some_lists = ['a', 'b', 'c', 'c', 'b', 'd', 'm', 'm', 'n']


for item in some_lists:
    if some_lists.count(item) > 1: 
        print(item)               # each item will be checked and if count>1, then it will be printed.

for item in some_lists: 
    if some_lists.count(item) > 1:
        print(list(item))          #for each item, it will do new list.

duplicates = []
for item in some_lists: 
    if some_lists.count(item) > 1:
        if item not in duplicates:  # not in is used.
            duplicates.append(item) # the item will be added to empty list.
    
print(duplicates) #this will be production of new and 1 list. 

