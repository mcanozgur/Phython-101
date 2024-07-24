#conditional logic
#booleans are very important

is_old = True
is_licenced = True

if is_old: 
    print('you\'re old enough to drive')

is_old = False
is_licenced = True

if is_old: 
    print('you\'re old enough to drive')  #if condition is not supplied, then this will not be printed.
print('checheck')   # this will be printed.

# for otherwise condition: if - else 
is_old = False
is_licenced = True

if is_old: 
    print('you\'re old enough to drive')
else: 
    print('checheck')

# if there more than 1 condition, elif is used. 
is_old = True
is_licenced = True

if is_old: 
    print('you\'re old enough to drive')    #it is ture, so it will be printed. Other options will be ignored.
elif is_licenced:  
    print('you can drive it')
else:
    print('by by')    # you are old enough to drive. when the first condition is supplied, then it will be printed.

is_old = False
is_licenced = True

if is_old: 
    print('you\'re old enough to drive')    #this is false
elif is_licenced:  
    print('you can drive it')               #this is true. so this will be printed.
else:
    print('by by')    

is_old = False
is_licenced = False

if is_old: 
    print('you\'re old enough to drive')  #false
elif is_licenced:  
    print('you can drive it')             #false
else:
    print('by by')                        #it will be printed. 

#If 1 consition is not enough and 2 conditions sould be supplied together, then 'and' is used.

is_old = False
is_licenced = False

if is_old and is_licenced:
    print('you\'re old enough to drive and you have a licence')
else:
    print('your are not of age')     # this will be printed.

# More than 2 statement; you can use More than 1 elif. 

is_old = False
is_licenced = False
is_visible = False
is_ref = True                  #Here more than 2 options are available, then nore than 1 elif can be used for each option.

if is_old: 
    print('you\'re old enough to drive')
elif is_licenced:  
    print('you can drive it')
elif is_visible:
    print('you have visiual functions')
elif is_ref:
    print('you\'re reflexes are so good')
else:
    print('by by') 


#Truthy and Falsy

is_old = bool('hello')
is_licenced = bool(2)

print(bool('hello'))   #True -->  truthy. If false is printed, then these are falsy
print(bool(2))


if is_old and is_licenced:      #here, the variables are not true or false, so it will be checked any data is exist for these variables.
    print('you\'re old enough to drive and you have a licence') #this will be printed
else:
    print('your are not of age')



password = '12334'              #here, the variables are not true or false, so it will be checked any data is exist for these variables.
username = 'jojo'

if password and username:       
    print('you have enough info to sign in')   #this will be printed
else: 
    print('fill in the blanks')
