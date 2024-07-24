#function : we can form a new function w/ def. 
#def function_name(): 
#to call the function: function_name()

def say_hello():
    print('helooooooğğğğ')   

say_hello()   #when we call this function, 'helllooooğ' will be printed.

#In GUI, we aimed to draw a tree using matrix. 
#Instead of writing long code again, we can write a function and we call it again and again. 

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0]
]

def tree_fun():
    for list_m in picture:
        for each_number in list_m:
        if each_number == 0:
            print(' ', end='')             # boşluklu siyah yapsın diye. 
        elif each_number == 1:
            print('*', end='')             # her seferinde yeni bir line'a yazıyordu zaten. yine öyle oldu.
    print('') 

tree_fun()
tree_fun()

print(tree_fun) #storage in memory. 