#List Compherension
#Set compherension
#Dictionary compherension

#Compherension --> quick way to create lists, sets, or dictionaries. To make clean and shorter lists, dic., etc.  
#Instead of looping or appending an item to list.

#exercise  --> create a list from characters in a string
my_list = []
for char in 'hello':
    my_list.append(char)

print(my_list)           


#Instead of For Loop:

my_list = [x for x in 'hello']    
#just in a 1 string, we did the same thing. For loop is in the list
#for each x in hello, create a list
print(my_list)

#exercise -- to create a quick list w/ numbers from 0 to 100

my_list2 = [number for number in range(1,100)]
print(my_list2)

#OR

print(list(range(0,100)))

#OR
#FOR LOOP: 
y = 0
list = []
for y in range(1,100):
    y += 1 
    list.append(y)
print(list)
    
#exercise: multiply each item w/ 2 from 0 to 100 and create a list

mc_list = [(number*2) for number in range(0,100)]

print(mc_list)

# Keep only even numbers in mc_list
# Long way :( 

a = []
for number in range(0,100):
    if number % 2 == 0: 
        a.append(number)
    print(number)
print(a)

#w/list compehrension --> shorter and cleaner code. 

b = [num*2 for num in range(0,100) if (num*2) % 2 == 0]
        # both for and if are used together. 
print(b)


#Set Compherension
#is similar w/ lists. 

my_set = {x for x in 'hello'}
print(my_set)

my_set2 = {number for number in range(1,100)}
print(my_set2)

mc_set3 = {(number*2) for number in range(0,100)}
print(mc_set3)

#Dictionaries Compherension
simple_dict = {
    'a' : 1,
    'b' : 2
}

# create a dict with squared of values.

my_dict = {key:value**2 for key,value in simple_dict.items()}
print(my_dict)   #here, both key and values will be printed

#OR
print(simple_dict.items())

a_dict = {value**2 for value in simple_dict.values()}
print(a_dict)    #here, just squared values of values in dict will be printed w/o keys.

# to write only keys in dict.
my_dict2 = {key for key in simple_dict.keys()}
print(my_dict2)
#OR
print(simple_dict.keys())

#just write even squared values in dict.
my_dict3 = {v**2 for v in simple_dict.values() if (v**2) % 2 == 0 }
print(my_dict3)

#exercise: find duplicated data in list.

some_list = ['a', 'b', 'c', 'd,', 'b', 'n', 'n']

duplicates = []
for items in some_list:
    if some_list.count(items) > 1 and items not in duplicates:
        duplicates.append(items)

print(duplicates)
 
#OR

duplicates_1 = [items for items in some_list if some_list.count(items) > 1] 
print(duplicates_1)

#böyle yazınca iki kere basıyor. Aslında listede olanı tekrarlamasını istmeiyoruz.
#fakat items not in duplicates_1 'da diyemiyoruz çünkü önceden tanımlanan boş bir liste ile başlamadık.
#BU DURUMDA SET YAPMAMIZ LAZIM !!!!

duplicates_1 = set([items for items in some_list if some_list.count(items) > 1])
print(duplicates_1)

#set yaparken set yazarız, list yaparken ise list yazarız. Oluşturduğumuz listenin basına set yaparak set'e dönüştürüz. 
#böyle olunca da set şeklinde yazdı çünkü set'e dönüştürdük.
#liste istiyorsak bunu da listeye dönüştürmek lazım.

#duplicates_1 = list(set([items for items in some_list if some_list.count(items) > 1]))
#print(duplicates_1)