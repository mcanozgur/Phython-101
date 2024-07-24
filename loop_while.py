# while: similar to 'for loop'. it is a LOOP. 
# while: a condition is happening: do something.

#i = 0 
#while i < 50:     # print 0 again and again because 0 always smaller than 50.
    #print(i)      # infinite loop. program does not know when it stops. It is dangerous.

#to stop the while; BREAK 

i = 0 
while i < 50:     
    print(i)
    break        # just 0 will be printed.

#Write 0 to 50 using while loop:  

i = 0 
while i < 50:         #when this is not supplied, loop stops.
    print(i)
    i += 1   

#while - else: similar to if else, when while condition is not supplied, then else will be printed.

i = 0 
while i < 50:
    print(i)
    i += 1
else: 
    print('done')

# NOTE! : else works if BREAK is not available after while. 

i = 0 
while i < 50:
    print(i)
    i += 1
    break
else: 
    print('done')      #just 0 is printed. After 1st loop, while loop stops w/break. 
                       #else condition not work !
