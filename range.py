#range FUNCTION is commonly used when we create a new list including any range.  

print(range(100))   # error. Firstly, we need to create a list, set, tuple, etc. 

#range is also used for tuples, setts. 
print(set(range(1,100)))      #from 1 to 100. 100 is not included.
print(list(range(1,100)))
print(tuple(range(1,100)))
print(list(range(10, 0, -2)))

#if we want to write from 0 to 100 in distinct lines w/o creat. a list, tuple, set; 
#we can use for loop:
for number in range(0,100):
   print(number)                      #from o to 100. 
   

for number in range(0, 10):           #for each number from 0 to 10;
   print('email email list')          #it will print this string.

for number in range(0,100, 2):        #range (start, stop, stepover).
   print(number)                      #0 ,2,4,...., 98

for x in range(10, 0, -1):            # for each x from 10 to 0: print x. 
   print(x)                           # - means opposite direction.

for x in range(10, 0, -2):            # - opposite direction. Stepover 2
   print(x)

for a in range(2):                   # 2 means: from 0 to 2. First. for 0, it will print a list. Then for 1, it will print a list again. 
   print(list(range(10, 0, -2)))                