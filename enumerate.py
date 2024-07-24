#enumerate() similar to range, to show index.
#it is useful for index counter. 

for x, y in enumerate('Helloooo'):
    print(x, y)                         # only one x or y can be written. But we get both index and string character, so to be more clear, two variable can be used.
                                        # x refers to index, y referst to characters in string.

for x, y in enumerate([1,2,3,4,5,6,7,8,9,10]):
    print(x, y) 


#exercise. we wonder the index of 50 in a list from 0 to 100.

a_list = list(range(0,100))

for index, number in enumerate(a_list):
    if number == 50: 
        print(index)
