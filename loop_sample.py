# for and While loop

my_list = [1,2,3]

for item in my_list:
    print(item)        # 1, 2, 3

i = 0 
while i < len(my_list):
    print(my_list[i]) 
    i+=1               #1, 2, 3 

#while ve for are very similar loops
#while flexible. there is a condition, can do more things.
#for loops are easier. 

while True:
    input('say something: ')
    break    #say something will printed and stoped !

while True:
    response = input('say something:  ')
    if (response == 'bye'):
        break                     # if by is written then stop !Otherwise, same something will be written in console. 
    