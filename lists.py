#lists: to storage of data. Used w/ [] squared brackets.  
# data is written into data ['a', 'b', 'c'], [1,2,3,4,5], etc.
# reuired data is printted using integer starting from 0. 

amazon_cart = ['notebooks', 'sunglasses', 'dress']
               # 0              1            2 

print(amazon_cart[0])   #- --> 0 refers to notebooks. 

#lists slicing
#lists can be sliced.
#in strings, specific part of the word can be written using [x (start):y(stop)]
#in lists, specific data can be written using [x (start):y(stop)].
#[x:y] -- from the x data included to y data (not included)
amazon_cart = [
    'notebooks',
    'sunglasses', 
    'toys', 
    'grapes'
]

print(amazon_cart[0:1])   # print notebooks

#the DIFFERENCE BW/ STR and LIST : String are immutable. But, list are mutable and can be changed.

amazon_cart = [
    'notebooks',
    'sunglasses', 
    'toys', 
    'grapes'
]

amazon_cart[0] = 'laptop'    # we changed the 0. data from notebooks to laptop. This is stored.
print(amazon_cart[0:3]) # we changed the amazon_chart list in the 33rd line. So, it will print laptop, sunglasses,toys.
print(amazon_cart)      # laptops, sunglasses, toys, grapes

# Instead of writting a new list --> we can duplicate the available list, then we can make some changes in duplicated list. 
                                # OR we can make some changes in the available list, then we can duplicate it. 
amazon_cart = [
    'notebooks',
    'sunglasses', 
    'toys', 
    'grapes'
]

a_char = amazon_cart           # we directly duplicate the amzon_chart list. 
print(a_char)

amazon_cart[0] = 'laptop'       # we changed 0. data
new_cart = amazon_cart[0:3]     # new list is determined as previous list including data from 0 to 3. 
new_cart[0] = 'gum'             # we changed the 0. data again. 
    
print(new_cart)
print(amazon_cart)

# COPY Method can be used. 
# new_list = previous_list.copy()
# print(new_list)

amazon_cart = [
    'notebooks',
    'sunglasses', 
    'toys', 
    'grapes'
]

amazon_cart[0] = 'laptop'      # we changed the 0.data.
new_cart = amazon_cart.copy()  # new_chart is created w/duplication of amazon_chart. 
new_cart[0] = 'gum'            # 0. data is also changed again. 
print(new_cart)   




