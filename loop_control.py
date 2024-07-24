#break, continue, pass

#BREAK and CONTINUE i used in FOR and WHILE LOOP.

my_list = [1,2,3]

for item in my_list:
    print(item)
    break        # JUST 1 will be printed

i = 0 
while i < len(my_list):
    print(my_list[i]) 
    i+=1        
    break       # JUST 1 will be printed

#CONTINUE seems like useless :) it returns the while or for loop line whatever happens.

my_list = [1,2,3]

for item in my_list:
    print(item)
    continue       # 1, 2, 3 

i = 0 
while i < len(my_list):
    print(my_list[i]) 
    i+=1        
    continue       #  1, 2, 3 

#if continue is written before print, then while and for loops will be performed for each condition again and again.  

my_list = [1,2,3]

for item in my_list:
    continue                # it goes for.
    print(item)             # loop continue again and again, item will not be printed.

#PASS: not very useful. essentially does nothing
#it is usefull to pass new line. 
my_list = [1,2,3]

for item in my_list:
       print(item)
       pass                   