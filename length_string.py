#string indexes: [] is used to print the int or letter in the required region in a str, list, tuple, etc..
# [start:stop] -- strat is inclued, stop is not included. (It starts from the 0).
# [start:stop:stepover] star included until the stop, stop is not included, stepover -- to write w/ specific gaps. 
# [- minus value] starts at the end. It starts from the 1).


selfish = 'me you us'
          #012345678

print(selfish[0])         #print m 
print(selfish[1:4])       #print e y
print(selfish[1:8:3])     #print eou
print(selfish[-2])        #print u


# len() function ---- length of the string.

print(len('helloooooo) ')) 

greet = 'hellooooo'
print(greet[0:5])

print(greet[1:2]) 

print(greet[0:len(greet)])

quote = 'to be or not to be'

# Methods for Strings

# variable. --> available methods are shown.
# capatalize()  -- uppercase leeter for just first letters of words.
# upper ()      -- uppercase for all letters
# lower ()      -- lowercase of rall letters
# find  ('what you want to find')          -- if it is available, it shows the index of it.       
# index (' anything in a string, list, etc.')      -- to learn index of the written thing.
# replace (x,y) -- x is available thing in the variable, y is the new thing to replace. 
 
print(quote.capitalize())    # to write uppercase of the first leters.

print(quote.upper())         # to write uppercase for all letters.

new_quote = 'MELIKE'

print(new_quote.lower())     # to write lowercase for all letters.     

#find deyince hangi yerde olduğunu söylüyor 0dan başlayarak saymaya. boşlukları da sayıyor. 

print(quote.find('or'))
print(quote.index('or'))   #index'i llistede kullanıyorduk. nerde olduğunu buluyor. 'dan başlayarak


print(quote.replace('be', 'me')) # be and me is replaced. print to me or not to me.

quote_2 = quote.replace('be', 'me') # quate_2 is new variable and it is also quote but, replaced be and me. 
print(quote_2)   # it prints print to me or not to me
print(quote)     # it print to be or not to be. because we did not change it completely. Just we change it w/method in line 53 and print it there. 

quote.replace('be', 'me')
print(quote)              # it also print to be nor not to be since strings are immutable.

#STRINGS ARE IMMUTABLE:

string_immutable = 'melikeee'

# string_immutable[0] = 'k'   --> immutable ! Strings can not be changed ! 
print(string_immutable)     

#booleans TRUE or FALSE
# bool(0) means the FALSE 
# bool(1) means the TRUE

name = 'melike'

print(bool(0))       #print false
print(bool(1))       #print true
print(bool('true'))  #print true

#type conversion

print(str(100))        #100

print(type(str(100)))  #str

print(type(int(str(100)))) #int

a = str(100)  
b = int(a)
c = type(b)
print(c)               #int

#Escapse Sequence: 

# we use ' ' to write string. But sometinmes we want to use ' inside string. 
# example:  'it's a sunny day' --> first ' -- is start, the second ' -- is stop. Here, the third one is actually stop. 
# to prevent this condition, we can use " for start and stop separately.
# But the best option is the usage of  \ 
# when phyton interpreter comes to \ sign, it knows that what comes after this \, it is a string, and then continue. 
# \t means the tab
# \n means the new line

x = 'it\'s a \'kind of\' sunny day'
x = "it\'s a 'kind of' sunny day"

print(x)


wheather_2 = '\t wheather is very cold'
print (wheather_2)

statement = '\t today is too hot \n \t tomorrow will be also hot'

print(statement)

# formatted strings

# f 'string' -- f is used 
# if we need to write an integer or variable (include integer) in  a string, we need to change of type from int to str. 
# but ıf we use formated string, the no need type conversion.

name = 'melike'
age = 31

print('hi ' + name + ' you are ' + str(age) + ' old')
                                 # need to convert int to str.

print(f'hi {name} you are {age} old')

#If there is the same variable (more than one). The last updated variable is used. 

name = 'melike'
age = 10
relationship = 'single'

relationship = 'it\'s complicated'   #this updated one will be used. 

print(relationship)     #it is comlicated.

#exercise : calculation of the age of a person

birth_year = input('what year were you born?')

age = 2024 - int(birth_year)

print(f'your age is {age}')

print('your age is ' + str(age))




