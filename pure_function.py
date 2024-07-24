#pure function
 
#rules: 
#given same input --> always return the same output
#with the same input, function that we create works --> give the same output.
#any function should not have SIDE EFFECTS. 
#SIDE EFFECT --> a function affect the outside world (screen).

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([1,2,3])) 

#is that pure function: 1st test : it produces the same output when the same input was given.
                      # 2nd rule : any side effect --> does it touch outside world? Nothing in the outside world matters to this function.
                                   #because everything is inside the function.

# example below HAVE SIDE EFFECTS!!!!
def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return print(new_list)   # print interacts w/ outside. it will print this thing on screen. we give control to print. 

(multiply_by2([1,2,3]))      #we call this function for a list.

# example SIDE EFFECT 
new_list = []                #this (outside of the function) can be modified any other developer. 
def multiply_by2(li):
    for item in li:
        new_list.append(item*2)
    return new_list  

# new_list = ''    --> here, we did a empty string as new_list. 
print(multiply_by2([2,4,8]))
